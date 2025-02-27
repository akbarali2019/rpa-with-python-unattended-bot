import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pyautogui
from selenium.webdriver.support.ui import Select
from ilab_automation_localDb import CheckLocalDb

class EcoLabDetailedAutomations:

    def open_driver_session(self):
        driver = webdriver.Chrome()
        return driver
    
    def window_configs(self, driver):
        driver.maximize_window()
        time.sleep(2)
        ecolabUrl = "https://www.xn--lu5b7kx8m.kr/init.go"
        
        # Open the target web application
        driver.get(ecolabUrl) 
        main_window = driver.current_window_handle
        # Detect and handle the new window
        WebDriverWait(driver, 10).until(
            lambda d: len(d.window_handles) > 1  # Wait until a new window appears
        )

        new_window = [handle for handle in driver.window_handles if handle != main_window][0]
        driver.switch_to.window(new_window)
        driver.close()
        driver.switch_to.window(main_window)

    def ecolab_login(self, driver, companyCode):
        username_field =WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.NAME, "user_email")))
        
        ecolabUserCredentials = CheckLocalDb.get_ecoLabUser_details_by_company_code(companyCode)
        ecolab_username = ecolabUserCredentials[0]  # OR Later Replace with API call ==> samplings[sampling].get('iLabUserId')
        ecolab_userpassword = ecolabUserCredentials[1]  # OR Later Replace with API call ==> samplings[sampling].get('iLabUserPassword')
        username_field.send_keys(ecolab_username)  # Replace with your actual username
        time.sleep(0.5)
        password_field = driver.find_element(By.NAME, "login_pwd_confirm")  # Replace with the correct locator
        password_field.send_keys(ecolab_userpassword)  # Replace with your actual password
        time.sleep(0.5)
        password_field.send_keys(Keys.RETURN)
        time.sleep(1)

    def close_alarm_dialog(self, driver):
        try:
            print("close_alarm_dialog")
            # Wait for the modal dialog to appear
            WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.ID, 'myModalEquipDupCnt'))
            )
            print("myModalEquipDupCnt detected")
            
            # Use JavaScript to locate and click the close button
            driver.execute_script("""
                document.querySelector("#myModalEquipDupCnt > div > div > div.modal-header > button").click();
            """)
            print("Close button clicked using JavaScript")

            # Wait for the modal dialog to disappear
            WebDriverWait(driver, 10).until(
                EC.invisibility_of_element((By.ID, 'myModalEquipDupCnt'))
            )
            print("invisibility of myModalEquipDupCnt detected")
            time.sleep(0.5)  # Ensure it's fully closed
        except Exception as e:
            print(f"Error closing alarm dialog: {e}")



    def click_sidebarMenu_subMenu(self, driver):
        # Wait for the sidebar menu element to be visible and clickable
        sidebar_menu = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="left-panel"]/nav/ul/li[5]/a/span'))
        )
        # Click the sidebar menu
        sidebar_menu.click()
        time.sleep(1)

        # Wait for the submenu item to be visible and clickable
        submenu_item = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="left-panel"]/nav/ul/li[5]/ul/li[1]/a'))
        )
        # Scroll into view (optional)
        # driver.execute_script("arguments[0].scrollIntoView(true);", submenu_item) //changed 2025-01-09
        # Click the submenu item
        submenu_item.click()
        time.sleep(0.5)

    def input_search_date(self, driver, date):
        # Locate the input field
        date_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "search_meas_start_dt"))
        )
        time.sleep(0.5)
        # Clear the field using JavaScript
        driver.execute_script("arguments[0].value = '';", date_input)
        time.sleep(0.5)
        # Input the new value
        date_input.send_keys(date)
        date_input.send_keys(Keys.ENTER)  # Simulate pressing Enter

    def input_search_regNumber(self, driver, sampling_reg_number):
        # Wait for the input field to be visible and interactable
        reg_number_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "search_meas_mgmt_no"))
        )

        # Clear the field (optional if it's already empty)
        reg_number_input.clear()
        time.sleep(0.5)
        # Input the registration number
        reg_number_input.send_keys(sampling_reg_number)
        time.sleep(0.5)
        # Simulate pressing Enter to trigger 'onkeyup' if required
        reg_number_input.send_keys(Keys.ENTER)  # Simulate Enter (or replace with another key if needed)
        time.sleep(2.5) # don't decrease

    # def regNumber_based_mouseClick(self, driver):
    #     # Wait for the canvas or grid to load
    #     WebDriverWait(driver, 10).until(
    #         EC.presence_of_element_located((By.XPATH, "//*[@id='gridVisistPlanList']/div/canvas"))
    #     )
        
    #     time.sleep(0.5)
    #     pyautogui.moveTo(430, 465, 0.5) # 접수번호 table row click
    #     time.sleep(0.5)
    #     pyautogui.doubleClick()

    #     time.sleep(1.5) #added 2024-01-09

    #     # Wait for the tab element to be clickable
    #     tab_element = WebDriverWait(driver, 10).until(
    #         EC.element_to_be_clickable((By.ID, "ui-id-2"))  # Using the `id` attribute
    #     )

    #     time.sleep(1.5) #added 2024-01-09
    #     # Click the tab
    #     tab_element.click()


    # Updated UI framework removing a canvas by Ecolab - 2025-02-27
    def regNumber_based_mouseClick(self, driver):
        
        # Wait for the canvas or grid to load
        # WebDriverWait(driver, 10).until(
        #     EC.presence_of_element_located((By.XPATH, "//*[@id='gridVisistPlanList']/div/canvas"))
        # )
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//*[@id='gridVisistPlanList']"))
        ) # updated ecolab ui 2025-02-27 from [@id='gridVisistPlanList']/div/canvas into [@id='gridVisistPlanList']
        time.sleep(0.5)
        pyautogui.moveTo(430, 465, 0.5) # 접수번호 table row click
        time.sleep(0.5)
        pyautogui.doubleClick()

        time.sleep(1.5) #added 2024-01-09

        # Wait for the tab element to be clickable
        tab_element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "ui-id-2"))  # Using the `id` attribute
        )

        time.sleep(1.5) #added 2024-01-09
        # Click the tab
        tab_element.click()


    def input_meaEndDate(self, driver, meaEndDate):
        time.sleep(1.5)
        # Locate the input field
        date_input = driver.find_element(By.ID, "meas_end_dt")
        # Set the value using JavaScript
        driver.execute_script(f"arguments[0].value = '{meaEndDate}';", date_input)
        date_input.send_keys(Keys.ENTER)

    def input_meaStartTime(self, driver, meaStartTime):
        time.sleep(0.2)
        # Locate the input field
        time_start_input = driver.find_element(By.ID, "meas_start_time")
        # Set the value using JavaScript
        driver.execute_script(f"arguments[0].value = '{meaStartTime}';", time_start_input)
        time_start_input.send_keys(Keys.ENTER)
    
    def input_meaEndTime(self, driver, meaEndTime):
        time.sleep(0.2)
        # Locate the input field
        time_end_input = driver.find_element(By.ID, "meas_end_time")
        # Set the value using JavaScript
        driver.execute_script(f"arguments[0].value = '{meaEndTime}';", time_end_input)
        time_end_input.send_keys(Keys.ENTER)

    def input_meaWeather(self, driver, meaWeather):
        time.sleep(0.2)
        # Locate the input field 날씨
        weather_input = driver.find_element(By.NAME, "meas_wthr")
        # Set the value using JavaScript
        driver.execute_script(f"arguments[0].value = '{meaWeather}';", weather_input)

    def input_meaTemper(self, driver, meaTemper):
        time.sleep(0.2)
        # Locate the input field 기온 (℃)
        temper_input = driver.find_element(By.NAME, "meas_temper")
        # Set the value using JavaScript
        driver.execute_script(f"arguments[0].value = '{meaTemper}';", temper_input)

    def input_meaHumidity(self, driver, meaHumidity):
        time.sleep(0.2)
        # Locate the input field 습도 (%)
        humidity_input = driver.find_element(By.NAME, "meas_humd")
        # Set the value using JavaScript
        driver.execute_script(f"arguments[0].value = '{meaHumidity}';", humidity_input)
    
    def input_meaAtmosPress(self, driver, meaAtmosPress):
        time.sleep(0.2)
        # Locate the input field 대기압 (mmHg)
        atmospheric_input = driver.find_element(By.NAME, "meas_atoms")
        # Set the value using JavaScript
        driver.execute_script(f"arguments[0].value = '{meaAtmosPress}';", atmospheric_input)
    
    def input_meaWindDir(self, driver, meaWindDir): 
        # Filter the API value to match the dropdown value or return the original value
        filtered_value = EcoLabDetailedAutomations.filter_meaWindDir(meaWindDir)
        
        time.sleep(0.2)
        # Wait for the dropdown to be visible
        dropdown = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "meas_wdir"))
        )
        # Create a Select object
        select = Select(dropdown)
        # Select the desired value by visible text
        select.select_by_visible_text(filtered_value)

    def filter_meaWindDir(api_value):
        # Define the mapping from API values to dropdown values
        mapping = {
            "북북동": "북-북동",
            "동북동": "동-북동",
            "동남동": "동-남동",
            "남남동": "남-남동",
            "남남서": "남-남서",
            "서남서": "서-남서",
            "서북서": "서-북서",
            "북북서": "북-북서"
        }

        # If the value is in the mapping, return the mapped value; otherwise, return the same value
        return mapping.get(api_value, api_value)


    
    def input_meaWindSpeed(self, driver, meaWindSpeed):
        time.sleep(0.2)
        # Locate the input field 풍속 (m/s)
        windSpeed_input = driver.find_element(By.NAME, "meas_wspd")
        # Set the value using JavaScript
        driver.execute_script(f"arguments[0].value = '{meaWindSpeed}';", windSpeed_input)

    def input_eGasAmount(self, driver, eGasAmount):
        time.sleep(0.2)
        # Locate the input field 배출가스 유량(Sm/분) (산소보정 전)
        gas_fvol_input = driver.find_element(By.ID, "meas_gas_fvol")
        # Set the value using JavaScript
        driver.execute_script(f"arguments[0].value = '{eGasAmount}';", gas_fvol_input)

    def input_stdOxygen(self, driver, gas_stdOxygen):
        time.sleep(0.2)
        # Locate the input field 배출가스 유량(Sm/분) (산소보정 후)
        basis_o2c_input = driver.find_element(By.ID, "basis_o2c")
        # Set the value using JavaScript
        driver.execute_script(f"arguments[0].value = '{gas_stdOxygen}';", basis_o2c_input)

    def input_stdOxygenEqvAmount(self, driver, gas_stdOxygenEqvAmount):
        time.sleep(0.2)
        # Locate the input field 배출가스 유량(Sm/분) (산소보정 후)
        gas_fvol_o2_aft_input = driver.find_element(By.ID, "meas_gas_fvol_o2_aft")
        # Set the value using JavaScript
        driver.execute_script(f"arguments[0].value = '{gas_stdOxygenEqvAmount}';", gas_fvol_o2_aft_input)
    
    def input_measureO2(self, driver, measureO2):
        time.sleep(0.2)
        # Locate the input field 산소농도(%) // 측정 O2 (%)
        gas_meas_o2c_input = driver.find_element(By.ID, "meas_o2c")
        # Set the value using JavaScript
        driver.execute_script(f"arguments[0].value = '{measureO2}';", gas_meas_o2c_input)

    def input_eGasTempAvg(self, driver, eGasTempAvg):
        time.sleep(0.2)
        # Locate the input field 배출가스온도(℃)
        gas_meter_temper_input = driver.find_element(By.ID, "gas_meter_temper")
        # Set the value using JavaScript
        driver.execute_script(f"arguments[0].value = '{eGasTempAvg}';", gas_meter_temper_input)

    def input_mositureAmount(self, driver, mositureAmount):
        time.sleep(0.2)
        # Locate the input field 수분량(%)
        meas_humd_vol_input = driver.find_element(By.ID, "meas_humd_vol")
        # Set the value using JavaScript
        driver.execute_script(f"arguments[0].value = '{mositureAmount}';", meas_humd_vol_input)

    def input_eGasFlowSpeed(self, driver, eGasFlowSpeed):
        time.sleep(0.2)
        # Locate the input field 배출가스 속도(m/s)
        meas_fspd_input = driver.find_element(By.ID, "meas_fspd")
        # Set the value using JavaScript
        driver.execute_script(f"arguments[0].value = '{eGasFlowSpeed}';", meas_fspd_input)

    def input_meaOpinion(self, driver, meaOpinion):
        time.sleep(0.2)
        # Locate the textarea 채취자 의견
        mOpinion_textarea = driver.find_element(By.ID, "smpl_ctor_opin")
        # Set the value using JavaScript (handle null/empty cases)
        if meaOpinion:
            driver.execute_script("arguments[0].value = arguments[1];", mOpinion_textarea, meaOpinion)
        else:
            print("API returned empty value. mOpinion_textarea left empty.")

    def input_meaMemo(self, driver, meaMemo):
        time.sleep(0.2)
        # Locate the textarea 비고
        samplingMemo_textarea = driver.find_element(By.ID, "remark1")
        # Set the value using JavaScript (handle null/empty cases)
        if meaMemo:
            driver.execute_script("arguments[0].value = arguments[1];", samplingMemo_textarea, meaMemo)
        else:
            print("API returned empty value. samplingMemo_textarea left empty.")

    def upload_files(self, driver, folder_path):
        # Loop through all files in the folder
        for file_name in os.listdir(folder_path):
            # Ensure it's a file and a PDF
            if file_name.lower().endswith(".pdf"):
                file_path = os.path.join(folder_path, file_name)  # Construct full file path

                if os.path.isfile(file_path):
                    if "report" in file_name.lower():
                        # Use the XPath for files that include "report"
                        add_file_xpath = "//*[@id='fileArea']/section/div/div[1]/input[1]"
                        print(f"Uploading file with 'report': {file_path}")
                    else:
                        # Use the XPath for files that do not include "report"
                        add_file_xpath = "//*[@id='fileAreaAdd']/section/div/div[1]/input[1]"
                        print(f"Uploading file without 'report': {file_path}")

                    # Step 1: Click the appropriate "Add File" button
                    add_file_button = WebDriverWait(driver, 10).until(
                        EC.element_to_be_clickable((By.XPATH, add_file_xpath))
                    )
                    add_file_button.click()

                    # Step 2: Wait for the file dialog to open
                    time.sleep(2)  # Adjust based on dialog opening time

                    # Step 3: Upload the file by sending its path
                    file_input = WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.XPATH, "//input[@type='file']"))
                    )
                    file_input.send_keys(file_path)
                 
                    # Navigate the UI after uploading
                    pyautogui.press('tab', 3, 0.5)
                    pyautogui.press('enter')

                    # Step 4: Wait for any success confirmation (if applicable)
                    time.sleep(5)  # Adjust as needed for processing delays
            else:
                print(f"Skipped file: {file_name} (Not a PDF)")


    # Updated to Close file upload dialog 
    def new_upload_files(self, driver, folder_path):
        # Loop through all files in the folder
        for file_name in os.listdir(folder_path):
            # Ensure it's a file and a PDF
            if file_name.lower().endswith(".pdf"):
                file_path = os.path.join(folder_path, file_name)  # Construct full file path

                if os.path.isfile(file_path):
                    if "report" in file_name.lower():
                        # Use the XPath for files that include "report"
                        add_file_xpath = "//*[@id='fileArea']/section/div/div[1]/input[1]"
                        print(f"Uploading file with 'report': {file_path}")
                    else:
                        # Use the XPath for files that do not include "report"
                        add_file_xpath = "//*[@id='fileAreaAdd']/section/div/div[1]/input[1]"
                        print(f"Uploading file without 'report': {file_path}")

                    # Step 1: Click the appropriate "Add File" button
                    add_file_button = WebDriverWait(driver, 10).until(
                        EC.element_to_be_clickable((By.XPATH, add_file_xpath))
                    )
                    add_file_button.click()

                    # Step 2: Wait for the file dialog to open
                    time.sleep(2)  # Adjust based on dialog opening time

                    # Step 3: Upload the file by sending its path
                    file_input = WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.XPATH, "//input[@type='file']"))
                    )
                    file_input.send_keys(file_path)
                    
                    time.sleep(2) # new

                    #time.sleep(5) # new
                    pyautogui.press("esc") # new
                    #time.sleep(1) # new
                    #print(f"Closed file upload dialog.")
                     

                    # Navigate the UI after uploading
                    #####pyautogui.press('tab', 3, 0.5)
                    #####pyautogui.press('enter')


                    # Step 4: Wait for any success confirmation (if applicable)
                    ####time.sleep(5)  # Adjust as needed for processing delays
                time.sleep(5)
            else:
                print(f"Skipped file: {file_name} (Not a PDF)")
                return
        print(f"Closed file upload dialog.")

    def temp_save(self, driver):
        print("*************temp_save SAVING")
        time.sleep(3)
        # Trigger the click event directly with JavaScript
        driver.execute_script("document.getElementById('btnDraftMsFieldDoc').click();")
        time.sleep(7)
        pyautogui.press('enter')
        time.sleep(3)
        pyautogui.press('enter')
        print("*************temp_save SAVING TIME FINISHED")

    def quit_driver(self, driver):
        print("***********quit_driver")
        time.sleep(0.5) #2
        # Close the browser and end the WebDriver session    
        driver.quit()
        print("Driver Session completed/closed successfully!")
        time.sleep(1)


