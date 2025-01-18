
from flask import Flask, request, jsonify, render_template
import os
import logging
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

@app.route("/")
def index():
    return render_template("index.html", webhook=os.getenv("DISCORD_WEBHOOK_URL", ""), port=os.getenv("UDP_PORT", "2237"))

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

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
