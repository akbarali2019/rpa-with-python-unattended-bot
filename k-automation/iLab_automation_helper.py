import tkinter as tk
from tkinter import messagebox
import os

class Helper:
        
        # More generic validation function to handle different data types
        @staticmethod
        def safe_value(val, default=""):
            if val is None:
                return default
            if isinstance(val, (float, int)):  # Handle numbers as-is
                return str(val)  # Convert to string if required
            return val  # Return the original value if it's valid
        
        def show_auto_closing_message(message, timeout=2000):
            # Create a new Tkinter root window
            root = tk.Tk()
            root.withdraw()  # Hide the root window

            # Schedule a callback to destroy the pop-up after a timeout
            root.after(timeout, root.destroy)

            # Show messagebox
            messagebox.showinfo("INFORMATION", message)

        def get_automation_db_path():
            # Get the path to the user's desktop
            desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
            # Define the path for the KnexusAutomation folder
            knexus_folder_path = os.path.join(desktop_path, "KnexusAutomation")
            # Define the path for the automation.db file
            db_path = os.path.join(knexus_folder_path, "automation.db")
            return db_path
        
        def get_automation_log_path():
            # Get the path to the user's desktop
            desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
            # Define the path for the KnexusAutomation folder
            knexus_folder_path = os.path.join(desktop_path, "KnexusAutomation")
            # Define the path for the automation.db file
            log_path = os.path.join(knexus_folder_path, "RPA-LOGS")

            # Check if the KnexusAutomation folder exists, if not, create it
            if not os.path.exists(log_path):
                os.makedirs(log_path)
                print(f"Created folder: {log_path}")
            else:
                print(f"Folder already exists: {log_path}")

            return log_path