import pyautogui
import requests
import os
import glob
from datetime import datetime
import time

# Replace with your bot token and chat ID
BOT_TOKEN = "*********************"
CHAT_ID = "***********************"
##SCREENSHOT_FOLDER = "screenshots"  # Folder where screenshots are saved
SCREENSHOT_FOLDER = os.path.join(os.path.expanduser("~"), "Desktop", "KnexusAutomation", "screenshots")

# Ensure the folder exists
os.makedirs(SCREENSHOT_FOLDER, exist_ok=True)

def capture_screenshot():
    """Capture a screenshot with a timestamped filename."""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    screenshot_path = os.path.join(SCREENSHOT_FOLDER, f"rpa_screenshot_{timestamp}.png")
    screenshot = pyautogui.screenshot()
    screenshot.save(screenshot_path)
    return screenshot_path  # Return the filename to use later

def get_latest_screenshot():
    """Find the most recent screenshot in the folder."""
    list_of_files = glob.glob(os.path.join(SCREENSHOT_FOLDER, "rpa_screenshot_*.png"))
    if not list_of_files:
        return None  # No files found
    latest_file = max(list_of_files, key=os.path.getctime)  # Get the newest file
    return latest_file

def send_screenshot():
    """Send the latest screenshot via Telegram."""
    latest_screenshot = get_latest_screenshot()
    if not latest_screenshot:
        print("No screenshot found to send.")
        return
    
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendPhoto"
    with open(latest_screenshot, "rb") as photo:
        files = {"photo": photo}
        data = {"chat_id": CHAT_ID, "caption": "Here is the latest screenshot."}
        response = requests.post(url, data=data, files=files)
        print(f"Sent {latest_screenshot}: {response.json()}")

# Capture and send the latest screenshot
time.sleep(10)
screenshot_file = capture_screenshot()  # Capture the screenshot
send_screenshot()  # Send the latest one
