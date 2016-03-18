#!/usr/bin/python
from flask import Flask, jsonify
from flask import request
from flask import abort
import os

app = Flask(__name__)
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
    },
    {
        'id': 3,
        'title': u'Remote Code Sent!',
        'description': u'Need to find a good Python tutorial on the web', 
        'done': False
    }
]

def toggle_power():
    command = "irsend SEND_ONCE led KEY_POWER"
    os.system(command)

def send_remote_code(cmd_code):
    command = "irsend SEND_ONE led " + cmd_code
    os.system(command)
    print "[SENT] " + command

def write_file(cmd):
    bash = "echo '%s' >> /tmp/remote.log" % cmd
    os.system(bash)

@app.route('/todo/api/v1.0/tasks/<string:task_id>', methods=['GET'])
def get_task(task_id):
    print "[heard] " + task_id 
    write_file(task_id)
    return
    toggle_power()
    task = [task for task in tasks if task['id'] == task_id]
    return jsonify({'task': task[1]})
    if len(task) == 0:
        abort(404)
    return jsonify({'task': task[0]})

@app.route('/todo/api/v1.0/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=8080)
