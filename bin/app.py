#!/usr/bin/python
from flask import Flask, jsonify
from flask_cors import CORS
import os
from flask import Flask, render_template, redirect, url_for, request, session, flash, g, abort

POWER_ON='POWER_ON'
POWER_OFF='POWER_OFF'

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})

@app.route('/api/<string:cmd_code>', methods=['GET'])
def send_remote_code(cmd_code):
    """

    :param cmd_code:
    :return:
    """
    if cmd_code == POWER_ON:
        #remotelib.power_on()
        return gimmiedat()
    elif cmd_code == POWER_OFF:
        #remotelib.power_off()
        return gimmiedat()
    command = "irsend SEND_ONCE led " + cmd_code
    os.system(command)
    print "[SENT] " + command # Debug purposes
    return cmd_code


@app.route('/index/<string:cmd_code>', methods=['GET'])
def gimmiedat(cmd_code):
    port = 8080
    return render_template("index.html", port=port)

@app.route('/', methods=['GET','POST'])
def home():
    if request.method == 'POST':
        if request.form['cmd_code']:
            path ="/api/" +str(request.form['cmd_code'])
            redirect(path)


    return render_template("index.html")


"""
@app.route('/', methods=['GET', 'POST']) #this is called a decorator
def home():
    cow = cowsay.cowsay("moo")
    if request.method == 'POST':
        if request.form['text']:
            moo_text = request.form['text']
            cow = cowsay.cowsay(moo_text)
            app.logger.info('[Moo] '+ unicode(now.replace(microsecond=0)) + "\t" + request.remote_addr + "\t" + moo_text)
    return render_template("index.html", cow=cow)
    """



if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=8080)
