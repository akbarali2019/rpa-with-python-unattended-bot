from comtypes import stream
from iLab_automation_start import StartILabAutomation

def main():

    # Create an instance of the StarILabAutomation class
    startILab = StartILabAutomation()
    startILab.start_iLab_automation() 
                    
 
if __name__ == '__main__':
    main()                  