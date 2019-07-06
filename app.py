
from flask import Flask

app = Flask(__name__)

@app.route('/')

def enter():
    return 'Welcome to the container training'

if __name__ == '__main__':
    app.run(host='0.0.0.0')
