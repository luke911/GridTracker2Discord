
import socket
import json
import requests
import os
import logging
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Environment variables
discord_webhook_url = os.getenv("DISCORD_WEBHOOK_URL")
udp_ip = os.getenv("UDP_IP", "0.0.0.0")
udp_port = int(os.getenv("UDP_PORT", 2237))

if not discord_webhook_url:
    logging.error("DISCORD_WEBHOOK_URL is not set in the environment variables or .env file.")
    exit(1)

def post_to_discord(call_sign, grid, time, freq):
    """Send a QSO message to Discord."""
    message = f"📡 New QSO!\n**Call Sign:** {call_sign}\n**Grid:** {grid}\n**Time:** {time}\n**Frequency:** {freq}"
    response = requests.post(discord_webhook_url, json={"content": message})
    if response.status_code == 204:
        logging.info(f"Posted QSO to Discord: {call_sign}")
    else:
        logging.error(f"Failed to post to Discord: {response.status_code}, {response.text}")

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((udp_ip, udp_port))

logging.info(f"Listening for UDP data on {udp_ip}:{udp_port}...")

while True:
    data, addr = sock.recvfrom(1024)  # Buffer size
    try:
        qso = json.loads(data.decode())
        call_sign = qso.get("call", "Unknown")
        grid = qso.get("gridsquare", "Unknown")
        time = qso.get("time", "Unknown")
        freq = qso.get("freq", "Unknown")
        post_to_discord(call_sign, grid, time, freq)
    except Exception as e:
        logging.error(f"Error processing UDP data: {e}")
