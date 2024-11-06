import tkinter as tk
from tkinter import messagebox
import sqlite3
import os

# Db parent folder setup
def setup_automation_folder():
    # Get the path to the user's desktop
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    # Define the path for the KnexusAutomation folder
    knexus_folder_path = os.path.join(desktop_path, "KnexusAutomation")

    # Check if the KnexusAutomation folder exists, if not, create it
    if not os.path.exists(knexus_folder_path):
        os.makedirs(knexus_folder_path)
        print(f"Created folder: {knexus_folder_path}")
    else:
        print(f"Folder already exists: {knexus_folder_path}")

    return knexus_folder_path

# Initialize the database and create the tables
def init_db(folder_path_for_db):
    # Define the path for the automation.db file
    DB_PATH =  os.path.join(folder_path_for_db, "automation.db")
    print(f"DB_PATH: {DB_PATH}")

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Create users table
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                        userId INTEGER PRIMARY KEY AUTOINCREMENT,
                        companyCode TEXT,
                        iLabUserCode TEXT UNIQUE,   -- Make this unique
                        iLabUserName TEXT,
                        iLabUserPassword TEXT,
                        setAutomationTime TEXT)''')
    
    # Create inquiries table with foreign key userId
    cursor.execute('''CREATE TABLE IF NOT EXISTS inquiries (
                        inquiryId INTEGER PRIMARY KEY AUTOINCREMENT,
                        userId INTEGER,
                        inquiryNumber TEXT,
                        samplingStatus TEXT DEFAULT 'PENDING',
                        inquiryStatus TEXT DEFAULT 'PENDING',
                        FOREIGN KEY(userId) REFERENCES users(userId))''')

    conn.commit()
    conn.close()

if __name__ == "__main__":
    folder_path_for_db = setup_automation_folder()
    init_db(folder_path_for_db)  # Ensure the database and tables are set up
    root.mainloop()  # Start the Tkinter UI
