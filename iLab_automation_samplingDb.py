# import sqlite3
# import os

# RPA_DB_DIRECTORY_DB_FILE = r"C:\Users\LENOVO\Desktop\KEFA-RPA\rpa-pyhton\users.db"

# class RpaDBManager:
#     def rpa_db_manager():
#         # Create or connect to a local database file
#         if not os.path.exists(RPA_DB_DIRECTORY_DB_FILE):
#             os.makedirs(RPA_DB_DIRECTORY_DB_FILE)
#         conn = sqlite3.connect(RPA_DB_DIRECTORY_DB_FILE)

#         # Create a cursor object to execute SQL commands
#         cursor = conn.cursor()

#         # Create users table with auto-incrementing id
#         cursor.execute('''
#         CREATE TABLE IF NOT EXISTS users (
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             userCode INTEGER NOT NULL,
#             userName TEXT NOT NULL,
#             userPassword TEXT NOT NULL
#         )
#         ''')

#         # Create sampling_numbers table with a foreign key reference to the user id
#         cursor.execute('''
#         CREATE TABLE IF NOT EXISTS sampling_numbers (
#             samplingNumber TEXT NOT NULL,
#             userId INTEGER,
#             FOREIGN KEY (userId) REFERENCES users(id)
#         )
#         ''')

#         # Commit and close connection
#         conn.commit()
#         conn.close()

#     def insert_user(userCode, userName, userPassword):
#         conn = sqlite3.connect(RPA_DB_DIRECTORY_DB_FILE)
#         cursor = conn.cursor()

#         # Check if the user with this userCode already exists
#         cursor.execute('''
#         SELECT id FROM users WHERE userCode = ?
#         ''', (userCode,))
#         result = cursor.fetchone()

#         if result:
#             print(f"User with userCode {userCode} already exists.")
#             user_id = result[0]  # Get the existing user's id
#         else:
#             # Insert new user if they don't exist
#             cursor.execute('''
#             INSERT INTO users (userCode, userName, userPassword) 
#             VALUES (?, ?, ?)
#             ''', (userCode, userName, userPassword))
            
#             user_id = cursor.lastrowid
#             print(f"User with userCode {userCode} added to the database.")
        
#         conn.commit()
#         conn.close()

#         return user_id
    
#     # def insert_sampling_number(userId, samplingNumber):
#     #     conn = sqlite3.connect(RPA_DB_DIRECTORY_DB_FILE)
#     #     cursor = conn.cursor()

#     #     # Check if the samplingNumber already exists for the given userId
#     #     cursor.execute('''
#     #     SELECT COUNT(1) FROM sampling_numbers WHERE userId = ? AND samplingNumber = ?
#     #     ''', (userId, samplingNumber))
        
#     #     result = cursor.fetchone()

#     #     if result[0] > 0:
#     #         print(f"SamplingNumber {samplingNumber} already exists for userId {userId}. Skipping insertion.")
#     #     else:
#     #         # Insert samplingNumber if it doesn't exist
#     #         cursor.execute('''
#     #         INSERT INTO sampling_numbers (userId, samplingNumber)
#     #         VALUES (?, ?)
#     #         ''', (userId, samplingNumber))
            
#     #         print(f"SamplingNumber {samplingNumber} added for userId {userId}.")
        
#     #     conn.commit()
#     #     conn.close()



#     def get_user_id_by_code(userCode):
#         conn = sqlite3.connect(RPA_DB_DIRECTORY_DB_FILE)
#         cursor = conn.cursor()

#         # Query to get userId from users table based on userCode
#         cursor.execute('''
#         SELECT id FROM users WHERE userCode = ?
#         ''', (userCode,))
#         resultId = cursor.fetchone()

#         conn.close()

#         if resultId:
#             return resultId[0]  # Return userId
#         else:
#             return None  # If user not found
        

#     def check_sampling_number_exists(userId, samplingNumber):
#         conn = sqlite3.connect(RPA_DB_DIRECTORY_DB_FILE)
#         cursor = conn.cursor()

#         # Query to check if the samplingNumber exists for the specific userId
#         cursor.execute('''
#         SELECT COUNT(1) FROM sampling_numbers WHERE userId = ? AND samplingNumber = ?
#         ''', (userId, samplingNumber))

#         result = cursor.fetchone()

#         conn.close()

#         return result[0] > 0  # Return True if exists, False otherwise
    

#     def insert_sampling_number(userId, samplingNumber, status="PENDING"):
#         conn = sqlite3.connect(RPA_DB_DIRECTORY_DB_FILE)
#         cursor = conn.cursor()

#         # Insert into sampling_numbers table
#         cursor.execute('''
#         INSERT INTO sampling_numbers (userId, samplingNumber, kefalabStatus)
#         VALUES (?, ?, ?)
#         ''', (userId, samplingNumber, status))

#         conn.commit()
#         conn.close()


 
        
    


