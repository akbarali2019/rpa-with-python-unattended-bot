import requests
import pyautogui
import time
import pyperclip
from iLab_automation_helper import Helper
from iLab_automation_log import LoggerConfig
from iLab_automation_notifiyCompletion import NotifyCompletion
from ilab_automation_checkLocalDbStatusOfSamplingRegNumber import CheckLocalDbStatus

DEALY_TIME = 0.005
class GaseousSteps:

    def __init__(self):
        self.logger = LoggerConfig.setup_logger()

    def apiCallForGaseousSteps(self, iLab, samplingId, samplingRegNum):
        gaseousUrl = f""
        self.logger.info(f"apiCallForGaseousSteps ==> Call for api: {gaseousUrl} to get iLab sampling gaseous data")
        print(f"Gaseous Url: {gaseousUrl}")
        gaseousResponse = requests.get(gaseousUrl)

        if gaseousResponse.status_code == 200:
            gaseousData = gaseousResponse.json()          
            totalItemElements = gaseousData.get('totalItemElements')
            self.logger.info(f"apiCallForGaseousSteps ==> api call was successfull! Total Elements: {totalItemElements}")
            self.logger.info(gaseousData)
            print(gaseousData)
            print(f"Total Item Elements: {totalItemElements}")
            
            if totalItemElements != 0:
                    # Mouse Click to Order "항목명"
                    self.logger.info(f"apiCallForGaseousSteps ==> Mouse Click to Order 항목명") 
                    pyautogui.moveTo(453, 1113)
                    pyautogui.click() # 항목명
                    time.sleep(DEALY_TIME)

                    # Get to desired position of the table box of the ilab screen to check and input gaseous items values
                    self.logger.info(f"apiCallForGaseousSteps ==> Get to desired position of the table box of the ilab screen to check and input gaseous items values")  
                    pyautogui.press('right')
                    time.sleep(DEALY_TIME)
                    
                    # Iteration over exsiting Items
                    for item in gaseousData['gaseous']:
                        
                        # Copy item to check item is a gas item
                        self.logger.info(f"apiCallForGaseousSteps ==> Copy item to check item is a gas item")  
                        pyautogui.hotkey('ctrl', 'c')
                        time.sleep(0.05)
                        iLab_current_item = pyperclip.paste()
                        print(f"=====> ILAB Current Item: {iLab_current_item}")
                        time.sleep(DEALY_TIME)                     
                        kefa_item_byApi = item['pollutantType']
                        print(f"=====> API KEFA Item: {kefa_item_byApi}")
                        self.logger.info(f"apiCallForGaseousSteps ==> ILAB Current Item: {iLab_current_item} -- API KEFA Item: {kefa_item_byApi}")

                        if kefa_item_byApi == '가스상' and iLab_current_item == '가스상':

                            # Get iLab Sampling stdOxygenState value from .json after API call to kefalab.com and set val
                            self.logger.info(f"apiCallForGaseousSteps ==> Get iLab Sampling stdOxygenState value from .json after API call to kefalab.com and set val")  
                            stdOxygenState = Helper.safe_value(item.get('stdOxygenState'))
                            iLab.set_stdOxygenState(stdOxygenState)

                            # Get iLab Sampling collectionTime value from .json after API call to kefalab.com and set val
                            self.logger.info(f"apiCallForGaseousSteps ==> Get iLab Sampling collectionTime value from .json after API call to kefalab.com and set val")  
                            collectionTime = Helper.safe_value(item.get('collectionTime'))
                            iLab.set_collectionTime(collectionTime)

                            # Get iLab Sampling fieldMeasuredDensity value from .json after API call to kefalab.com and set val
                            self.logger.info(f"apiCallForGaseousSteps ==> Get iLab Sampling fieldMeasuredDensity value from .json after API call to kefalab.com and set val")  
                            fieldMeasuredDensity = Helper.safe_value(item.get('fieldMeasuredDensity'))
                            iLab.set_fieldMeasuredDensity(fieldMeasuredDensity)

                            # Get iLab Sampling suctionPipeNumber value from .json after API call to kefalab.com and set val
                            self.logger.info(f"apiCallForGaseousSteps ==> Get iLab Sampling suctionPipeNumber value from .json after API call to kefalab.com and set val") 
                            suctionPipeNumber = Helper.safe_value(item.get('suctionPipeNumber'))
                            iLab.set_suctionPipeNumber(suctionPipeNumber)

                            # Get iLab Sampling gasMeterTemp value from .json after API call to kefalab.com and set val
                            self.logger.info(f"apiCallForGaseousSteps ==> Get iLab Sampling gasMeterTemp value from .json after API call to kefalab.com and set val") 
                            gasMeterTemp = Helper.safe_value(item.get('gasMeterTemp'))
                            iLab.set_gasMeterTemp(gasMeterTemp)

                            # Get iLab Sampling gaugePressureHg value from .json after API call to kefalab.com and set val
                            self.logger.info(f"apiCallForGaseousSteps ==> Get iLab Sampling gaugePressureHg value from .json after API call to kefalab.com and set val")
                            gaugePressureHg = Helper.safe_value(item.get('gaugePressureHg'))
                            iLab.set_gaugePressureHg(gaugePressureHg)

                            # Get iLab Sampling gasVolumeResult value from .json after API call to kefalab.com and set val
                            self.logger.info(f"apiCallForGaseousSteps ==> Get iLab Sampling gasVolumeResult value from .json after API call to kefalab.com and set val")
                            gasVolumeResult = Helper.safe_value(item.get('gasVolumeResult'))
                            iLab.set_gasVolumeResult(gasVolumeResult)

                            # Get iLab Sampling calibratedGasAmount value from .json after API call to kefalab.com and set val
                            self.logger.info(f"apiCallForGaseousSteps ==> Get iLab Sampling calibratedGasAmount value from .json after API call to kefalab.com and set val")
                            calibratedGasAmount = Helper.safe_value(item.get('calibratedGasAmount'))
                            iLab.set_calibratedGasAmount(calibratedGasAmount)

                            # Back to beinning of the cell
                            self.logger.info(f"apiCallForGaseousSteps ==> Back to beinning of the cell")
                            pyautogui.press('down')
                            pyautogui.press('left', 9)
                            time.sleep(DEALY_TIME)

                        else:
                                # Back to the desired starting celll of ilab sampling gasbox
                                self.logger.info(f"apiCallForGaseousSteps ==> Either kefa_item_byApi or iLab_current_item is NOT EQUAL to '가스상'. Back to the desired starting celll of ilab sampling gasbox")
                                pyautogui.press('down')
                                time.sleep(DEALY_TIME)
            
            # Calculate and save results
            self.logger.info(f"apiCallForGaseousSteps ==> Calculate and save results")            
            iLab.calculate_and_save_inputVals()
            time.sleep(3)

            # Close ilab application
            self.logger.info(f"apiCallForGaseousSteps ==> Closing iLab app")             
            iLab.close_ilab_app()
            #time.sleep(3)          
            
            # Update the iLabStatus of automated samplingRegNumber in the local automation_db
            CheckLocalDbStatus.update_inquiry_status(samplingRegNum, 'APPROVED', '4800804')
            time.sleep(3) 

            # Notify to update the iLabStatus of automated samplingRegNumber
            self.logger.info(f"Notify to update the iLabStatus of automated samplingRegNumber")
            NotifyCompletion.notify_kefalab(self, samplingId)
        else:
             self.logger.warning(f"apiCallForGaseousSteps ==> API Call for {gaseousUrl} Failed. Response: {gaseousResponse.text}")
             # Close ilab application
             self.logger.info(f"apiCallForGaseousSteps ==> Closing iLab app")           
             iLab.close_ilab_app()
             # HERE BEFORE CLOSING ILAB APP, IT ASKS TO SAVE THE INOUT VALUES OR NOT VIA SHOWING UP POP UP
             # CONSIDERING THIS WE SHOULD DEVELOP A LOGIC FOR THIS SPECIFIC CASE 
             # SHOWUP POPUP => TAB+ENTER+TAB+ENTER
             iLab.popup_window_cancelToSave() 
             time.sleep(2)
