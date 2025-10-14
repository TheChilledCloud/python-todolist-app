# app.py
from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory storage
todos = []
todo_id = 1

@app.route('/', methods=['GET'])
def home():
    return jsonify({"message": "Todo API is running!"}), 200

@app.route('/todos', methods=['GET'])
def get_todos():
    return jsonify(todos), 200

@app.route('/todos', methods=['POST'])
def add_todo():
    global todo_id
    data = request.get_json()
    new_todo = {
        "id": todo_id,
        "task": data.get("task"),
        "done": False
    }
    todos.append(new_todo)
    todo_id += 1
    return jsonify(new_todo), 201

@app.route('/todos/<int:id>', methods=['DELETE'])
def delete_todo(id):
    global todos
    todos = [t for t in todos if t['id'] != id]
    return jsonify({"message": "Todo deleted"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
