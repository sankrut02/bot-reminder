# WhatsApp Trip Countdown Bot 🚀

A Python automation bot that updates WhatsApp group names with countdown timers and sends daily reminders for upcoming trips.

## 📋 Features

- **Automated Group Name Updates**: Changes WhatsApp group name to show days remaining until trip
- **Daily Reminders**: Sends countdown messages to the group at specified times
- **Persistent Browser Session**: Uses Chrome user data directory to maintain login state
- **Customizable Trip Details**: Easy configuration for trip date, group name, and message timing

## 🛠️ Prerequisites

Before running this bot, ensure you have:

- Python 3.7 or higher
- Google Chrome browser installed
- ChromeDriver compatible with your Chrome version
- WhatsApp Web account

## 📦 Dependencies

Install the required Python packages:

```bash
pip install selenium
```

## ⚙️ Setup

1. **Clone the repository**:
   ```bash
   git clone <your-repo-url>
   cd bot
   ```

2. **Download ChromeDriver**:
   - Download ChromeDriver from [official site](https://chromedriver.chromium.org/)
   - Place the `chromedriver` executable in the project directory
   - Ensure it's executable: `chmod +x chromedriver` (macOS/Linux)

3. **Configure the bot**:
   Edit the configuration variables in `imp.py`:
   ```python
   trip_date = datetime(2025, 10, 17)   # Your trip date
   group_name = '"Friends"'             # WhatsApp group name (with quotes)
   update_time = "00:01"               # Daily update time (24-hour format)
   ```

4. **First-time WhatsApp Web login**:
   - Run the bot for the first time
   - Scan the QR code in WhatsApp Web to log in
   - The session will be saved in the `chrome-data` directory

## 🚀 Usage

### Main Bot (`imp.py`)
The primary bot file that runs the countdown automation:

```bash
python imp.py
```

### Testing/Development (`ha.py`)
A utility script to check trip calculations:

```bash
python ha.py
```

## 📁 File Structure

```
bot/
├── imp.py              # Main bot script
├── ha.py              # Trip date calculator/tester
├── chromedriver       # Chrome WebDriver executable
├── chrome-data/       # Chrome user data (auto-generated)
├── README.md          # This file
└── .git/             # Git repository
```

## 🔧 Configuration Options

### Trip Configuration
```python
trip_date = datetime(2025, 10, 17)    # Set your trip date
group_name = '"Friends"'               # Target WhatsApp group (include quotes)
update_time = "00:01"                 # When to send daily updates (HH:MM)
```

### Message Customization
The bot updates:
- **Group name**: `"Friends - X Days Left!!"`
- **Daily message**: `"Helloo Bastards! X more days to gooooo!!"`

Edit these in the `update_group()` function to customize your messages.

## ⚠️ Important Notes

### Security & Privacy
- **Chrome Data**: The bot stores browser session data in `chrome-data/` directory
- **WhatsApp Session**: Your WhatsApp Web login is persisted between runs
- **Add to .gitignore**: Consider adding `chrome-data/` to `.gitignore` for privacy

### Limitations
- **UI Dependencies**: Uses XPath selectors that may break if WhatsApp updates their interface
- **Manual QR Login**: Requires initial QR code scan for WhatsApp Web
- **Single Group**: Currently configured for one group at a time
- **Continuous Running**: Must run continuously to send daily updates

### Troubleshooting
- **ChromeDriver Version**: Ensure ChromeDriver matches your Chrome browser version
- **XPath Errors**: WhatsApp UI changes may break element selectors
- **Session Expired**: Delete `chrome-data/` and re-login if session issues occur

## 🔄 How It Works

1. **Browser Automation**: Uses Selenium WebDriver to control Chrome browser
2. **WhatsApp Web**: Navigates to WhatsApp Web and interacts with the interface
3. **Group Management**: Finds target group, clicks group info, and updates name
4. **Message Sending**: Sends countdown message to the group
5. **Scheduling**: Continuously checks time and runs updates at specified interval

## 🤝 Contributing

Feel free to fork this project and submit pull requests for improvements:

- Better error handling
- Support for multiple groups
- More robust XPath selectors
- Configuration file support
- GUI interface

## 📜 License

This project is for educational purposes. Please use responsibly and in accordance with WhatsApp's Terms of Service.

## ⚡ Quick Start

1. Install dependencies: `pip install selenium`
2. Download ChromeDriver and place in project directory
3. Configure your trip date and group name in `imp.py`
4. Run: `python imp.py`
5. Scan QR code when prompted
6. Let the bot handle your countdown! 🎉

---

**Note**: This bot automates WhatsApp Web interactions. Use responsibly and ensure you have permission to modify group names and send messages to your groups.