from flask import Flask, jsonify
from flask import request
import json


app = Flask(__name__)

todos = [
    { "label": "Pasear al perro", "done": False },
    { "label": "Cenar", "done": False }
]


@app.route('/todos', methods=['GET'])
def hello_world():
    return jsonify(todos)

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.data
    decoded_object = json.loads(request_body)
    todos.append(decoded_object)
    print("Incoming request with the following body", request_body)
    return jsonify(todos)



if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)