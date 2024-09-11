from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException
import time

################################################## STEP 1: Set up WebDriver
print('\n##### Setting up WebDriver')
aari_driver = webdriver.Chrome()

################################################## STEP 2: Visit to AARI
print('##### Visiting Automation Anywhere AARI')
url = "https://community.cloud.automationanywhere.digital/aari/#/processes?processInfoId=10699&name=process-test-1"
aari_driver.execute("get", {'url': url})
time.sleep(2)

# Maximize a current window
aari_driver.maximize_window()

################################################## STEP 3: Automate AARI login
# Locate the username input field using a CSS selector
print('##### Logging in Automation Anywhere AARI')
aari_username = aari_driver.find_element(By.CSS_SELECTOR, 'input.textinput-cell-input-control[name="username"]')
# Set the username value
aari_username.send_keys("*")
time.sleep(1)

# Locate the password input field using a CSS selector
aari_password = aari_driver.find_element(By.CSS_SELECTOR, 'input.textinput-cell-input-control[name="password"]')
# Set the password value
aari_password.send_keys("*")
time.sleep(1)

# Find and Forward login 'Button' using a CSS selector
aari_login_btn = aari_driver.find_element(By.CSS_SELECTOR, 'button[name="submitLogin"]')
# Click the login Button 
aari_login_btn.click()
print('##### Successfully Logged in Automation Anywhere AARI')
time.sleep(5)
print("Current Url: ", aari_driver.current_url)

################################################## STEP 4: AARI Submit button to Execute KEFA BOT
# Find and Forward login 'Button' using a CSS selector
aari_submit_btn = aari_driver.find_element(By.CSS_SELECTOR, 'button[name="submit"]')
# Click the login Button 
aari_submit_btn.click()
print('<<<THE KEFA BOT HAS BEEN STARTED TO EXECUTE>>>')
time.sleep(120)
# Clean up
aari_driver.quit()