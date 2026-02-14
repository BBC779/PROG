import json
import re
import time
import threading
import sqlite3
import requests
from datetime import datetime
import feedparser

from flask import Flask, request, jsonify, render_template_string

# Optional TTS/STT
import pyttsx3
import speech_recognition as sr

# Selenium for autonomous browsing
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# ------------------- CONFIG -------------------
app = Flask(__name__)
last_activity_time = time.time()
learning = False
conversation_history = []

# ------------------- HUGGING FACE API -------------------
HF_API_TOKEN = "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"
HF_MODEL = "EleutherAI/gpt-neo-2.7B"
HF_API_URL = f"https://router.huggingface.co/models/{HF_MODEL}"

def hf_response(prompt):
    headers = {"Authorization": f"Bearer {HF_API_TOKEN}"}
    payload = {
        "inputs": prompt,
        "parameters": {"max_new_tokens": 200, "temperature": 0.7}
    }
    try:
        response = requests.post(HF_API_URL, headers=headers, json=payload, timeout=60)
        data = response.json()
        if isinstance(data, list) and "generated_text" in data[0]:
            return data[0]["generated_text"]
        elif isinstance(data, dict) and "error" in data:
            return f"HF API error: {data['error']}"
        else:
            return str(data)
    except Exception as e:
        return f"HF request error: {e}"

# ------------------- DATABASE -------------------
conn = sqlite3.connect('ai_memory.db', check_same_thread=False)
c = conn.cursor()

c.execute('''
CREATE TABLE IF NOT EXISTS memory (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    role TEXT,
    content TEXT,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
)
''')
c.execute('''
CREATE TABLE IF NOT EXISTS knowledge (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    topic TEXT,
    content TEXT,
    source TEXT,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
)
''')
conn.commit()

# ------------------- SETTINGS -------------------
SETTINGS = {
    "news_sources": ["https://news.google.com/rss", "https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml"],
    "wikipedia_topics": ["Artificial intelligence", "Python (programming language)"],
    "scrape_frequency_minutes": 10
}

def save_settings():
    with open("settings.json", "w", encoding="utf-8") as f:
        json.dump(SETTINGS, f, indent=4)

def load_settings():
    global SETTINGS
    try:
        with open("settings.json", "r", encoding="utf-8") as f:
            SETTINGS = json.load(f)
    except:
        save_settings()

load_settings()

# ------------------- TTS/STT -------------------
tts_engine = pyttsx3.init()
recognizer = sr.Recognizer()
mic = sr.Microphone()
VOICE_ENABLED = True  # Voice default on

def speak(text):
    if VOICE_ENABLED:
        tts_engine.say(text)
        tts_engine.runAndWait()

def listen():
    try:
        with mic as source:
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source, timeout=5)
        return recognizer.recognize_google(audio)
    except:
        return None

# ------------------- DATABASE FUNCTIONS -------------------
def store_message(role, content):
    c.execute('INSERT INTO memory (role, content) VALUES (?, ?)', (role, content))
    conn.commit()

def store_knowledge(topic, content, source="news"):
    try:
        c.execute('INSERT INTO knowledge (topic, content, source) VALUES (?, ?, ?)',
                  (topic, content, source))
        conn.commit()
    except Exception as e:
        print("Knowledge storage error:", e)

def retrieve_relevant_knowledge(query, top_k=3):
    try:
        c.execute('SELECT topic, content FROM knowledge')
        rows = c.fetchall()
        scored = []
        for topic, content in rows:
            score = len(set(query.lower().split()) & set(content.lower().split()))
            if score > 0:
                scored.append((score, content))
        top = sorted(scored, reverse=True)[:top_k]
        return [t[1] for t in top]
    except Exception as e:
        print("Knowledge retrieval error:", e)
        return []

# ------------------- NEWS + WIKI LEARNING -------------------
def learn_from_sources():
    global learning
    learning = True
    print("AI: Learning news and Wikipedia topics...")
    # News
    for source_url in SETTINGS["news_sources"]:
        try:
            feed = feedparser.parse(source_url)
            for entry in feed.entries[:5]:
                title = entry.title
                summary = getattr(entry, "summary", "")
                content = f"{title} - {summary}"
                store_knowledge(topic=title, content=content, source="news")
        except Exception as e:
            print("News learning error:", e)
    # Wikipedia
    for topic in SETTINGS["wikipedia_topics"]:
        try:
            url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{topic.replace(' ', '_')}"
            headers = {"User-Agent": "WebLearningAI/1.0"}
            r = requests.get(url, headers=headers, timeout=5)
            if r.status_code == 200:
                data = r.json()
                content = data.get("extract", "")
                store_knowledge(topic=topic, content=content, source="wiki")
        except Exception as e:
            print("Wikipedia learning error:", e)
    print("AI: Finished learning sources.")
    learning = False

# ------------------- AUTONOMOUS BROWSING -------------------
def browse_and_learn(url):
    global learning
    learning = True
    print(f"AI: Browsing {url} ...")
    try:
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get(url)
        time.sleep(3)
        paragraphs = driver.find_elements("tag name", "p")
        content = "\n".join([p.text for p in paragraphs if p.text.strip()])
        driver.quit()
        if content:
            store_knowledge(topic=url, content=content, source="web")
            print(f"AI: Learned content from {url}")
    except Exception as e:
        print(f"Browsing error: {e}")
    learning = False

