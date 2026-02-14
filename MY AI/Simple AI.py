import json
import random
import os

MEMORY_FILE = "memory.json"

# Load memory from file
def load_memory():
    if os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, "r") as file:
            return json.load(file)
    return {}

# Save memory to file
def save_memory(memory):
    with open(MEMORY_FILE, "w") as file:
        json.dump(memory, file, indent=4)

# Get response from memory
def get_response(user_input, memory):
    user_input = user_input.lower()
    if user_input in memory:
        return random.choice(memory[user_input])
    return None

# Main chat function
def chat():
    memory = load_memory()
    print("LearningAI: Hello! I can learn new things.")
    print("Type 'bye' to exit.\n")

    while True:
        user_input = input("You: ").lower()

        if user_input == "bye":
            print("LearningAI: Goodbye!")
            break

        response = get_response(user_input, memory)

        if response:
            print("LearningAI:", response)
        else:
            print("LearningAI: I don't know how to respond to that.")
            new_response = input("Teach me what I should say: ")

            if user_input not in memory:
                memory[user_input] = []

            memory[user_input].append(new_response)
            save_memory(memory)

            print("LearningAI: Got it! I'll remember that.")

if __name__ == "__main__":
    chat()