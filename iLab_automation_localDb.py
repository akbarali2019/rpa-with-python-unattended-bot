import sqlite3
from iLab_automation_helper import Helper

class CheckLocalDb:

    def get_user_id_by_company_code(company_code):

        RPA_DB_DIRECTORY_DB_FILE = Helper.get_automation_db_path()
        conn = sqlite3.connect(RPA_DB_DIRECTORY_DB_FILE)
        cursor = conn.cursor()

        # Query to get userId based on companyCode
        cursor.execute('''SELECT userId FROM users WHERE companyCode = ?''', (company_code,))
        user_id = cursor.fetchone()  # Fetch one result

        conn.close()

        if user_id:
            return user_id[0]  # Return the userId if found
        else:
            return None  # Return None if no user found
        
    def check_ilab_status_forSampling(company_code, sampling_reg_number):
        user_id = CheckLocalDb.get_user_id_by_company_code(company_code)

        if user_id is not None:
            RPA_DB_DIRECTORY_DB_FILE = Helper.get_automation_db_path()
            conn = sqlite3.connect(RPA_DB_DIRECTORY_DB_FILE)
            cursor = conn.cursor()

            # Check the iLabStatus of the specific samplingRegNumber for the user/company
            cursor.execute('''SELECT samplingStatus FROM inquiries 
                            WHERE inquiryNumber = ? AND userId = ?''', 
                            (sampling_reg_number, user_id))
            status = cursor.fetchone()

            conn.close()

            if status:
                return status[0]  # Return the iLabStatus
            else:
                return None  # No record found for the samplingRegNumber
        else:
            print(f"No user found with companyCode: {company_code}")
            return None

    def check_inquiry_exists_for_company(inquiry_number, company_code):
            RPA_DB_DIRECTORY_DB_FILE = Helper.get_automation_db_path()
            conn = sqlite3.connect(RPA_DB_DIRECTORY_DB_FILE)
            cursor = conn.cursor()
    
            # Get the userId associated with the companyCode
            cursor.execute('''SELECT userId FROM users WHERE companyCode = ?''', (company_code,))
            user = cursor.fetchone()
    
            if user:
                user_id = user[0]
                
                # Check if the inquiry number exists for this userId (specific to the company)
                cursor.execute('''SELECT inquiryId FROM inquiries WHERE inquiryNumber = ? AND userId = ?''', 
                            (inquiry_number, user_id))
                inquiry = cursor.fetchone()
                
                conn.close()
    
                if inquiry:
                    return True  # Inquiry number exists for this company
                else:
                    return False  # Inquiry number does not exist for this company
            else:
                conn.close()
                return False  # No user found for this company
    
    
        def insert_inquiry(inquiry_number, company_code):
            # Get userId based on companyCode
            user_id = CheckLocalDb.get_user_id_by_company_code(company_code)
    
            if user_id is not None:
                RPA_DB_DIRECTORY_DB_FILE = Helper.get_automation_db_path()
                conn = sqlite3.connect(RPA_DB_DIRECTORY_DB_FILE)
                cursor = conn.cursor()
    
                # Insert the inquiry since it does not exist
                cursor.execute('''INSERT INTO inquiries (inquiryNumber, userId) 
                                VALUES (?, ?)''', 
                                (inquiry_number, user_id))
    
                conn.commit()
                conn.close()
                print(f"Inquiry number '{inquiry_number}' successfully inserted.")
            else:
                print(f"No user found with companyCode: {company_code}")
        

    