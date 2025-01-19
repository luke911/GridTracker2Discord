
# Use a lightweight Python base image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy the application files
COPY app.py .
COPY templates ./templates
COPY requirements.txt .

# Upgrade pip to the latest version
RUN pip install --upgrade pip

# Install dependencies
RUN pip install -r requirements.txt

# Set environment variables (can be overridden)
ENV UDP_IP=0.0.0.0
ENV UDP_PORT=2237
ENV DISCORD_WEBHOOK_URL=

# Expose the Flask port
EXPOSE 5000

# Run the Flask app with Gunicorn and eventlet
CMD ["gunicorn", "-k", "eventlet", "-w", "1", "-b", "0.0.0.0:5000", "app:app"]
