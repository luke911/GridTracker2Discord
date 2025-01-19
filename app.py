
from flask import Flask, request, jsonify, render_template
from flask_socketio import SocketIO, emit
import os
import logging
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)
app.config["SECRET_KEY"] = "secret!"

# Initialize SocketIO for real-time updates
socketio = SocketIO(app)

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Store the last 10 contacts in memory
last_10_contacts = []

@app.route("/")
def index():
    return render_template("index.html", webhook=os.getenv("DISCORD_WEBHOOK_URL", ""), port=os.getenv("UDP_PORT", "2237"), contacts=last_10_contacts)

@app.route("/update", methods=["POST"])
def update_config():
    try:
        data = request.json
        webhook = data.get("webhook", "").strip()
        port = data.get("port", "2237").strip()

        # Save to .env file
        with open(".env", "w") as f:
            f.write(f"DISCORD_WEBHOOK_URL={webhook}\n")
            f.write(f"UDP_PORT={port}\n")

        return jsonify({"status": "success", "message": "Configuration updated. Restart the container for changes to take effect."}), 200
    except Exception as e:
        logging.error(f"Error updating configuration: {e}")
        return jsonify({"status": "error", "message": "Failed to update configuration."}), 500

# API endpoint to simulate adding a contact (for testing purposes)
@app.route("/add_contact", methods=["POST"])
def add_contact():
    data = request.json
    contact = {
        "call_sign": data.get("call_sign", "Unknown"),
        "grid": data.get("grid", "Unknown"),
        "time": data.get("time", "Unknown"),
        "frequency": data.get("frequency", "Unknown"),
    }
    add_contact_to_log(contact)
    return jsonify({"status": "success", "contact": contact}), 200

def add_contact_to_log(contact):
    # Add a contact to the in-memory log and emit it to the WebSocket.
    if len(last_10_contacts) >= 10:
        last_10_contacts.pop(0)  # Remove the oldest contact
    last_10_contacts.append(contact)
    socketio.emit("new_contact", contact)

if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0", port=5000)
