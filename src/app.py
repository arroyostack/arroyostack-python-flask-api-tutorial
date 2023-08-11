from flask import Flask, jsonify
app = Flask(__name__)
from flask import request


todos = [
    { "label": "My first task", "done": False },
    { "label": "My second task", "done": False }
]





@app.route('/todos', methods=['GET'])
def hello_world():
    json_text = jsonify(todos)

  

    return json_text

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.data.json
    todos.append(json_text)
    print("Incoming request with the following body", request_body)
    return 'Response for the POST todo'





# These two lines should always be at the end of your app.py file.
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)