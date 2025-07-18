from flask import Flask, request, jsonify
from datetime import datetime
import socket

app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "ip": request.remote_addr
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
