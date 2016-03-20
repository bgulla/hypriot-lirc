#!/usr/bin/python
from flask import Flask, jsonify
from flask import request
from flask import abort
import os

app = Flask(__name__)

@app.route('/bar/api/v1.0/remote/<string:cmd_code>', methods=['GET'])
def send_remote_code(cmd_code):
    command = "irsend SEND_ONCE led " + cmd_code
    os.system(command)
    print "[SENT] " + command # Debug purposes
    return "{'cmd', '%s'}" % (cmd_code)
    return jsonify({'cmd', cmd_code})


#@app.route('/todo/api/v1.0/tasks', methods=['GET'])
#def get_tasks():
#    return jsonify({'tasks': tasks})

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=8080)
