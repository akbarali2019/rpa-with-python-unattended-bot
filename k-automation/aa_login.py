from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException
import time

#Step 1: Set up WebDriver
driver = webdriver.Chrome()

#Step2: Automate login
driver.execute("get", {'url': 'https://community.cloud.automationanywhere.digital/#/login?next=/index'})
time.sleep(2)

driver.maximize_window()

# Locate the username input field using a CSS selector
username = driver.find_element(By.CSS_SELECTOR, 'input.textinput-cell-input-control[name="username"]')
# Set the username value
username.send_keys("*")
time.sleep(1)

# Locate the password input field using a CSS selector
password = driver.find_element(By.CSS_SELECTOR, 'input.textinput-cell-input-control[name="password"]')
# Set the password value
password.send_keys("*")
time.sleep(1)

# Find and Forward login 'Button' using a CSS selector
login_btn = driver.find_element(By.CSS_SELECTOR, 'button[name="submitLogin"]')
# Click the login Button 
login_btn.click()

automation_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[href="#/bots/repository"]')))
automation_link.click()
time.sleep(2)

# Wait until the link is clickable and then click it
linkToParentFolder = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[href="#/bots/repository/private/folders/13015819"]'))
)
linkToParentFolder.click()
time.sleep(2)

# Wait until the link is clickable and then click it
linkToBotFile = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[href="#/bots/repository/private/files/13726012/module/hbc/process/edit"]'))
)
linkToBotFile.click()

# Wait until the iframe is available and switch to it
iframe = WebDriverWait(driver, 20).until(
    EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, 'iframe.modulepage-frame'))
)

# Wait until the "Run" button is clickable
run_button = WebDriverWait(driver, 20).until(
     EC.element_to_be_clickable((By.CSS_SELECTOR, 'div.pagelayout-header-controls button[name="process-run"]'))
 )

# Execute JavaScript to click the button
driver.execute_script("arguments[0].click();", run_button)

# Optionally, switch back to the main content after interaction
#driver.switch_to.default_content()

print("#################### Current URL after redirection:", driver.current_url)
# Wait for the modal to appear
try:

    # Wait until the URL changes or until a specific element on the new page is visible
    WebDriverWait(driver, 30).until(
        EC.url_contains('aari')  # Adjust this URL pattern based on what you expect
    )
    time.sleep(5)
    print("!!!!!!!!!!!!!!URL CONTAINS aari: ", driver.current_url)
    # Optionally, wait for the modal container
    modal = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'div.modal-form[data-modal-ready="true"]'))  # Adjust selector as needed
    )
    time.sleep(5)
    print('data-modal-ready="true"')
    # Ensure the modal is visible
    WebDriverWait(driver, 30).until(
        EC.visibility_of(modal)
    )
    time.sleep(5)
    # Locate and click the Confirm button within the modal
    confirm_button = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[name="submit"]'))  # Adjust selector as needed
    )
    time.sleep(5)
    print('button[name="submit"]')
    confirm_button.click()

except TimeoutException as e:
    print("Modal or Confirm button was not interactable.")
    driver.save_screenshot("screenshot.png")  # Save a screenshot for debugging
    raise

# Wait to observe the result
time.sleep(15)

# Clean up
driver.quit()