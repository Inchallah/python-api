from flask import Flask
import socket
import os
import json

app = Flask(__name__)


@app.route('/prout/<name>')
def gepete(name):
    return 'hey '+name+' par ton host ' + socket.gethostname()


@app.route('/state')
def status():
    return "Message: " + os.environ.get('MESSAGE') + " | Name: " + os.environ.get('NAME') + " | Sender: " + os.environ.get('SENDER')


@app.route('/file')
def readFromFile():
    # read from config
    with open('config.json', 'r') as config:
        configData = json.loads(config)
        configStr = "Hello sender: " + configData['sender'] + \
            ", sent this message to you " + configData['message']
    with open('secrets.json', 'r') as secrets:
        secretsData = json.loads(secrets)
        secretStr = "Hello sender: " + secretsData['sender'] + \
            ", sent this message to you " + secretsData['message']
    simpleResponse = configStr + '<br>' + secretStr
    # read from secret
    return simpleResponse


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='127.0.0.1', port=port)
