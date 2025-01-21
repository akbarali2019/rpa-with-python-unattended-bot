from ilab_automation_localDb import CheckLocalDb
from .ecolab_notifyCompletion import EcolabNotifyCompletion
from iLab_automation_helper import Helper
from .ecolab_fileDownload import DownloadFiles
from iLab_automation_log import LoggerConfig
import time

STATUS_APPROVED = "APPROVED"
COMPANY_CODE = "4800804"

class EcolabWeb:

    def __init__(self):
        self.logger = LoggerConfig.setup_logger()

    def ecolab_automation_start(self, samplingId, samplingRegNumber, samplings, sampling, ecoLabAutos, driver):
        try:
            ecoLabAutos.close_alarm_dialog(driver)

            ecoLabAutos.click_sidebarMenu_subMenu(driver)
   
            date = Helper.safe_value(samplings[sampling].get('meaDay'))
            ecoLabAutos.input_search_date(driver, date)

            # Input the registration number
            ecoLabAutos.input_search_regNumber(driver, samplingRegNumber)

            # Wait for the canvas or grid to load => 접수번호 table row click
            ecoLabAutos.regNumber_based_mouseClick(driver)

            # measurement end date 
            meaEndDate = Helper.safe_value(samplings[sampling].get('meaDay'))
            ecoLabAutos.input_meaEndDate(driver, meaEndDate)

            # mea start time 측정시작시간
            meaStartTime = Helper.safe_value(samplings[sampling].get('meaStartTime'))
            meaStartTime = meaStartTime.replace(":","")
            ecoLabAutos.input_meaStartTime(driver, meaStartTime)

            # mea end time 측정종료시간
            meaEndTime = Helper.safe_value(samplings[sampling].get('meaEndTime'))
            meaEndTime = meaEndTime.replace(":","")
            ecoLabAutos.input_meaEndTime(driver, meaEndTime)

            # mea 날씨 weather
            meaWeather = Helper.safe_value(samplings[sampling].get('weather'))
            ecoLabAutos.input_meaWeather(driver, meaWeather)

            # mea 기온 (℃) temperature
            meaTemper = Helper.safe_value(samplings[sampling].get('temperature'))
            ecoLabAutos.input_meaTemper(driver, meaTemper)

            # mea 습도 (%) humidity
            meaHumidity = Helper.safe_value(samplings[sampling].get('humidity'))
            ecoLabAutos.input_meaHumidity(driver, meaHumidity)

            # mea  대기압 (mmHg) atmosphericPressure
            meaAtmosPress = Helper.safe_value(samplings[sampling].get('atmosphericPressure'))
            ecoLabAutos.input_meaAtmosPress(driver, meaAtmosPress)

            # mea 풍향 windDirection
            meaWindDir = Helper.safe_value(samplings[sampling].get('windDirection'))
            ecoLabAutos.input_meaWindDir(driver, meaWindDir)

            # mea 풍속 (m/s) windSpeed
            meaWindSpeed = Helper.safe_value(samplings[sampling].get('windSpeed'))
            ecoLabAutos.input_meaWindSpeed(driver, meaWindSpeed)

            # mea 표준산소농도(%) stdOxygen // basic_o2c
            meaStdOxygen = Helper.safe_value(samplings[sampling].get('stdOxygen'))
            ecoLabAutos.input_stdOxygen(driver, meaStdOxygen)

            # mea 배출가스량 (Sm³/min) emsGasAmount (산소보정 전)
            eGasAmount = Helper.safe_value(samplings[sampling].get('emsGasAmount'))
            ecoLabAutos.input_eGasAmount(driver, eGasAmount)
                       
            
            # mea 배출가스량 (Sm³/min) emsGasAmount (산소보정 후)
            gas_stdOxygenEqvAmount = Helper.safe_value(samplings[sampling].get('stdOxygenEqvAmount'))
            ecoLabAutos.input_stdOxygenEqvAmount(driver, gas_stdOxygenEqvAmount)
            
            
            # mea 측정 O2 (%) measureO2
            measureO2 = Helper.safe_value(samplings[sampling].get('measureO2'))
            ecoLabAutos.input_measureO2(driver, measureO2)

            # mea 배출가스온도(℃) emsGasTempAvg
            eGasTempAvg = Helper.safe_value(samplings[sampling].get('emsGasTempAvg'))
            ecoLabAutos.input_eGasTempAvg(driver, eGasTempAvg)

            # mea 수분량(%) mositureAmount
            mositureAmount = Helper.safe_value(samplings[sampling].get('moistureAmount'))
            ecoLabAutos.input_mositureAmount(driver, mositureAmount)

            # mea 배출가스 유속 (m/s) emsGasFlowSpeed
            eGasFlowSpeed = Helper.safe_value(samplings[sampling].get('emsGasFlowSpeed'))
            ecoLabAutos.input_eGasFlowSpeed(driver, eGasFlowSpeed)

            # mea 채취자 의견 meaOpinion
            meaOpinion = Helper.safe_value(samplings[sampling].get('meaOpinion'))
            ecoLabAutos.input_meaOpinion(driver, meaOpinion)

            # mea samplingMemo 채취정보 메모
            meaMemo = Helper.safe_value(samplings[sampling].get('samplingMemo'))
            ecoLabAutos.input_meaMemo(driver, meaMemo)

            # download fiels from kefalab.com via API call
            api_base_url = "https://kefalab.com/api/v1/files/rpa/download"
            DownloadFiles.fileDownloadByAPI(self, api_base_url, samplingId)
            
            #Path to the folder containing files
            FOLDER_PATH = DownloadFiles.get_docs_folder(self)
            print(f"Ecolab upload_files DOCS FOLDER PATH: {FOLDER_PATH}")
            ecoLabAutos.upload_files(driver, FOLDER_PATH)

            # Trigger the click event directly with JavaScript to temp save
            ecoLabAutos.temp_save(driver)

            # Local DB Update
            CheckLocalDb.update_ecolabStatus(samplingRegNumber, STATUS_APPROVED, COMPANY_CODE)

            # kefalab status Update of the desired samplingId
            EcolabNotifyCompletion.ecolab_notify_kefalab(self, samplingId)

        except Exception as e:
            self.logger.warning(f"Error inside ecolab_automation_start() function: {e}")
            EcolabNotifyCompletion.ecolab_fail_notify_kefalab(self, samplingId)
            time.sleep(0.5)
            return
