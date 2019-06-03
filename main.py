import hmac
import json

from flask import Flask, request ,jsonify,abort

app = Flask(__name__)

@app.route('/', methods=['POST'])
def receive():
    
    getheaders = request.headers['X-Self-ID']
    post_type = request.json
    print (getheaders)
    
    print (json.loads(post_type))
    return 'OK.'

@app.route("/about")
def hello():
    return "<h1 style='color:blue'>Hello World! It's Mewtea API </h1>"



tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol',
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web',
        'done': False
    }
]

@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = filter(lambda t: t['id'] == task_id, tasks)
    if len(task) == 0:
        abort(404)
    return jsonify({'task': task[0]})

if __name__ == '__main__':
    app.run()

