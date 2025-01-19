
# GridTracker2Discord

GridTracker2Discord is a web-based dashboard that integrates with GridTracker to monitor and share QSO (contact) information via Discord using webhooks.

## Features

- Real-time monitoring of QSOs.
- Logs the last 10 contacts in a user-friendly grid layout.
- Displays QSO activity by band with an interactive chart.
- Plots QSOs on a world map using Leaflet.js.
- Allows configuration of Discord webhook and UDP port through the web interface.

## Technologies Used

- **Flask**: Backend server.
- **Flask-SocketIO**: Real-time updates using WebSockets.
- **Bootstrap**: Responsive styling.
- **Chart.js**: Interactive charts.
- **Leaflet.js**: QSO mapping.

## Installation

### Prerequisites

- Docker
- Docker Compose

### Steps

1. Clone the repository or download the ZIP file.
   ```bash
   git clone https://github.com/yourusername/GridTracker2Discord.git
   cd GridTracker2Discord
   ```

2. Update the `.env` file with your configuration:
   ```bash
   cp .env.example .env
   nano .env
   ```

   - Replace `your_discord_webhook_url` with your actual Discord webhook URL.
   - Update the UDP port if needed.

3. Build and run the Docker container:
   ```bash
   docker-compose up -d
   ```

4. Access the web interface:
   ```
   http://<your-server-ip>:5000
   ```

## Usage

- **Dashboard**: Monitor real-time QSOs, view stats, and explore a map of QSO locations.
- **Configuration**: Update Discord webhook or UDP port via the configuration form.
- **Logs**: Check the last 10 logged QSOs.

## Contributing

Contributions are welcome! Feel free to submit issues or pull requests.

## License

This project is licensed under the MIT License.

---
Made with 💙 for amateur radio enthusiasts.
