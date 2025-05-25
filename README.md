# Smart WiFi Door Lock Using ESP32-CAM & Telegram

This project implements a smart door lock system using ESP32-CAM and Telegram integration. The system allows you to control your door lock remotely through Telegram commands and provides real-time photo capture capabilities.

## Features

- Remote door lock/unlock control via Telegram
- Real-time photo capture using ESP32-CAM
- Secure authentication through Telegram chat ID
- Physical button control for local access
- LED flash control for better photo capture in low light
- WiFi connectivity for remote access

## Hardware Requirements

- ESP32-CAM module
- Relay module for door lock control
- Push button for local control
- LED flash (optional)
- Power supply
- Jumper wires

## Software Requirements

- Arduino IDE
- Required Libraries:
  - WiFi.h
  - WiFiClientSecure.h
  - UniversalTelegramBot.h
  - ArduinoJson.h
  - esp_camera.h

## Setup Instructions

1. **Hardware Setup**
   - Connect the relay module to GPIO 12 (LOCK)
   - Connect the push button to GPIO 13 (BUTTON)
   - Connect the LED flash to GPIO 4 (FLASH_LED)
   - Connect the ESP32-CAM camera pins as defined in the code

2. **Software Setup**
   - Install the required libraries in Arduino IDE
   - Update the following in the code:
     - WiFi credentials (SSID and password)
     - Telegram Bot Token (obtained from BotFather)
     - Your Telegram Chat ID (obtained from @myidbot)

3. **Telegram Bot Setup**
   - Create a new bot using BotFather on Telegram
   - Get your bot token and chat ID
   - Start the bot by sending /start command

## Usage

The system supports the following Telegram commands:

- `/start` - Displays welcome message and available commands
- `/photo` - Captures and sends a photo from the ESP32-CAM
- `/unlock` - Unlocks the door
- `/lock` - Locks the door

## Security Features

- Authentication through Telegram chat ID
- Secure HTTPS communication
- Brown-out protection enabled
- Unauthorized user access prevention

## Project Structure

- `code.ino` - Main Arduino sketch
- `server.py` - Python server for additional functionality
- `uploads/` - Directory for storing captured images
- `ArduinoJson-7.x.zip` - Required library for JSON handling

## Troubleshooting

1. If the camera fails to initialize:
   - Check the camera connections
   - Verify the GPIO pin configurations
   - Ensure proper power supply

2. If Telegram commands are not working:
   - Verify your bot token and chat ID
   - Check WiFi connectivity
   - Ensure the bot is started with /start command

## Contributing

Feel free to submit issues and enhancement requests!

## License

This project is open source and available under the MIT License. 