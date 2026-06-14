# Personal AI Assistant with Memory using Gemini API

## Overview

Personal AI Assistant is a Python-based chatbot powered by Google's Gemini API. The assistant can answer user questions, remember user information, store tasks, and support multi-step conversations using persistent memory.

## Features

* AI-powered chatbot using Gemini API
* Memory storage using JSON
* Remembers user names
* Stores and retrieves tasks
* Multi-step conversations
* Context-aware responses
* Simple command-line interface

## Technologies Used

* Python
* Google Gemini API
* JSON
* Google Generative AI SDK

## Project Structure

```
AI Project/
│
├── app.py
├── memory.json
├── requirements.txt
└── README.md
```

## How It Works

1. User enters a message.
2. The assistant checks stored memory.
3. User information and tasks are saved in a JSON file.
4. Previous memory is included in the conversation context.
5. Gemini API generates intelligent responses.
6. The assistant continues the conversation while retaining memory.

## Installation

### Clone the Repository

```bash
git clone https://github.com/sakshilimse1122/Personal-AI-Assistant-With-Memory.git
cd Personal-AI-Assistant-With-Memory
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Add Gemini API Key

Replace:

```python
API_KEY = "YOUR_API_KEY"
```

with your Gemini API key.

### Run the Application

```bash
python app.py
```

## Example Commands

### Save User Name

```
My name is Sakshi
```

### Recall User Name

```
What is my name?
```

### Save Task

```
Remember task Complete AI Internship Project
```

### Retrieve Task

```
Show task
```

### Ask Questions

```
What is Artificial Intelligence?
```

## Sample Output

```
You: My name is Sakshi
AI: Nice to meet you, Sakshi!

You: What is my name?
AI: Your name is Sakshi

You: Remember task Complete AI Internship Project
AI: Task saved successfully!

You: Show task
AI: Complete AI Internship Project
```

## Future Enhancements

* Web Interface using Streamlit
* Voice Assistant Integration
* Database Storage
* Task Reminder System
* User Authentication

## Author

Sakshi Limse

AI Internship Project
