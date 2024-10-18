
from iLab_automation_helper import Helper
from iLab_automation_log import LoggerConfig

class ILabInputCells:

    def __init__(self):
        self.logger = LoggerConfig.setup_logger()

    def ilab_mid_input_cells(self, iLab, samplings, sampling):
            
            # Make a mouse clcik to tick a score checkbox
            self.logger.info(f"ilab_input_cells ==>: Make a mouse clcik to tick a score checkbox")
            iLab.set_score(samplings[sampling].get('score'))
            iLab.mouse_click_to_tick_scorebox()

            # Get iLab Sampling meaOpinion value from .json after API call to kefalab.com and set val
            self.logger.info(f"ilab_input_cells ==>: Get iLab Sampling meaOpinion value from .json after API call to kefalab.com and set val")
            meaOpinion = Helper.safe_value(samplings[sampling].get('meaOpinion'))
            iLab.set_meaOpinion(meaOpinion)
             
            # Get iLab Sampling meaStartTime_meaEndTime value from .json after API call to kefalab.com and set val
            self.logger.info(f"ilab_input_cells ==>: Get iLab Sampling meaStartTime_meaEndTime value from .json after API call to kefalab.com and set val")
            meaStartTime = Helper.safe_value(samplings[sampling].get('meaStartTime'))
            meaEndTime = Helper.safe_value(samplings[sampling].get('meaEndTime'))
            iLab.set_meaStartTime_meaEndTime(meaStartTime, meaEndTime)

            # Get iLab Sampling exposureDiameter value from .json after API call to kefalab.com and set val
            self.logger.info(f"ilab_input_cells ==>: Get iLab Sampling exposureDiameter value from .json after API call to kefalab.com and set val")
            exposureDiameter = Helper.safe_value(samplings[sampling].get('exposureDiameter'))
            iLab.set_exposureDiameter(exposureDiameter)

            # Get iLab Sampling filterPaper value from .json after API call to kefalab.com and set val
            self.logger.info(f"ilab_input_cells ==>: Get iLab Sampling filterPaper value from .json after API call to kefalab.com and set val")
            filterPaper = Helper.safe_value(samplings[sampling].get('filterPaper'))
            iLab.set_filterPaper(filterPaper)

            # Get iLab Sampling weather value from .json after API call to kefalab.com and set val
            self.logger.info(f"ilab_input_cells ==>: Get iLab Sampling weather value from .json after API call to kefalab.com and set val")
            weather = Helper.safe_value(samplings[sampling].get('weather'))
            iLab.set_weather(weather)

            # Get iLab Sampling temperature value from .json after API call to kefalab.com and set val
            self.logger.info(f"ilab_input_cells ==>: Get iLab Sampling temperature value from .json after API call to kefalab.com and set val")
            temperature = Helper.safe_value(samplings[sampling].get('temperature'))
            iLab.set_temperature(temperature)

            # Get iLab Sampling humidity value from .json after API call to kefalab.com and set val
            self.logger.info(f"ilab_input_cells ==>: Get iLab Sampling humidity value from .json after API call to kefalab.com and set val")
            humidity = Helper.safe_value(samplings[sampling].get('humidity'))
            iLab.set_humidity(humidity)

            # Get iLab Sampling atmosphericPressure value from .json after API call to kefalab.com and set val
            self.logger.info(f"ilab_input_cells ==>: Get iLab Sampling atmosphericPressure value from .json after API call to kefalab.com and set val")
            atmosphericPressure = Helper.safe_value(samplings[sampling].get('atmosphericPressure'))
            iLab.set_atmosphericPressure(atmosphericPressure)

            # Get iLab Sampling windDirection value from .json after API call to kefalab.com and set val
            self.logger.info(f"ilab_input_cells ==>: Get iLab Sampling windDirection value from .json after API call to kefalab.com and set val")
            windDirection = Helper.safe_value(samplings[sampling].get('windDirection'))
            iLab.set_windDirection(windDirection)

            # Get iLab Sampling windSpeed value from .json after API call to kefalab.com and set val
            self.logger.info(f"ilab_input_cells ==>: Get iLab Sampling windSpeed value from .json after API call to kefalab.com and set val")
            windSpeed = Helper.safe_value(samplings[sampling].get('windSpeed'))
            iLab.set_windSpeed(windSpeed)

            # Get iLab Sampling measureO2 value from .json after API call to kefalab.com and set val
            self.logger.info(f"ilab_input_cells ==>: Get iLab Sampling measureO2 value from .json after API call to kefalab.com and set val")
            measureO2 = Helper.safe_value(samplings[sampling].get('measureO2'))
            iLab.set_measureO2(measureO2)
            
            # Get iLab Sampling measureCO2 value from .json after API call to kefalab.com and set val
            self.logger.info(f"ilab_input_cells ==>: Get iLab Sampling measureCO2 value from .json after API call to kefalab.com and set val")
            measureCO2 = Helper.safe_value(samplings[sampling].get('measureCO2'))
            iLab.set_measureCO2(measureCO2)

            # Get iLab Sampling gasMeterCollBeforeAndAfter value from .json after API call to kefalab.com and set val
            self.logger.info(f"ilab_input_cells ==>: Get iLab Sampling gasMeterCollBeforeAndAfter value from .json after API call to kefalab.com and set val")
            gasMeterCollBefore = Helper.safe_value(samplings[sampling].get('gasMeterCollBefore'))
            gasMeterCollAfter = Helper.safe_value(samplings[sampling].get('gasMeterCollAfter'))
            iLab.set_gasMeterCollBeforeAndAfter(gasMeterCollBefore, gasMeterCollAfter)
            
            # Get iLab Sampling suctionGasFlowRate value from .json after API call to kefalab.com and set val
            self.logger.info(f"ilab_input_cells ==>: Get iLab Sampling suctionGasFlowRate value from .json after API call to kefalab.com and set val")
            suctionGasFlowRate = Helper.safe_value(samplings[sampling].get('suctionGasFlowRate'))
            iLab.set_suctionGasFlowRate(suctionGasFlowRate)
           
            # Get iLab Sampling suctionGasAmount value from .json after API call to kefalab.com and set val
            self.logger.info(f"ilab_input_cells ==>: Get iLab Sampling suctionGasAmount value from .json after API call to kefalab.com and set val")
            suctionGasAmount = Helper.safe_value(samplings[sampling].get('suctionGasAmount'))
            iLab.set_suctionGasAmount(suctionGasAmount)

            # Get iLab Sampling gasMeterTemp value from .json after API call to kefalab.com and set val
            self.logger.info(f"ilab_input_cells ==>: Get iLab Sampling gasMeterTemp value from .json after API call to kefalab.com and set val")
            gasMeterTemp = Helper.safe_value(samplings[sampling].get('gasMeterTemp'))
            iLab.set_aboveGasMeterTemp(gasMeterTemp)
            
            # Get iLab Sampling gaugePressureHg value from .json after API call to kefalab.com and set val
            self.logger.info(f"ilab_input_cells ==>: Get iLab Sampling gaugePressureHg value from .json after API call to kefalab.com and set val")
            gaugePressureHg = Helper.safe_value(samplings[sampling].get('gaugePressureHg'))
            iLab.set_aboveGaugePressureHg(gaugePressureHg)
            
            # Get iLab Sampling Moisture values from .json after API call to kefalab.com and set val
            self.logger.info(f"ilab_input_cells ==>: Get iLab Sampling Moisture values from .json after API call to kefalab.com and set val")
            moistureBefore1 = Helper.safe_value(samplings[sampling].get('moistureBefore1'))
            moistureBefore2 = Helper.safe_value(samplings[sampling].get('moistureBefore2'))
            moistureAfter1 = Helper.safe_value(samplings[sampling].get('moistureAfter1'))
            moistureAfter2 = Helper.safe_value(samplings[sampling].get('moistureAfter2'))
            iLab.set_moistures(moistureBefore1, moistureAfter1, moistureBefore2, moistureAfter2)

            # Get iLab Sampling inputMiddleRaw1 values from .json after API call to kefalab.com and set val
            self.logger.info(f"ilab_input_cells ==>: Get iLab Sampling inputMiddleRaw1 values from .json after API call to kefalab.com and set val")
            particulateTime1 = Helper.safe_value(samplings[sampling].get('particulateTime1'))
            vacuumPressure1 = Helper.safe_value(samplings[sampling].get('vacuumPressure1'))
            emsGasTemp1 = Helper.safe_value(samplings[sampling].get('emsGasTemp1'))
            staticPressure1 = Helper.safe_value(samplings[sampling].get('staticPressure1'))
            dynamicPressure1 = Helper.safe_value(samplings[sampling].get('dynamicPressure1'))
            sampleVolumeMeter1 = Helper.safe_value(samplings[sampling].get('sampleVolumeMeter1'))
            gasMeterTempIn1 = Helper.safe_value(samplings[sampling].get('gasMeterTempIn1'))
            gasMeterTempOut1 = Helper.safe_value(samplings[sampling].get('gasMeterTempOut1'))
            filterPaperTemp1 = Helper.safe_value(samplings[sampling].get('filterPaperTemp1'))
            impingerTemp1 = Helper.safe_value(samplings[sampling].get('impingerTemp1'))
            meaPoint1 = Helper.safe_value(samplings[sampling].get('meaPoint1'))
            w1 = Helper.safe_value(samplings[sampling].get('w1'))
            h1 = Helper.safe_value(samplings[sampling].get('h1'))
            iLab.set_inputMiddleRaw1(particulateTime1,vacuumPressure1,emsGasTemp1,staticPressure1,dynamicPressure1,sampleVolumeMeter1,gasMeterTempIn1,gasMeterTempOut1,filterPaperTemp1,impingerTemp1,meaPoint1,w1,h1)

            # Get iLab Sampling inputMiddleRaw2 values from .json after API call to kefalab.com and set val
            self.logger.info(f"ilab_input_cells ==>: Get iLab Sampling inputMiddleRaw2 values from .json after API call to kefalab.com and set val")
            particulateTime2 = Helper.safe_value(samplings[sampling].get('particulateTime2'))
            vacuumPressure2 = Helper.safe_value(samplings[sampling].get('vacuumPressure2'))
            emsGasTemp2 = Helper.safe_value(samplings[sampling].get('emsGasTemp2'))
            staticPressure2 = Helper.safe_value(samplings[sampling].get('staticPressure2'))
            dynamicPressure2 = Helper.safe_value(samplings[sampling].get('dynamicPressure2'))
            sampleVolumeMeter2 = Helper.safe_value(samplings[sampling].get('sampleVolumeMeter2'))
            gasMeterTempIn2 = Helper.safe_value(samplings[sampling].get('gasMeterTempIn2'))
            gasMeterTempOut2 = Helper.safe_value(samplings[sampling].get('gasMeterTempOut2'))
            filterPaperTemp2 = Helper.safe_value(samplings[sampling].get('filterPaperTemp2'))
            impingerTemp2 = Helper.safe_value(samplings[sampling].get('impingerTemp2'))
            meaPoint2 = Helper.safe_value(samplings[sampling].get('meaPoint2'))
            w2 = Helper.safe_value(samplings[sampling].get('w2'))
            h2 = Helper.safe_value(samplings[sampling].get('h2'))
            iLab.set_inputMiddleRaw2(particulateTime2,vacuumPressure2,emsGasTemp2,staticPressure2,dynamicPressure2,sampleVolumeMeter2,gasMeterTempIn2,gasMeterTempOut2,filterPaperTemp2,impingerTemp2,meaPoint2,w2,h2)

            # Get iLab Sampling inputMiddleRaw3 values from .json after API call to kefalab.com and set val
            self.logger.info(f"ilab_input_cells ==>: Get iLab Sampling inputMiddleRaw3 values from .json after API call to kefalab.com and set val")
            particulateTime3 = Helper.safe_value(samplings[sampling].get('particulateTime3'))
            vacuumPressure3 = Helper.safe_value(samplings[sampling].get('vacuumPressure3'))
            emsGasTemp3 = Helper.safe_value(samplings[sampling].get('emsGasTemp3'))
            staticPressure3 = Helper.safe_value(samplings[sampling].get('staticPressure3'))
            dynamicPressure3 = Helper.safe_value(samplings[sampling].get('dynamicPressure3'))
            sampleVolumeMeter3 = Helper.safe_value(samplings[sampling].get('sampleVolumeMeter3'))
            gasMeterTempIn3 = Helper.safe_value(samplings[sampling].get('gasMeterTempIn3'))
            gasMeterTempOut3 = Helper.safe_value(samplings[sampling].get('gasMeterTempOut3'))
            filterPaperTemp3 = Helper.safe_value(samplings[sampling].get('filterPaperTemp3'))
            impingerTemp3 = Helper.safe_value(samplings[sampling].get('impingerTemp3'))
            meaPoint3 = Helper.safe_value(samplings[sampling].get('meaPoint3'))
            w3 = Helper.safe_value(samplings[sampling].get('w3'))
            h3 = Helper.safe_value(samplings[sampling].get('h3'))
            iLab.set_inputMiddleRaw3(particulateTime3,vacuumPressure3,emsGasTemp3,staticPressure3,dynamicPressure3,sampleVolumeMeter3,gasMeterTempIn3,gasMeterTempOut3,filterPaperTemp3,impingerTemp3,meaPoint3,w3,h3)

            # Get iLab Sampling inputMiddleRaw4 values from .json after API call to kefalab.com and set val
            self.logger.info(f"ilab_input_cells ==>: Get iLab Sampling inputMiddleRaw4 values from .json after API call to kefalab.com and set val")
            particulateTime4 = Helper.safe_value(samplings[sampling].get('particulateTime4'))
            vacuumPressure4 = Helper.safe_value(samplings[sampling].get('vacuumPressure4'))
            emsGasTemp4 = Helper.safe_value(samplings[sampling].get('emsGasTemp4'))
            staticPressure4 = Helper.safe_value(samplings[sampling].get('staticPressure4'))
            dynamicPressure4 = Helper.safe_value(samplings[sampling].get('dynamicPressure4'))
            sampleVolumeMeter4 = Helper.safe_value(samplings[sampling].get('sampleVolumeMeter4'))
            gasMeterTempIn4 = Helper.safe_value(samplings[sampling].get('gasMeterTempIn4'))
            gasMeterTempOut4 = Helper.safe_value(samplings[sampling].get('gasMeterTempOut4'))
            filterPaperTemp4 = Helper.safe_value(samplings[sampling].get('filterPaperTemp4'))
            impingerTemp4 = Helper.safe_value(samplings[sampling].get('impingerTemp4'))
            meaPoint4 = Helper.safe_value(samplings[sampling].get('meaPoint4'))
            w4 = Helper.safe_value(samplings[sampling].get('w4'))
            h4 = Helper.safe_value(samplings[sampling].get('h4'))
            iLab.set_inputMiddleRaw4(particulateTime4,vacuumPressure4,emsGasTemp4,staticPressure4,dynamicPressure4,sampleVolumeMeter4,gasMeterTempIn4,gasMeterTempOut4,filterPaperTemp4,impingerTemp4,meaPoint4,w4,h4)

            # Get iLab Sampling inputMiddleRaw5 values from .json after API call to kefalab.com and set val
            self.logger.info(f"ilab_input_cells ==>: Get iLab Sampling inputMiddleRaw5 values from .json after API call to kefalab.com and set val")
            particulateTime5 = Helper.safe_value(samplings[sampling].get('particulateTime5'))
            vacuumPressure5 = Helper.safe_value(samplings[sampling].get('vacuumPressure5'))
            emsGasTemp5 = Helper.safe_value(samplings[sampling].get('emsGasTemp5'))
            staticPressure5 = Helper.safe_value(samplings[sampling].get('staticPressure5'))
            dynamicPressure5 = Helper.safe_value(samplings[sampling].get('dynamicPressure5'))
            sampleVolumeMeter5 = Helper.safe_value(samplings[sampling].get('sampleVolumeMeter5'))
            gasMeterTempIn5 = Helper.safe_value(samplings[sampling].get('gasMeterTempIn5'))
            gasMeterTempOut5 = Helper.safe_value(samplings[sampling].get('gasMeterTempOut5'))
            filterPaperTemp5 = Helper.safe_value(samplings[sampling].get('filterPaperTemp5'))
            impingerTemp5 = Helper.safe_value(samplings[sampling].get('impingerTemp5'))
            meaPoint5 = Helper.safe_value(samplings[sampling].get('meaPoint5'))
            w5 = Helper.safe_value(samplings[sampling].get('w5'))
            h5 = Helper.safe_value(samplings[sampling].get('h5'))
            iLab.set_inputMiddleRaw5(particulateTime5,vacuumPressure5,emsGasTemp5,staticPressure5,dynamicPressure5,sampleVolumeMeter5,gasMeterTempIn5,gasMeterTempOut5,filterPaperTemp5,impingerTemp5,meaPoint5,w5,h5)

            # Get iLab Sampling smoke value from .json after API call to kefalab.com and set val
            self.logger.info(f"ilab_input_cells ==>: Get iLab Sampling smoke value from .json after API call to kefalab.com and set val")
            smoke = Helper.safe_value(samplings[sampling].get('smoke'))
            iLab.set_smoke(smoke)

            # Get iLab Sampling samplingMemo value from .json after API call to kefalab.com and set val
            self.logger.info(f"ilab_input_cells ==>: Get iLab Sampling samplingMemo value from .json after API call to kefalab.com and set val")
            samplingMemo = Helper.safe_value(samplings[sampling].get('samplingMemo'))
            iLab.set_samplingMemo(samplingMemo)