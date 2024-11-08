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


# Store data into the database
def store_data(company_code, user_code, user_name, user_password, automation_time):
    folder_path_for_db = setup_automation_folder()
    DB_PATH =  os.path.join(folder_path_for_db, "automation.db")
    print(f"DB_PATH: {DB_PATH}")
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute('''INSERT INTO users (companyCode, iLabUserCode, iLabUserName, iLabUserPassword, setAutomationTime)
                      VALUES (?, ?, ?, ?, ?)''', 
                      (company_code, user_code, user_name, user_password, automation_time))

    conn.commit()
    conn.close()

# Confirm action
def confirm_action():
    company_code = company_code_entry.get()
    user_code = user_code_entry.get()
    user_name = user_name_entry.get()
    user_password = user_password_entry.get()
    automation_time = automation_time_entry.get()

    if company_code and user_code and user_name and user_password and automation_time:
        try:
            store_data(company_code, user_code, user_name, user_password, automation_time)
            messagebox.showinfo("Success", "Data saved successfully!")
        except sqlite3.IntegrityError:
            messagebox.showerror("Error", "User with this 사업자 번호 already exists!")
        root.destroy()
    else:
        messagebox.showerror("Error", "All fields are required.")

# Update data in the database
def update_data(company_code, user_code, user_name, user_password, automation_time):

    folder_path_for_db = setup_automation_folder()
    DB_PATH =  os.path.join(folder_path_for_db, "automation.db")
    print(f"DB_PATH: {DB_PATH}")
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Update query based on iLabUserCode (can change this to another unique identifier)
    cursor.execute('''UPDATE users
                      SET companyCode = ?, iLabUserName = ?, iLabUserPassword = ?, setAutomationTime = ?
                      WHERE iLabUserCode = ?''', 
                      (company_code, user_name, user_password, automation_time, user_code))

    if cursor.rowcount == 0:
        messagebox.showerror("Error", "User not found!")
    else:
        messagebox.showinfo("Success", "User info updated successfully!")

    conn.commit()
    conn.close()

def update_action():
    company_code = company_code_entry.get()
    user_code = user_code_entry.get()
    user_name = user_name_entry.get()
    user_password = user_password_entry.get()
    automation_time = automation_time_entry.get()

    if company_code and user_code and user_name and user_password and automation_time:
        update_data(company_code, user_code, user_name, user_password, automation_time)
        root.destroy()
    else:
        messagebox.showerror("Error", "All fields are required.")

def cancel_action():
    root.destroy()
    
        
if __name__ == "__main__":
    folder_path_for_db = setup_automation_folder()
    init_db(folder_path_for_db)  # Ensure the database and tables are set up
    root.mainloop()  # Start the Tkinter UI
