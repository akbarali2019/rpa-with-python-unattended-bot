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
        

    
