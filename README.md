
# QSO to Discord

A Dockerized application for posting QSO data (e.g., call sign, grid, frequency) from GridTracker to a Discord channel using webhooks.

## Features

- Monitors GridTracker's UDP broadcasts.
- Posts QSO details to Discord.
- Easy setup with Docker Compose and `.env` support.
- Logs for debugging and monitoring.

## Quick Start

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/qso-to-discord.git
cd qso-to-discord
```

### 2. Configure the Application

Copy the `.env.example` file and edit it with your settings:

```bash
cp .env.example .env
nano .env
```

### 3. Run the Application

Use Docker Compose to build and start the container:

```bash
docker-compose up -d
```

### 4. Check Logs

```bash
docker logs qso-to-discord
```

## Contributing

Contributions are welcome! Please submit issues and pull requests via GitHub.

## License

MIT
