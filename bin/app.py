#!/usr/bin/python
from flask import Flask, jsonify
from flask import request
from flask import abort
from flask.ext.cors import CORS
from flask import Flask, render_template, redirect, url_for, request, session, flash, g, abort
import os
from flask import Flask, render_template, redirect, url_for, request, session, flash, g, abort
import ConfigParser
#import remotelib

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})

CONFIG_FILE='settings.cfg'
settings  = ConfigParser.ConfigParser()
if not os.path.isfile(CONFIG_FILE):
    print "[FATAL] missing settings.cfg file."
    exit()

import collections

colors = collections.OrderedDict()
colors['#FFFFFE'] = ""
colors['#FFFFFF'] = ""
colors['#000000'] = ""
colors['#E33939'] = ""

colors['#24AD75'] = ""
colors['#2854C1'] = ""
colors['#F8FFFF'] = ""
colors['#FF7927'] = ""
colors['#7DE5AA'] = ""
colors['#2A91F0'] = ""
colors['#FDBCDA'] = ""
colors['#FF7E56'] = ""
colors['#7AD1E4'] = ""
colors['#484F79'] = ""
colors['#F0B5E3'] = ""
colors['#FEA049'] = ""
colors['#3BAFEA'] = ""
colors['#975A95'] = ""
colors['#B2F0FF'] = ""
colors['#F1E461'] = ""
colors['#1197D4'] = ""
colors['#CB7DD3'] = ""
colors['#A2DDEF'] = ""

settings.read(CONFIG_FILE)
port = settings.defaults()['port']
photocell_pin = settings.defaults()['photocell_pin']

POWER_ON='POWER_ON'
POWER_OFF='POWER_OFF'


#remote = remotelib(port,photocell_pin)

@app.route('/bar/api/v1.0/remote/<string:cmd_code>', methods=['GET'])
def send_remote_code(cmd_code):

    if photocell_pin:
        if cmd_code == POWER_ON:
            #remotelib.power_on()
            return gimmiedat()
        elif cmd_code == POWER_OFF:
            #remotelib.power_off()
            return gimmiedat()


    command = "irsend SEND_ONCE led " + cmd_code
    os.system(command)
    print "[SENT] " + command # Debug purposes
    return "{'cmd', '%s'}" % (cmd_code)
    return jsonify({'cmd', cmd_code})


@app.route('/index/<string:cmd_code>', methods=['GET'])
def gimmiedat(cmd_code):
    port = 8080
    return render_template("index.html", port=port)

@app.route('/ui', methods=['GET'])
def gimmiedat2():
    return render_template("remote.html")




if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=8080)
