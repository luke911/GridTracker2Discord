# QSO to Discord
A simple Dockerized solution to post QSO data from GridTracker to Discord using a webhook.

## Features
- Monitors GridTracker's UDP broadcasts or log files.
- Posts QSO details (e.g., call sign, grid, time, frequency) to a Discord channel.

## Setup Instructions
1. Clone the repository:
   ```
   git clone https://github.com/yourusername/qso-to-discord.git
   ```
2. Build the Docker container:
   ```
   docker build -t qso-to-discord .
   ```
3. Run the container:
   ```
   docker run -d --name qso-to-discord      -e DISCORD_WEBHOOK_URL="your_discord_webhook_url"      qso-to-discord
   ```

## Requirements
- Docker
- GridTracker configured to send UDP broadcasts or write log files.
