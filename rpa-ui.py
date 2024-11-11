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


# Function to center the window on the screen
def center_window(width=550, height=400):
    # Get the screen's width and height
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # Calculate the x and y coordinates to center the window
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)

    # Set the window size and position it at the center of the screen
    root.geometry(f"{width}x{height}+{x}+{y}")

# Create the UI window

# Define the font style
root = tk.Tk()
root.title(" Required Input for Automation ")
#root.configure(bg='black')
center_window(550, 400)

# Labels and Entry Fields
tk.Label(root, text="사업자 번호:", width=20).grid(row=0, column=0, padx=10, pady=10)
company_code_entry = tk.Entry(root, width=40)
company_code_entry.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="아이랩 긱관 코드:", width=20).grid(row=1, column=0, padx=10, pady=10)
user_code_entry = tk.Entry(root, width=40)
user_code_entry.grid(row=1, column=1, padx=10, pady=10)

tk.Label(root, text="아이랩 User ID:", width=20).grid(row=2, column=0, padx=10, pady=10)
user_name_entry = tk.Entry(root, width=40)
user_name_entry.grid(row=2, column=1, padx=10, pady=10)

tk.Label(root, text="아이랩 Password:", width=20).grid(row=3, column=0, padx=10, pady=10)
user_password_entry = tk.Entry(root, width=40, show="*")
user_password_entry.grid(row=3, column=1, padx=10, pady=10)

tk.Label(root, text="아이랩 Automation Time:", width=20).grid(row=4, column=0, padx=10, pady=10)
automation_time_entry = tk.Entry(root, width=40)
automation_time_entry.grid(row=4, column=1, padx=10, pady=10)

# Buttons with desired positions and layout
confirm_button = tk.Button(root, text="Confirm", width=12, command=confirm_action)
confirm_button.grid(row=5, column=0, padx=20, pady=20, sticky="e")

cancel_button = tk.Button(root, text="Cancel", width=12, command=cancel_action)
cancel_button.grid(row=5, column=1, padx=10, pady=20, sticky="w")

update_button = tk.Button(root, text="Update", width=12, command=update_action)
update_button.grid(row=5, column=2, padx=0, pady=20, sticky="w")
    
        
if __name__ == "__main__":
    folder_path_for_db = setup_automation_folder()
    init_db(folder_path_for_db)  # Ensure the database and tables are set up
    root.mainloop()  # Start the Tkinter UI
