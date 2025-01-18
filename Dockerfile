# Use a lightweight Python base image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy the Python script
COPY qso_to_discord.py .

# Install required dependencies
RUN pip install requests

# Set environment variables (can be overridden at runtime)
ENV UDP_IP=0.0.0.0
ENV UDP_PORT=2237
ENV DISCORD_WEBHOOK_URL="https://discord.com/api/webhooks/your_webhook_id"

# Run the script
CMD ["python", "qso_to_discord.py"]
