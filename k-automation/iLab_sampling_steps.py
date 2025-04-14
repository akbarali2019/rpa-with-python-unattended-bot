
from iLab_automation_process import ILabAutomationProcesses
from Sampling.iLab_sampling_input_cells import ILabInputCells
from Sampling.iLab_sampling_gaseousSteps import GaseousSteps
from Sampling.iLab_sampling_notifiyCompletion import NotifyCompletion
from iLab_automation_helper import Helper
from iLab_automation_log import LoggerConfig
from ilab_automation_localDb import CheckLocalDb
import time

class IlabAutomationSteps:

    def __init__(self):
        self.logger = LoggerConfig.setup_logger()

    def work_on_sampling(self, data):
            
            # access to samplings data and get num of samplings
            samplings = data.get('samplings', [])
            numberOfSampling = len(samplings)
            self.logger.info(f"work_on_sampling ==> number of samplings list: {numberOfSampling}")
            print(f"NUMBER OF SAMPLINGS LIST: {numberOfSampling}")

            # loop according to samplings number
            for sampling in range(numberOfSampling):
                companyCode = "4800804"
                samplingId = samplings[sampling].get('samplingId')
                samplingRegNumber = samplings[sampling].get('samplingRegNumber')

                self.logger.info(f"work_on_sampling ==> ilab_automation_steps func is starting for samplingId: {samplingId} and samplingRegNumber: {samplingRegNumber}")
                print(f"samplingId: {samplingId}")
                print(f"samplingRegNumber: {samplingRegNumber}")
                
                # check local db to know the status of samplingRegNumber before proceeding an automation
               # Check if inquiry number exists for this specific company
                if CheckLocalDb.check_inquiry_exists_for_company(samplingRegNumber, companyCode):
                    print(f"Confirmation of Inquiry number.  Inquiry number '{samplingRegNumber}' exists for company '{companyCode}'.")
                    IlabAutomationSteps.ilab_automation_steps(self, companyCode, samplingId, samplingRegNumber, samplings, sampling)
                # CheckLocalDb.ilab_automation_checkLocalDbStatusOfSamplingRegNumber()
                # else:
                #     CheckLocalDb.insert_inquiry(samplingRegNumber, '4800804')  # There should be a CompanyCode information by API call from kefalab
                #     print(f"Inquiry number '{samplingRegNumber}' inserted successfully!'.")
                #     IlabAutomationSteps.ilab_automation_steps(self, samplingId, samplingRegNumber, samplings, sampling)
                else: print(f"Inquiry number '{samplingRegNumber}' does not exists for company '{companyCode}' which means There may not have been done InquiryProcess yet for this samplingRegNumber!.")
        
    def ilab_automation_steps(self, companyCode, samplingId, samplingRegNumber, samplings, sampling):

        iLabInquiryStatus = CheckLocalDb.check_ilab_status_forInquiry(companyCode, samplingRegNumber)
        if iLabInquiryStatus != "PENDING":
            IlabAutomationSteps.ilab_samplingProcess(self, companyCode, samplingId, samplingRegNumber, samplings, sampling)
        else:  print(f"Inquiry number '{samplingRegNumber}' has not been inquiried yet! First Process with Inquiry.")
        
        
    def ilab_samplingProcess(self, companyCode, samplingId, samplingRegNumber, samplings, sampling):

        iLabSamplingStatus = CheckLocalDb.check_ilab_status_forSampling(companyCode, samplingRegNumber)

        if iLabSamplingStatus == "PENDING":

            userCredentials = CheckLocalDb.get_user_details_by_company_code(companyCode)

            print(f"Starting automation for samplingRegNumber '{samplingRegNumber}' as the status is 'PENDING'.")
            iLab_path = Helper.ILAB_PATH
            user_code = userCredentials[0]  # OR Later Replace with API call ==> samplings[sampling].get('iLabUserCode')
            print(f"user_code: {user_code}")
            user_id = userCredentials[1]  # OR Later Replace with API call ==> samplings[sampling].get('iLabUserId')
            print(f"user_id: {user_id}")
            user_password = userCredentials[2]  # OR Later Replace with API call ==> samplings[sampling].get('iLabUserPassword')
            print(f"user_password: {user_password}")

            # Create an instance of the iLabAutomation class
            iLab = ILabAutomationProcesses(iLab_path, user_code, user_id, user_password)

            # Open the iLab app
            self.logger.info(f"ilab_automation_steps ==>: opening iLab application")
            iLab.open_ilab_app(iLab_path) 

            # Log into the app
            self.logger.info(f"ilab_automation_steps ==>: logging in iLab application")
            iLab.login_to_iLab(user_code, user_id, user_password)  

            # Navigate to the sampling page
            self.logger.info(f"ilab_automation_steps ==>: going to sampling page")
            iLab.go_to_sampling_page()  

            # Set search date for the inquiry
            self.logger.info(f"ilab_automation_steps ==>: setting the date")
            iLab.set_the_date()  

            # Search for the inquiry number
            self.logger.info(f"ilab_automation_steps ==>: searching for the inquiry number") 
            iLab.search_the_inquiry_number(samplingRegNumber) # Search for the inquiry number
            #iLab.search_the_inquiry_number("TTTTTTTT") 

            # Get screen inquiry number
            self.logger.info(f"ilab_automation_steps ==>: getting the desired inquiry number from the sampling screen") 
            screen_inquiry_number = iLab.get_inquiry_number_from_the_screen() 

            # Compare regNumber and inquiryNumber
            if screen_inquiry_number == samplingRegNumber:
                self.logger.info(f"ilab_automation_steps ==>: ilab_input_cells func is starting")
                ILabInputCells.ilab_mid_input_cells(self, iLab, samplings, sampling)

                self.logger.info(f"ilab_automation_steps ==>: apiCallForGaseousSteps func is starting")
                GaseousSteps.apiCallForGaseousSteps(self, iLab, samplingId, samplingRegNumber)

            else:
                Helper.show_auto_closing_message(" There might not be a comparable '접수번호'. 접수번호 not found! ", 2000)
                # Close ilab application
                self.logger.info(f"ilab_automation_steps ==>: there might not be a comparable '접수번호': {samplingRegNumber}. SamplingRegNumber-{samplingRegNumber} Not found on iLab Window!. Closing iLab app!")            
                iLab.close_ilab_app()
        # elif iLabSamplingStatus is None:
        #     print(f"[NONE VALUE] No matching samplingRegNumber '{samplingRegNumber}' found for company '{companyCode}'.")
        #     return
        else:
            print(f"Sampling Automation not started. Current status for samplingRegNumber '{samplingRegNumber}' is '{iLabSamplingStatus}'.")
            Helper.show_auto_closing_message(f"Current Inquiry has already been automated according to loacalDb iLab Status. iLab status is  {iLabSamplingStatus} for the inquiry number {samplingRegNumber}. Notifiying kefalab...") # removable later
            # Here if the iLabStatus equals to 'APPROVED' already, we need to add a API call to kefalab for updating the status of this samplingRegNumber
            # Notify to update the iLabStatus of automated samplingRegNumber
            
            self.logger.info(f"SamplingProcess has already been automated for the inquiry number {samplingRegNumber} according to loacalDb iLab Status. iLab samplingStatus is  {iLabSamplingStatus} for the inquiry number {samplingRegNumber}. Notifiying kefalab...")
            NotifyCompletion.notify_kefalab(self, samplingId)
            self.logger.info(f"Notify to update the iLabStatus of automated samplingRegNumber")
            time.sleep(3)           
            return


        
            
