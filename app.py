
from flask import Flask, request, jsonify, render_template
from flask_socketio import SocketIO
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
socketio = SocketIO(app)

last_10_contacts = []

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/update", methods=["POST"])
def update_config():
    data = request.json
    webhook = data.get("webhook", "")
    port = data.get("port", "2237")
    with open(".env", "w") as f:
        f.write(f"DISCORD_WEBHOOK_URL={webhook}\nUDP_PORT={port}\n")
    return jsonify({"message": "Configuration updated successfully!"})

@socketio.on("new_contact")
def handle_new_contact(contact):
    if len(last_10_contacts) >= 10:
        last_10_contacts.pop(0)
    last_10_contacts.append(contact)
    socketio.emit("new_contact", contact)

if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0", port=5000)
