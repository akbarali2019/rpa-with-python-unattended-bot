import requests
from iLab_automation_steps import IlabAutomationSteps
from iLab_automation_helper import Helper
from iLab_automation_log import LoggerConfig

class StartILabAutomation:

    def __init__(self):
        self.logger = LoggerConfig.setup_logger()

    def start_iLab_automation(self):
        self.logger.info("start_iLab_automation ==> iLab Sampling Automation is Starting...")
        # initialize hasNextSamplingInquiry to True to begin RPA logic 
        hasNextSamplingInquiries = True
        # Api call for kefalab.com to get started with RPA
        while hasNextSamplingInquiries:
            url = ""
            self.logger.info(f"start_iLab_automation ==> Call for api: {url} to get iLab sampling data")
            response = requests.get(url)
            # check api call is successfull and then proceed if it is. Otherwise log about it in the 'else' statement 
            if response.status_code == 200:
                data = response.json()
                hasNext = data.get('hasNext')
                self.logger.info(f"start_iLab_automation ==> SamplingInquiry hasNext: {hasNext}. Loop Starting...\n")
                print(data)
                self.logger.info(f"{data}\n")

                totalElements = data.get('totalElements')

                # break the loop if there hasNext == 'break'
                if hasNext == 'break' or totalElements == 0:
                    hasNextSamplingInquiries = False
                    self.logger.info(f"start_iLab_automation ==> SamplingInquiry hasNext: {hasNext}. So Loop Ended!")
                    print(f"SamplingInquiry hasNext: {hasNext}. So Loop Ended!")
                
                # if totalElements equals to 0, then stop to preceed the automation and log about it in the 'else' part
                if totalElements != 0:
                    IlabAutomationSteps.work_on_sampling(self, data)
                else:
                    self.logger.info(f"start_iLab_automation ==> No Automation TO DO for now! Total Elements equal to {totalElements}") 
                    Helper.show_auto_closing_message(f"No Automation TO DO for now! Total Elements equal to {totalElements}") # removable later
            else:
                hasNextSamplingInquiries = False
                self.logger.warning(f"start_iLab_automation ==> API Response for {url}: {response.text}")
                print(f"API Call for {url} Failed! Response: {response.text}")

                
            