# ------------------- AUTONOMOUS TASK SCHEDULER -------------------
def autonomous_tasks():
    while True:
        try:
            time.sleep(SETTINGS["scrape_frequency_minutes"] * 60)
            print("AI: Running autonomous tasks...")
            learn_from_sources()
            if SETTINGS["wikipedia_topics"]:
                browse_and_learn(f"https://en.wikipedia.org/wiki/{SETTINGS['wikipedia_topics'][0].replace(' ','_')}")
        except Exception as e:
            print("Autonomous task error:", e)

threading.Thread(target=autonomous_tasks, daemon=True).start()

# ------------------- IDLE MONITOR -------------------
IDLE_SECONDS = 30

def monitor_inactivity():
    global last_activity_time
    while True:
        time.sleep(5)
        if time.time() - last_activity_time > IDLE_SECONDS and not learning:
            print("AI: Idle detected, starting autonomous learning...")
            learn_from_sources()
            last_activity_time = time.time()

threading.Thread(target=monitor_inactivity, daemon=True).start()

# ------------------- HYBRID RESPONSE -------------------
def hybrid_response(user_input):
    global last_activity_time
    last_activity_time = time.time()
    conversation_history.append({"role": "user", "content": user_input})

    if len(conversation_history) > 20:
        conversation_history.pop(0)

    user_input_lower = user_input.lower()
    if "time" in user_input_lower:
        reply = f"The current time is {datetime.now().strftime('%H:%M:%S')}"
        store_message("assistant", reply)
        speak(reply)
        return reply
    if "date" in user_input_lower:
        reply = f"Today's date is {datetime.now().strftime('%Y-%m-%d')}"
        store_message("assistant", reply)
        speak(reply)
        return reply
    if "news" in user_input_lower:
        top_news = retrieve_relevant_knowledge("news", top_k=5)
        reply = "\n\n".join(top_news) if top_news else "I haven't learned any news yet."
        store_message("assistant", reply)
        speak(reply)
        return reply

    try:
        context_knowledge = "\n".join(retrieve_relevant_knowledge(user_input, top_k=3))
        system_prompt = f"""
        You are an advanced, friendly, autonomous AI assistant.
        Use this knowledge to answer: {context_knowledge}
        Be human-like, informative, and conversational.
        User asked: {user_input}
        """
        reply = hf_response(system_prompt)
        store_message("assistant", reply)
        conversation_history.append({"role": "assistant", "content": reply})
        speak(reply)
        return reply
    except Exception as e:
        print("AI brain error:", e)
        return f"AI brain error: {e}"

# ------------------- FLASK WEB UI -------------------
HTML = """
<!DOCTYPE html>
<html>
<head>
<title>WebLearningAI</title>
<style>
body { font-family: Arial; background: #111; color: white; padding: 20px; }
#chat { height: 500px; overflow-y: auto; border: 1px solid #444; padding: 10px; }
input { width: 80%; padding: 10px; }
button { padding: 10px; margin-top:5px;}
</style>
</head>
<body>
<h2>WebLearningAI</h2>
<div id="chat"></div>
<br>
<input id="message" placeholder="Type your message..." autofocus />
<button onclick="sendMessage()">Send</button>
<button onclick="toggleVoice()" id="voiceBtn">Mute Voice</button>

<h3>Settings</h3>
<textarea id="settings" rows="10" style="width:100%;">{{ settings_json }}</textarea>
<button onclick="saveSettings()">Save Settings</button>

<script>
let voiceOn = true;

function sendMessage() {
    let message = document.getElementById("message").value.trim();
    if(!message) return;
    fetch("/chat", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({message: message})
    })
    .then(res => res.json())
    .then(data => {
        let chat = document.getElementById("chat");
        chat.innerHTML += "<p><b>You:</b> " + message + "</p>";
        chat.innerHTML += "<p><b>AI:</b> " + data.reply + "</p>";
        document.getElementById("message").value = "";
        chat.scrollTop = chat.scrollHeight;
    });
}

document.getElementById("message").addEventListener("keydown", function(e){
    if(e.key === "Enter") { sendMessage(); e.preventDefault(); }
});

function saveSettings(){
    let newSettings = document.getElementById("settings").value;
    fetch("/settings", {
        method:"POST",
        headers: {"Content-Type":"application/json"},
        body: JSON.stringify({settings: newSettings})
    }).then(()=>{ alert("Settings saved!"); });
}

function toggleVoice(){
    voiceOn = !voiceOn;
    fetch("/voice_toggle", {
        method: "POST",
        headers: {"Content-Type":"application/json"},
        body: JSON.stringify({enabled: voiceOn})
    }).then(()=> {
        document.getElementById("voiceBtn").innerText = voiceOn ? "Mute Voice" : "Unmute Voice";
    });
}
</script>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML, settings_json=json.dumps(SETTINGS, indent=4))

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message", "")
    reply = hybrid_response(user_input)
    return jsonify({"reply": reply})

@app.route("/settings", methods=["POST"])
def update_settings():
    new_settings = request.json.get("settings", "{}")
    try:
        parsed = json.loads(new_settings)
        global SETTINGS
        SETTINGS = parsed
        save_settings()
        return jsonify({"status":"ok"})
    except:
        return jsonify({"status":"error"})

@app.route("/voice_toggle", methods=["POST"])
def voice_toggle():
    global VOICE_ENABLED
    VOICE_ENABLED = request.json.get("enabled", True)
    return jsonify({"status":"ok", "voice_enabled": VOICE_ENABLED})

# ------------------- RUN -------------------
if __name__ == "__main__":
    # Local IP for LAN access
    app.run(host="192.168.1.226", port=5000)
