from .iLab_inquiry_apiCall import InquiryAPI
def main():

    # Create an instance of the StarILabAutomation class
    print("Create an instance of the StarILabAutomation class")
    start_iLab = InquiryAPI()
    start_iLab.inquiry_apiCall()
                    
 
if __name__ == '__main__':
    main()  
