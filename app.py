import google.generativeai as genai
import json

# Gemini API Key
API_KEY = "YOUR_API_KEY"

genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash")

MEMORY_FILE = "memory.json"


def load_memory():
    try:
        with open(MEMORY_FILE, "r") as file:
            return json.load(file)
    except:
        return {}


def save_memory(memory):
    with open(MEMORY_FILE, "w") as file:
        json.dump(memory, file)


memory = load_memory()

print("🤖 Personal AI Assistant Started!")
print("Type 'exit' to quit.\n")

while True:

    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Goodbye!")
        break

    # Remember Name
    if "my name is" in user_input.lower():

        name = user_input.split("is")[-1].strip()

        memory["name"] = name

        save_memory(memory)

        print(f"AI: Nice to meet you, {name}!")

        continue

    # Recall Name
    if "what is my name" in user_input.lower():

        if "name" in memory:
            print(f"AI: Your name is {memory['name']}")
        else:
            print("AI: I don't know your name yet.")

        continue

    # Save Task
    if "remember task" in user_input.lower():

        task = user_input.replace("remember task", "").strip()

        memory["task"] = task

        save_memory(memory)

        print("AI: Task saved successfully!")

        continue

    # Show Task
    if "show task" in user_input.lower():

        print("AI:", memory.get("task", "No task found."))

        continue

    # Gemini Context
    context = f"""
    User Name: {memory.get('name', 'Unknown')}
    Current Task: {memory.get('task', 'None')}

    User Question:
    {user_input}
    """

    response = model.generate_content(context)

    print("\nAI:", response.text)
    print()