import cv2
import numpy as np
import pyautogui
import os
from datetime import datetime, timedelta
import threading
from iLab_automation_log import LoggerConfig

class ScreenRecorder:
    def __init__(self, fps=20, retention_days=7):
        """Initialize the screen recorder."""
        self.folder = os.path.join(os.path.expanduser("~"), "Desktop", "KnexusAutomation", "rpa-vids")
        self.fps = fps
        self.out = None
        self.screen_size = pyautogui.size()
        self.recording_thread = None
        self.stop_flag = [False]  # Mutable container to signal stopping
        self.retention_days = retention_days  # Retention period in days
        self.logger = LoggerConfig.setup_logger()

        # Ensure the folder exists
        self.ensure_folder_exists()

    def ensure_folder_exists(self):
        """Ensure the specified folder exists."""
        if not os.path.exists(self.folder):
            os.makedirs(self.folder)
            print(f"Folder '{self.folder}' created.")
        else:
            print(f"Folder '{self.folder}' already exists.")

    def get_unique_filename(self):
        """Generate a unique filename in the specified folder based on the current date and time."""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        return os.path.join(self.folder, f"automation_record_{timestamp}.avi")

    def start(self):
        """Start the screen recording."""
        output_path = self.get_unique_filename()
        fourcc = cv2.VideoWriter_fourcc(*"XVID")
        self.out = cv2.VideoWriter(output_path, fourcc, self.fps, self.screen_size)
        self.logger.info(f"Screen recording started. Saving to {output_path}")

        # Start recording in a separate thread
        self.recording_thread = threading.Thread(target=self.record_screen)
        self.recording_thread.start()

    def record_screen(self):
        """Continuously record the screen until stop is signaled."""
        while not self.stop_flag[0]:
            img = pyautogui.screenshot()
            frame = np.array(img)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            self.out.write(frame)

    def stop(self):
        """Stop the screen recording."""
        self.stop_flag[0] = True
        if self.recording_thread:
            self.recording_thread.join()
        if self.out:
            self.out.release()
        self.logger.info(f"Screen recording stopped and saved.")

    def cleanup_old_files(self):
        """Delete video files older than the retention period based on the date in their filenames."""
        now = datetime.now()
        retention_threshold = now - timedelta(days=self.retention_days)

        for file in os.listdir(self.folder):
            file_path = os.path.join(self.folder, file)
            if os.path.isfile(file_path):
                try:
                    # Extract timestamp from filename (e.g., automation_record_20250101_103000.avi)
                    timestamp_str = file.split("_")[2] + file.split("_")[3].split(".")[0]
                    file_date = datetime.strptime(timestamp_str, "%Y%m%d%H%M%S")

                    # Check if the file is older than the retention threshold
                    if file_date < retention_threshold:
                        os.remove(file_path)
                        print(f"Deleted old file: {file_path}")
                except (IndexError, ValueError):
                    print(f"Skipping file with invalid format: {file}")
