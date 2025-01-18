
#!/bin/bash

echo "Setting up QSO to Discord..."

# Prompt for webhook URL
read -p "Enter your Discord webhook URL: " DISCORD_WEBHOOK_URL

# Create .env file
cat <<EOF > .env
DISCORD_WEBHOOK_URL=$DISCORD_WEBHOOK_URL
UDP_PORT=2237
EOF

echo ".env file created. Starting the application with Docker Compose..."

# Run Docker Compose
docker-compose up -d
