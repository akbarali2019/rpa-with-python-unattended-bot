from iLab_automation_log import LoggerConfig
from iLab_automation_helper import Helper
from ilab_automation_localDb import CheckLocalDb
from Inquiry.iLab_inquiry_process import InquiryProcess

INQUIRY_COMPLETED_STATUS = "APPROVED"
MESSAGE_INQUIRY_COMPLETED = "Inquiry number '{}' has already been inquired. iLabInquiryStatus is '{}'."
MESSAGE_INQUIRY_PROCESSING = "Inquiry number '{}' is going to be automated. iLabInquiryStatus is '{}'."

class StartILabInquiry:
    def __init__(self):
        self.logger = LoggerConfig.setup_logger()

    def inquiryProcess_dbCheck(self, data, iLab, companyCode):
        """Check inquiries in local DB and process them if necessary."""
        inquiries = data.get('inquiries', [])
        number_of_inquiries = len(inquiries)

        self.logger.info(f"Number of inquiries: {number_of_inquiries}")
        print(f"NUMBER OF INQUIRIES: {number_of_inquiries}")

        for inquiry_data in inquiries:
            self._process_single_inquiry(inquiry_data, iLab, companyCode)

    def _process_single_inquiry(self, inquiry_data, iLab, companyCode):
        """Handle a single inquiry based on its DB status."""
        inquiry_sampling_id = inquiry_data.get('samplingId')
        inquiry_sampling_reg_number = inquiry_data.get('samplingRegNumber')

        self.logger.info(f"Processing inquirySamplingId: {inquiry_sampling_id}, "
                         f"inquirySamplingRegNumber: {inquiry_sampling_reg_number}")
        print(f"inquirySamplingId: {inquiry_sampling_id}, inquirySamplingRegNumber: {inquiry_sampling_reg_number}")

        try:
            if CheckLocalDb.check_inquiry_exists_for_company(inquiry_sampling_reg_number, companyCode):
                self._handle_existing_inquiry(
                    inquiry_sampling_id, inquiry_sampling_reg_number, companyCode, inquiry_data, iLab
                )
            else:
                CheckLocalDb.insert_inquiry(inquiry_sampling_reg_number, companyCode)
                self.logger.info(f"Inserted new inquiry: {inquiry_sampling_reg_number}")
                print(f"Inquiry '{inquiry_sampling_reg_number}' inserted successfully.")
                self.work_on_inquiry(companyCode, inquiry_sampling_reg_number, inquiry_sampling_id, inquiry_data, iLab)
        except Exception as e:
            self.logger.error(f"Error processing inquiry {inquiry_sampling_reg_number}: {e}")
            print(f"Error: {e}")

    def _handle_existing_inquiry(self, inquiry_sampling_id, inquiry_sampling_reg_number, companyCode, inquiry_data, iLab):
        """Handle inquiries that already exist in the local DB."""
        iLab_inquiry_status = CheckLocalDb.check_ilab_status_forInquiry(companyCode, inquiry_sampling_reg_number)

        if iLab_inquiry_status != INQUIRY_COMPLETED_STATUS:
            self.logger.info(MESSAGE_INQUIRY_PROCESSING.format(inquiry_sampling_reg_number, iLab_inquiry_status))
            print(MESSAGE_INQUIRY_PROCESSING.format(inquiry_sampling_reg_number, iLab_inquiry_status))
            self.work_on_inquiry(companyCode, inquiry_sampling_reg_number, inquiry_sampling_id, inquiry_data, iLab)
        else:
            self.logger.info(MESSAGE_INQUIRY_COMPLETED.format(inquiry_sampling_reg_number, iLab_inquiry_status))
            print(MESSAGE_INQUIRY_COMPLETED.format(inquiry_sampling_reg_number, iLab_inquiry_status))
            Helper.show_auto_closing_message(
                f"Inquiry number '{inquiry_sampling_reg_number}' already processed. Status: {iLab_inquiry_status}."
            )
            InquiryProcess.update_kefalab_inquiryStatus(self, inquiry_sampling_id)

    def work_on_inquiry(self, companyCode, inquiryNumber, inquirySamplingId, inquiryData, iLab):
        """Perform the automation process for an inquiry."""
        try:
            iLab.open_iLabInquiry_page()
            InquiryProcess.get_set_inquiry_values(self, iLab, inquiryNumber, inquiryData)
            iLab.close_iLabSubwindows()
            CheckLocalDb.update_inquiryStatus(inquiryNumber, INQUIRY_COMPLETED_STATUS, companyCode)
            InquiryProcess.update_kefalab_inquiryStatus(self, inquirySamplingId)
        except Exception as e:
            self.logger.error(f"Error automating inquiry {inquiryNumber}: {e}")
            print(f"Automation error for inquiry {inquiryNumber}: {e}")
