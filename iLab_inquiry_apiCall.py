from iLab_automation_log import LoggerConfig 
from iLab_automation_helper import Helper
from Inquiry.iLab_inquiry_start import StartILabInquiry 
import requests

class InquiryAPI:

    def __init__(self):
        self.logger = LoggerConfig.setup_logger()

    def inquiry_apiCall(self):
        print(f"API CALL to get available Inquiry Numbers")

        self.logger.info("start_iLab_automation ==> iLab Sampling Automation is Starting...")
        # initialize hasNextSamplingInquiry to True to begin RPA logic 
        hasNextInquiryNumbers = True
        # Api call for kefalab.com to get started with RPA
        while hasNextInquiryNumbers:
            url = "" 
            self.logger.info(f"start_iLab_automation ==> Call for Inquiry api: {url} to get iLab inquiryNumbers data")
            response = requests.post(url)
            # check api call is successfull and then proceed if it is. Otherwise log about it in the 'else' statement 
            if response.status_code == 200:
                data = response.json()
                inquiryHasNext = data.get('hasNext')
                self.logger.info(f"start_iLab_automation ==> Inquiry hasNext: {inquiryHasNext}. Loop Starting...\n")
                print(data)
                self.logger.info(f"{data}\n")

                inquirytotalElements = data.get('totalElements')

                # break the loop if there hasNext == 'break'
                if inquiryHasNext == 'break' or inquirytotalElements == 0:
                    hasNextInquiryNumbers = False
                    self.logger.info(f"start_iLab_automation ==> Inquiry hasNext: {inquiryHasNext}. So Loop Ended!")
                    print(f"Inquiry inquiryHasNext: {inquiryHasNext}. So Loop Ended!")
                
                # if totalElements equals to 0, then stop to preceed the automation and log about it in the 'else' part
                if inquirytotalElements != 0:
                    print(f"inquirytotalElements: {inquirytotalElements}. StartILabInquiry.inquiryProcess_dbCheck(self, data) can be continued!!!")
                    StartILabInquiry.inquiryProcess_dbCheck(self, data)
                else:
                    self.logger.info(f"start_iLab_automation ==> No Automation TO DO for now! Total Elements equal to {inquirytotalElements}") 
                    Helper.show_auto_closing_message(f"No INQUIRY Automation TO DO for now! Total Elements equal to {inquirytotalElements}") # removable later
            else:
                hasNextInquiryNumbers = False
                self.logger.warning(f"start_iLab_automation ==> API Response for {url}: {response.text}")
                print(f"API Call for {url} Failed! Response: {response.text}")
                print(f"response.status_code : {response.status_code }")
