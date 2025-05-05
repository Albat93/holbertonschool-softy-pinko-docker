from flask import Flask
from flask_cors import CORS
import socket

app = Flask(__name__)
CORS(app)

@app.route('/api/hello')
def hello():
    return f"Hello from {socket.gethostname()}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5252)
