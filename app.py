from flask import Flask
import socket
import os

app = Flask(__name__)


@app.route('/prout/<name>')
def gepete(name):
    return 'hey '+name+' par ton host ' + socket.gethostname()


@app.route('/state')
def status():
    return "Message: " + os.environ.get('MESSAGE') + " | Name: " + os.environ.get('NAME') + " | Sender: " + os.environ.get('SENDER')


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='127.0.0.1', port=port)
