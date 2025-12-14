import os
from flask import Flask, render_template, request, jsonify
import google.generativeai as genai
import json
from dotenv import load_dotenv

# 1. Load Environment Variables
load_dotenv()
app = Flask(__name__)

# 2. Configure Gemini AI
api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    raise ValueError("No API key found! Please check your .env file.")

genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-2.5-flash')

# 3. Global Storage (Session-based)
tasks = []
bot_personality = "You are a helpful, friendly AI assistant."

def ai_process_command(user_text, current_tasks, current_personality):
    """
    Decides the action and generates content using Gemini.
    """
    # Create a summary of tasks to show the AI
    task_summary = [f"- {t['task']} (Done: {t['done']}, Note: {t['notes']})" for t in current_tasks]
    
    prompt = f"""
    SYSTEM INSTRUCTION: {current_personality}
    
    You are managing this Task List: {task_summary}
    User Input: "{user_text}"
    
    Analyze the input and return a JSON object:
    {{
        "action": "add" | "delete" | "complete" | "train" | "chat",
        "target_data": "Task Name OR New Personality String",
        "note_content": "A short, helpful summary or answer (if adding a note/task)",
        "response_text": "Your natural reply to the user"
    }}
    
    Rules:
    1. 'Train: You are a pirate' -> action: 'train', target_data: 'You are a pirate'.
    2. 'Add buy milk' -> action: 'add', target_data: 'Buy milk'.
    3. 'Save a note about Ed Sheeran' -> action: 'add', target_data: 'Research: Ed Sheeran', note_content: 'Ed Sheeran is a British singer known for hits like Shape of You...' (GENERATE THIS INFO).
    4. 'Mark milk as done' -> action: 'complete', target_data: 'milk' (fuzzy match).
    5. If just chatting, action: 'chat'.
    """
    
    try:
        response = model.generate_content(prompt)
        clean = response.text.replace("```json", "").replace("```", "").strip()
        return json.loads(clean)
    except Exception as e:
        print(f"AI Error: {e}")
        return {"action": "chat", "response_text": "I encountered an error processing that request."}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    global bot_personality
    user_msg = request.json.get('message', '')
    
    # Ask AI for decision
    decision = ai_process_command(user_msg, tasks, bot_personality)
    
    action = decision.get('action')
    data = decision.get('target_data')
    note = decision.get('note_content', '')
    bot_reply = decision.get('response_text')
    
    # Execute Action
    if action == 'add':
        tasks.append({'task': data, 'done': False, 'notes': note})
        
    elif action == 'train':
        bot_personality = data
        bot_reply = f"Training Updated: {data}"

    elif action == 'complete':
        for t in tasks:
            if data and data.lower() in t['task'].lower():
                t['done'] = True
                
    elif action == 'delete':
        for t in tasks:
            if data and data.lower() in t['task'].lower():
                tasks.remove(t)

    return jsonify({"reply": bot_reply, "tasks": tasks})

if __name__ == '__main__':
    app.run(debug=True)