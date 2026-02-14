import sys
import json
import random
from datetime import datetime
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QTextEdit, QPushButton, QLabel
from PyQt5.QtWebEngineWidgets import QWebEngineView
import requests

MEMORY_FILE = "web_memory.json"

# ----------------- Memory -----------------
def load_memory():
    try:
        with open(MEMORY_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        return {}

def save_memory(memory):
    with open(MEMORY_FILE, "w", encoding="utf-8") as f:
        json.dump(memory, f, indent=4, ensure_ascii=False)

# ----------------- AI Response -----------------
def get_response(user_input, memory):
    user_input_lower = user_input.lower()

    # Time/Date
    if any(keyword in user_input_lower for keyword in ["time", "what time", "current time"]):
        return f"The current time is {datetime.now().strftime('%H:%M:%S')}"
    if any(keyword in user_input_lower for keyword in ["date", "today"]):
        return f"Today's date is {datetime.now().strftime('%Y-%m-%d')}"

    # Jokes
    if "joke" in user_input_lower:
        jokes = [
            "Why did the computer go to the doctor? It caught a virus!",
            "Why was the math book sad? It had too many problems.",
            "Why don’t scientists trust atoms? Because they make up everything!"
        ]
        return random.choice(jokes)

    # Wikipedia
    if "who is" in user_input_lower or "what is" in user_input_lower:
        query = user_input_lower.replace("who is", "").replace("what is", "").strip()
        try:
            url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{query.replace(' ', '_')}"
            r = requests.get(url, timeout=5)
            data = r.json()
            if "extract" in data:
                return data["extract"]
        except:
            return "I couldn't fetch a Wikipedia summary."

    # Memory
    if user_input_lower in memory:
        return random.choice(memory[user_input_lower])

    # Fallback: return URL to open
    return f"OPEN_BROWSER:{user_input}"

# ----------------- AI Browser GUI -----------------
class AIBrowser(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("WebLearningAI Browser")
        self.setGeometry(100, 100, 1000, 700)

        self.memory = load_memory()

        layout = QVBoxLayout()

        self.chat_display = QTextEdit()
        self.chat_display.setReadOnly(True)
        layout.addWidget(self.chat_display)

        self.input_line = QLineEdit()
        self.input_line.setPlaceholderText("Type your message here...")
        layout.addWidget(self.input_line)

        self.send_button = QPushButton("Send")
        self.send_button.clicked.connect(self.handle_input)
        layout.addWidget(self.send_button)

        self.browser = QWebEngineView()
        layout.addWidget(self.browser)

        self.setLayout(layout)

    def handle_input(self):
        user_text = self.input_line.text()
        if not user_text.strip():
            return
        self.chat_display.append(f"You: {user_text}")

        response = get_response(user_text, self.memory)
        if response.startswith("OPEN_BROWSER:"):
            query = response.replace("OPEN_BROWSER:", "")
            url = f"https://www.google.com/search?q={query}"
            self.browser.load(url)
            self.chat_display.append("WebLearningAI: Opened browser results.")
        else:
            self.chat_display.append(f"WebLearningAI: {response}")

        # Ask to remember
        teach = "no"
        if user_text.lower() not in self.memory:
            teach = "yes"  # auto-learn for demo; you can make a GUI prompt if you want
        if teach == "yes":
            self.memory.setdefault(user_text.lower(), []).append(response)
            save_memory(self.memory)

        self.input_line.clear()

# ----------------- Run -----------------
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ai_browser = AIBrowser()
    ai_browser.show()
    sys.exit(app.exec_())
