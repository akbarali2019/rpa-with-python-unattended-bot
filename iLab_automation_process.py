
import pyautogui
import pyperclip
import time
from pywinauto.application import Application
import subprocess

 # Set the desired delay time FOR ONLY AFTER "TAB" ACTIONS
DELAY_TIME = 0 

class ILabAutomationProcesses:

    def __init__(self, iLab_path, user_code, user_id, user_password):
        self.iLab_path = iLab_path
        self.user_code = user_code
        self.user_id = user_id
        self.user_password = user_password
        self.app = None

    # Open iLab Application
    def open_ilab_app(self, iLab_path):
        app = Application(backend='uia').start(iLab_path)
        time.sleep(3)

    # User Login
    def login_to_iLab(self,user_code, user_id, user_password):
        #user_code = "64" # need to receive from API Call
        #user_id = "알리" # need to receive from API Call
        #user_password = "35152510" # need to receive from API Call
        pyautogui.press('tab', 5)
        pyautogui.write(user_code)
        pyautogui.press('tab')
        pyautogui.write(user_id) 
        pyautogui.press('tab')
        pyautogui.write(user_password)
        pyautogui.press('tab')                      
        pyautogui.press('enter')
        time.sleep(3) # do not decrease

    # Go to Sampling Page
    def go_to_sampling_page(self):
        pyautogui.press('alt')
        pyautogui.press('right', 3)
        pyautogui.press('enter')                       
        pyautogui.press('down', 4)
        pyautogui.press('enter')
        time.sleep(0.05) # do not decrease

    # Set the date
    def set_the_date(self):        
        pyautogui.press('tab')
        pyautogui.press('del')
        pyautogui.press('tab')
        pyautogui.press('del')
        time.sleep(0.05)

    # Search the "접수번호" - samplingId
    def search_the_inquiry_number(self, inquiryNum):
        pyautogui.press('tab')
        pyautogui.write(inquiryNum, 0.05)
        pyautogui.press('enter')
        time.sleep(5) # do not decrease

    # Mouse Click to check for "접수번호"
    def get_inquiry_number_from_the_screen(self):
        pyautogui.moveTo(541, 361) # 접수번호
        pyautogui.click()
        pyautogui.hotkey('ctrl', 'c')
        time.sleep(0.5) # do not decrease
        inquiry_number = pyperclip.paste()
        print(f"Current Inquiry Number: {inquiry_number}")
        time.sleep(0.5) # do not decrease
        return inquiry_number
    
    # API Call input "지점수" - score
    def set_score(self, score):
        pyautogui.press('tab', 2) 
        pyautogui.write(score) # score
        time.sleep(DELAY_TIME)

    # Mouse Click to tick Checkbox for "지점수 직접입력"
    def mouse_click_to_tick_scorebox(self):
        pyautogui.moveTo(1261, 418)
        pyautogui.click() # 지점수 직접입력
        time.sleep(DELAY_TIME)

    # API Call input ""채취자의견"" - meaOpinion
    def set_meaOpinion(self, meaOpinion):
        pyautogui.press('tab')
        time.sleep(1)
        pyperclip.copy(meaOpinion) # meaOpinion
        time.sleep(0.05) 
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(DELAY_TIME)
    
    # API Call input "채취시간" - meaStartTime/meaEndTime
    def set_meaStartTime_meaEndTime(self, meaStartTime, meaEndTime):
        pyautogui.press('tab') 
        pyautogui.write(meaStartTime) # meaStartTime
        time.sleep(DELAY_TIME)
        pyautogui.press('tab') 
        pyautogui.write(meaEndTime) # meaEndTime
        time.sleep(DELAY_TIME)

    # API Call input "노즐직경" - exposureDiameter
    def set_exposureDiameter(self, exposureDiameter):
        pyautogui.press('tab') 
        pyautogui.write(exposureDiameter) # exposureDiameter
        time.sleep(DELAY_TIME)

    # API Call input "여과지번호" - filterPaper
    def set_filterPaper(self, filterPaper):
        pyautogui.press('tab') 
        pyperclip.copy(filterPaper) # filterPaper
        time.sleep(0.05) # do not decrease
        pyautogui.hotkey('ctrl', 'v')  

    # API Call input "날씨" - weather
    def set_weather(self, weather):
        pyautogui.press('tab') 
        pyperclip.copy(weather) # weather
        time.sleep(0.05) # do not decrease
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.press('enter')   
         
    # API Call input "기온(C)" - temperature
    def set_temperature(self, temperature):        
        pyautogui.press('tab') 
        pyautogui.write(temperature) # temperature
        time.sleep(DELAY_TIME)

    # API Call input "습도(%)" - humidity
    def set_humidity(self, humidity):
        pyautogui.press('tab') 
        pyautogui.write(humidity) # humidity
        time.sleep(DELAY_TIME)
    
    # API Call input "지압(mmHg)" - atmosphericPressure
    def set_atmosphericPressure(self, atmosphericPressure):
        pyautogui.press('tab') 
        pyautogui.write(atmosphericPressure) # atmosphericPressure
        time.sleep(DELAY_TIME)

    # API Call input "풍향" - windDirection
    def set_windDirection(self, windDirection):
        pyautogui.press('tab') 
        pyperclip.copy(windDirection) # windDirection
        time.sleep(0.05)
        pyautogui.hotkey('ctrl', 'v')  
        
    # API Call input "풍속(m/s)" - windSpeed
    def set_windSpeed(self, windSpeed):
        pyautogui.press('tab') 
        pyautogui.write(windSpeed) # windSpeed
        time.sleep(DELAY_TIME)

    # API Call input "측정O2 (%)" - measureO2
    def set_measureO2(self, measureO2):
        pyautogui.press('tab') 
        pyautogui.write(measureO2) # measureO2
        time.sleep(DELAY_TIME)

    # API Call input "측정CO2 (%)" - measureCO2
    def set_measureCO2(self, measureCO2):
        pyautogui.press('tab') 
        pyautogui.write(measureCO2) # measureCO2
        time.sleep(DELAY_TIME)

    # API Call input "가스미터(m3) 채취전/채취후" - gasMeterCollBefore/gasMeterCollAfter
    def set_gasMeterCollBeforeAndAfter(self, gasMeterCollBefore, gasMeterCollAfter):
        pyautogui.press('tab', 2) 
        pyautogui.write(gasMeterCollBefore) # gasMeterCollBefore
        time.sleep(DELAY_TIME)
        pyautogui.press('tab') 
        pyautogui.write(gasMeterCollAfter) # gasMeterCollAfter
        time.sleep(DELAY_TIME)
    
    # API Call input "흡인가스 유량 (L/min)" - suctionGasFlowRate
    def set_suctionGasFlowRate(self, suctionGasFlowRate):
        pyautogui.press('tab', 2) 
        pyautogui.write(suctionGasFlowRate) # suctionGasFlowRate
        time.sleep(DELAY_TIME)

    # API Call input "흡인가스량 (L)" - suctionGasAmount
    def set_suctionGasAmount(self, suctionGasAmount):
        pyautogui.press('tab') 
        pyautogui.write(suctionGasAmount) # suctionGasAmount
        time.sleep(DELAY_TIME)

    # API Call input "가스미터온도(C')" - gasMeterTemp
    def set_aboveGasMeterTemp(self, gasMeterTemp):
        pyautogui.press('tab')
        pyautogui.write(gasMeterTemp) # gasMeterTemp
        time.sleep(DELAY_TIME)

    # API Call input "가스 게이지압 (mmHg)" - gaugePressureHg
    def set_aboveGaugePressureHg(self, gaugePressureHg):
        pyautogui.press('tab') 
        pyautogui.write(gaugePressureHg) # gaugePressureHg
        time.sleep(DELAY_TIME)

    # API Call input "수분 무게 (전) ma1(g)"   (후) ma2(g)" - moistureBefore1, moistureAfter1, moistureBefore2, moistureAfter2
    def set_moistures(self, moistureBefore1, moistureAfter1, moistureBefore2, moistureAfter2):
        pyautogui.press('tab') 
        pyautogui.write(moistureBefore1) # moistureBefore1
        time.sleep(DELAY_TIME)
        pyautogui.press('tab') 
        pyautogui.write(moistureAfter1) # moistureAfter1
        time.sleep(DELAY_TIME)
        pyautogui.press('tab') 
        pyautogui.write(moistureBefore2) # moistureBefore2
        time.sleep(DELAY_TIME)
        pyautogui.press('tab') 
        pyautogui.write(moistureAfter2) # moistureAfter2
        time.sleep(DELAY_TIME)

    # Set input values for ilab sampling page middle raw1
    def set_inputMiddleRaw1(self,particulateTime1,vacuumPressure1,emsGasTemp1,staticPressure1,dynamicPressure1,sampleVolumeMeter1,gasMeterTempIn1,gasMeterTempOut1,filterPaperTemp1,impingerTemp1,meaPoint1,w1,h1):
        pyautogui.press('tab') 
        pyautogui.write(particulateTime1) # particulateTime1
        time.sleep(DELAY_TIME)

        pyautogui.press('tab') 
        pyautogui.write(vacuumPressure1) # vacuumPressure1
        time.sleep(DELAY_TIME)

        pyautogui.press('tab') 
        pyautogui.write(emsGasTemp1) # emsGasTemp1
        time.sleep(DELAY_TIME)

        pyautogui.press('tab') 
        pyautogui.write(staticPressure1) # staticPressure1
        time.sleep(DELAY_TIME)

        pyautogui.press('tab') 
        pyautogui.write(dynamicPressure1) # dynamicPressure1
        time.sleep(DELAY_TIME)

        pyautogui.press('tab') 
        pyautogui.write(sampleVolumeMeter1) # sampleVolumeMeter1
        time.sleep(DELAY_TIME)

        pyautogui.press('tab', 2) 
        pyautogui.write(gasMeterTempIn1) # gasMeterTempIn1
        time.sleep(DELAY_TIME)

        pyautogui.press('tab') 
        pyautogui.write(gasMeterTempOut1) # gasMeterTempOut1
        time.sleep(DELAY_TIME)

        pyautogui.press('tab', 2) 
        pyautogui.write(filterPaperTemp1) # filterPaperTemp1
        time.sleep(DELAY_TIME)

        pyautogui.press('tab') 
        pyautogui.write(impingerTemp1) # impingerTemp1
        time.sleep(DELAY_TIME)

        pyautogui.press('tab') 
        pyautogui.write(meaPoint1) # meaPoint1
        time.sleep(DELAY_TIME)

        pyautogui.press('tab') 
        pyautogui.write(w1) # w1
        time.sleep(DELAY_TIME)

        pyautogui.press('tab') 
        pyautogui.write(h1) # h1
        time.sleep(DELAY_TIME)

    # Set input values for ilab sampling page middle raw2
    def set_inputMiddleRaw2(self,particulateTime2,vacuumPressure2,emsGasTemp2,staticPressure2,dynamicPressure2,sampleVolumeMeter2,gasMeterTempIn2,gasMeterTempOut2,filterPaperTemp2,impingerTemp2,meaPoint2,w2,h2):
        pyautogui.press('tab') 
        pyautogui.write(particulateTime2) # particulateTime2
        time.sleep(DELAY_TIME)

        pyautogui.press('tab') 
        pyautogui.write(vacuumPressure2) # vacuumPressure2
        time.sleep(DELAY_TIME)

        pyautogui.press('tab') 
        pyautogui.write(emsGasTemp2) # emsGasTemp2
        time.sleep(DELAY_TIME)

        pyautogui.press('tab') 
        pyautogui.write(staticPressure2) # staticPressure2
        time.sleep(DELAY_TIME)

        pyautogui.press('tab') 
        pyautogui.write(dynamicPressure2) # dynamicPressure2
        time.sleep(DELAY_TIME)

        pyautogui.press('tab') 
        pyautogui.write(sampleVolumeMeter2) # sampleVolumeMeter2
        time.sleep(DELAY_TIME)

        pyautogui.press('tab') 
        pyautogui.write(gasMeterTempIn2) # gasMeterTempIn2
        time.sleep(DELAY_TIME)

        pyautogui.press('tab') 
        pyautogui.write(gasMeterTempOut2) # gasMeterTempOut2
        time.sleep(DELAY_TIME)

        pyautogui.press('tab', 2) 
        pyautogui.write(filterPaperTemp2) # filterPaperTemp2
        time.sleep(DELAY_TIME)

        pyautogui.press('tab') 
        pyautogui.write(impingerTemp2) # impingerTemp2
        time.sleep(DELAY_TIME)

        pyautogui.press('tab') 
        pyautogui.write(meaPoint2) # meaPoint2
        time.sleep(DELAY_TIME)

        pyautogui.press('tab') 
        pyautogui.write(w2) # w2
        time.sleep(DELAY_TIME)

        pyautogui.press('tab') 
        pyautogui.write(h2) # h2
        time.sleep(DELAY_TIME)

    # Set input values for ilab sampling page middle raw3
    def set_inputMiddleRaw3(self,particulateTime3,vacuumPressure3,emsGasTemp3,staticPressure3,dynamicPressure3,sampleVolumeMeter3,gasMeterTempIn3,gasMeterTempOut3,filterPaperTemp3,impingerTemp3,meaPoint3,w3,h3):

        pyautogui.press('tab') 
        pyautogui.write(particulateTime3) # particulateTime3
        time.sleep(DELAY_TIME)

        pyautogui.press('tab') 
        pyautogui.write(vacuumPressure3) # vacuumPressure3
        time.sleep(DELAY_TIME)

        pyautogui.press('tab') 
        pyautogui.write(emsGasTemp3) # emsGasTemp3
        time.sleep(DELAY_TIME)

        pyautogui.press('tab') 
        pyautogui.write(staticPressure3) # staticPressure3
        time.sleep(DELAY_TIME)

        pyautogui.press('tab') 
        pyautogui.write(dynamicPressure3) # dynamicPressure3
        time.sleep(DELAY_TIME)

        pyautogui.press('tab') 
        pyautogui.write(sampleVolumeMeter3) # sampleVolumeMeter3
        time.sleep(DELAY_TIME)

        pyautogui.press('tab') 
        pyautogui.write(gasMeterTempIn3) # gasMeterTempIn3
        time.sleep(DELAY_TIME)

        pyautogui.press('tab') 
        pyautogui.write(gasMeterTempOut3) # gasMeterTempOut3
        time.sleep(DELAY_TIME)

        pyautogui.press('tab') 
        pyautogui.write(filterPaperTemp3) # filterPaperTemp3
        time.sleep(DELAY_TIME)

        pyautogui.press('tab') 
        pyautogui.write(impingerTemp3) # impingerTemp3
        time.sleep(DELAY_TIME)

        pyautogui.press('tab') 
        pyautogui.write(meaPoint3) # meaPoint3
        time.sleep(DELAY_TIME)

        pyautogui.press('tab') 
        pyautogui.write(w3) # w3
        time.sleep(DELAY_TIME)

        pyautogui.press('tab') 
        pyautogui.write(h3) # h3
        time.sleep(DELAY_TIME)

    # Set input values for ilab sampling page middle raw4
    def set_inputMiddleRaw4(self,particulateTime4,vacuumPressure4,emsGasTemp4,staticPressure4,dynamicPressure4,sampleVolumeMeter4,gasMeterTempIn4,gasMeterTempOut4,filterPaperTemp4,impingerTemp4,meaPoint4,w4,h4):

        pyautogui.press('tab') 
        pyautogui.write(particulateTime4) # particulateTime4
        time.sleep(DELAY_TIME)

        pyautogui.press('tab') 
        pyautogui.write(vacuumPressure4) # vacuumPressure4
        time.sleep(DELAY_TIME)

        pyautogui.press('tab') 
        pyautogui.write(emsGasTemp4) # emsGasTemp4
        time.sleep(DELAY_TIME)

        pyautogui.press('tab') 
        pyautogui.write(staticPressure4) # staticPressure4
        time.sleep(DELAY_TIME)

        pyautogui.press('tab') 
        pyautogui.write(dynamicPressure4) # dynamicPressure4
        time.sleep(DELAY_TIME)

        pyautogui.press('tab') 
        pyautogui.write(sampleVolumeMeter4) # sampleVolumeMeter4
        time.sleep(DELAY_TIME)

        pyautogui.press('tab') 
        pyautogui.write(gasMeterTempIn4) # gasMeterTempIn4
        time.sleep(DELAY_TIME)

        pyautogui.press('tab') 
        pyautogui.write(gasMeterTempOut4) # gasMeterTempOut4
        time.sleep(DELAY_TIME)

        pyautogui.press('tab') 
        pyautogui.write(filterPaperTemp4) # filterPaperTemp4
        time.sleep(DELAY_TIME)

        pyautogui.press('tab') 
        pyautogui.write(impingerTemp4) # impingerTemp4
        time.sleep(DELAY_TIME)

        pyautogui.press('tab') 
        pyautogui.write(meaPoint4) # meaPoint4
        time.sleep(DELAY_TIME)

        pyautogui.press('tab') 
        pyautogui.write(w4) # w4
        time.sleep(DELAY_TIME)

        pyautogui.press('tab') 
        pyautogui.write(h4) # h4
        time.sleep(DELAY_TIME)

    # Set input values for ilab sampling page middle raw5
    def set_inputMiddleRaw5(self,particulateTime5,vacuumPressure5,emsGasTemp5,staticPressure5,dynamicPressure5,sampleVolumeMeter5,gasMeterTempIn5,gasMeterTempOut5,filterPaperTemp5,impingerTemp5,meaPoint5,w5,h5):

        pyautogui.press('tab') 
        pyautogui.write(particulateTime5) # particulateTime5
        time.sleep(DELAY_TIME)

        pyautogui.press('tab') 
        pyautogui.write(vacuumPressure5) # vacuumPressure5
        time.sleep(DELAY_TIME)

        pyautogui.press('tab') 
        pyautogui.write(emsGasTemp5) # emsGasTemp5
        time.sleep(DELAY_TIME)

        pyautogui.press('tab') 
        pyautogui.write(staticPressure5) # staticPressure5
        time.sleep(DELAY_TIME)

        pyautogui.press('tab') 
        pyautogui.write(dynamicPressure5) # dynamicPressure5
        time.sleep(DELAY_TIME)

        pyautogui.press('tab') 
        pyautogui.write(sampleVolumeMeter5) # sampleVolumeMeter5
        time.sleep(DELAY_TIME)

        pyautogui.press('tab') 
        pyautogui.write(gasMeterTempIn5) # gasMeterTempIn5
        time.sleep(DELAY_TIME)

        pyautogui.press('tab') 
        pyautogui.write(gasMeterTempOut5) # gasMeterTempOut5
        time.sleep(DELAY_TIME)

        pyautogui.press('tab') 
        pyautogui.write(filterPaperTemp5) # filterPaperTemp5
        time.sleep(DELAY_TIME)

        pyautogui.press('tab') 
        pyautogui.write(impingerTemp5) # impingerTemp5
        time.sleep(DELAY_TIME)

        pyautogui.press('tab') 
        pyautogui.write(meaPoint5) # meaPoint5
        time.sleep(DELAY_TIME)

        pyautogui.press('tab') 
        pyautogui.write(w5) # w5
        time.sleep(DELAY_TIME)

        pyautogui.press('tab') 
        pyautogui.write(h5) # h5
        time.sleep(DELAY_TIME)

    # Input for 매연 - smoke    
    def set_smoke(self, smoke):
        pyautogui.press('tab', 3) 
        pyautogui.write(smoke) # smoke
        pyautogui.press('enter') 
        time.sleep(DELAY_TIME)
    
    # API Call input "접수메모2" - samplingMemo
    def set_samplingMemo(self, samplingMemo):
        pyperclip.copy(samplingMemo) # samplingMemo
        time.sleep(0.05) # do not decrease
        pyautogui.press('tab', 2) 
        pyautogui.hotkey('ctrl', 'v')

    #AsCol.1 Input for "표준산소사용여부" - stdOxygenState
    def set_stdOxygenState(self, stdOxygenState):
        pyautogui.press('right', 2)
        pyautogui.write(stdOxygenState) # stdOxygenState
        time.sleep(DELAY_TIME)

    #AsCol.2 Input for "채취시간" - collectionTime
    def set_collectionTime(self, collectionTime):
        pyautogui.press('right')
        pyautogui.write(collectionTime) # collectionTime
        time.sleep(DELAY_TIME)

    #AsCol.3 Input for "보정된 시료 가스 채취량(L)" - calibratedGasAmount
    def set_calibratedGasAmount(self, calibratedGasAmount):
        pyautogui.press('right')
        pyautogui.write(calibratedGasAmount) # calibratedGasAmount
        time.sleep(DELAY_TIME)

    #AsCol.4 Input for "시료가스채취량(L)" - gasVolumeResult
    def set_gasVolumeResult(self, gasVolumeResult):
        pyautogui.press('right')
        pyautogui.write(gasVolumeResult) # gasVolumeResult
        time.sleep(DELAY_TIME)

    #AsCol.5 Input for "가스게이지압(mmHg)" - gaugePressureHg
    def set_gaugePressureHg(self, gaugePressureHg):
        pyautogui.press('right')
        pyautogui.write(gaugePressureHg) # gaugePressureHg
        time.sleep(DELAY_TIME)
    
    #AsCol.6 Input for "가스미터온도(C)" - gasMeterTemp
    def set_gasMeterTemp(self, gasMeterTemp):
        pyautogui.press('right')
        pyautogui.write(gasMeterTemp) # gasMeterTemp
        time.sleep(DELAY_TIME)

    #AsCol.7 Input for "현장측정농도(ppm)" - fieldMeasuredDensity
    def set_fieldMeasuredDensity(self, fieldMeasuredDensity):
        pyautogui.press('right')
        pyautogui.write(fieldMeasuredDensity) #  fieldMeasuredDensity
        time.sleep(DELAY_TIME)

    #AsCol.8 Input for "흡착관번호" - suctionPipeNumber
    def set_suctionPipeNumber(self, suctionPipeNumber):
        pyautogui.press('right')
        pyautogui.write(suctionPipeNumber) # suctionPipeNumber
        time.sleep(DELAY_TIME)

    # Calculate and Save result
    def calculate_and_save_inputVals(self):
        pyautogui.press('up')
        pyautogui.press('tab', 3)
        pyautogui.press('enter') # for calculation
        time.sleep(2) # do not decrease
        pyautogui.press('right', 2)
        pyautogui.press('enter') # for save
        time.sleep(5) # do not decrease
    
    # Close iLab Application
    def close_ilab_app(self):
        subprocess.call("taskkill /F /IM iLabApp.exe", shell=True)

    # Reject to save in case Pop Up window show up
    def popup_window_cancelToSave(self):
        pyautogui.press('tab')
        pyautogui.press('enter') # approve not to save input results
        pyautogui.press('tab')
        pyautogui.press('enter') # approve not to save input results