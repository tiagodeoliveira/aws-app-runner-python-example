from datetime import datetime
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return f'Hello from AWS AppRunner - 03 - {datetime.now()}'
