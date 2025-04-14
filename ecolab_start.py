import requests
from iLab_automation_log import LoggerConfig
from .ecolab_dbCheck import EcoLabDbCheck
from .ecolab_process_detailed import EcoLabDetailedAutomations

# ATTENTION! Company Code should be retreived by API call from the kefalab.com, after the version is being updated. 
COMPANY_CODE = "****"
API_URL = "*******"

class ApiCallForEcolab:
    def __init__(self):
        self.logger = LoggerConfig.setup_logger()

    def start_ecoLab_automation(self):
        """Start the EcoLab automation process."""
        self.logger.info("EcoLab Automation is starting...")
        has_next_inquiries = True

        while has_next_inquiries:
            try:
                response = requests.post(API_URL)
                response.raise_for_status()  # Raise error for HTTP issues
            except Exception as e:
                self.logger.error(f"An error occurred during EcoLab automation: {e}")
                break

            data = response.json()
            has_next = data.get('hasNext')
            total_elements = data.get('totalElements', 0)

            self.logger.info(f"API response: hasNext={has_next}, totalElements={total_elements}")

            # Proceed with automation if inquiries are available
            if total_elements > 0:
                self._process_sampling_data(data)

            # Stop fetching inquiries if hasNext is "break"
            if has_next == "break":
                self.logger.info("Stopping further inquiries as hasNext is 'break'.")
                has_next_inquiries = False

    def _process_sampling_data(self, data):
        """Process the fetched sampling data."""
        self.logger.info("Starting the automation process for sampling data.")
        ecoLabAutos = EcoLabDetailedAutomations()

        try:
            # Open the WebDriver session
            self.logger.info("Opening WebDriver session...")
            driver = ecoLabAutos.open_driver_session()
            
            # Configure the window and log in
            ecoLabAutos.window_configs(driver)
            ecoLabAutos.ecolab_login(driver, COMPANY_CODE)

            # Perform EcoLab automation
            self.logger.info("Processing EcoLab inquiries...")
            db_checker = EcoLabDbCheck()
            db_checker.work_on_ecolab(data, ecoLabAutos, driver, COMPANY_CODE)

        except Exception as e:
            self.logger.error(f"Error during sampling data processing: {e}")
        finally:
            # Ensure WebDriver is always closed
            self.logger.info("Closing WebDriver session...")
            ecoLabAutos.quit_driver(driver)
