from flask import Flask, render_template
from threading import Thread

app = Flask(__name__)  # Fixed typo: _name -> __name__

@app.route('/')
def index():
    return "Alive"  # Fixed indentation

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()
