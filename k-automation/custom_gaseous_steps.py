def apiCallForGaseousSteps(self, iLab, samplingId, samplingRegNum):
        gaseousBody = {"samplingId": samplingId}
        self.logger.info(f"apiCallForGaseousSteps ==> Call for api: {GASEOUS_URL} to get iLab sampling gaseous data")
        gaseousResponse = requests.post(GASEOUS_URL, json=gaseousBody)
        if gaseousResponse.status_code == 200:
            gaseousData = gaseousResponse.json()          
            totalItemElements = gaseousData.get('totalElements')

            self.logger.info(f"apiCallForGaseousSteps ==> api call was successfull! Total Elements: {totalItemElements}")
            self.logger.info(gaseousData)
            
            ''' To unclick the scorebox in case shape equals to 원형 '''
            facilityProperties = gaseousData.get('facilityProperties', {})
            facilityShape = facilityProperties.get('shape')
            
            if facilityShape == "원형":
                # To unclick scorebox in case facility shape(모양) equals to "원형"
                self.logger.info(f"facilityShape EQUALS to WONHYONG, UNCLICKING MANUAL SCOREBOX...")
                iLab.mouse_click_to_tick_scorebox()
                self.logger.info(f"UNCLICKED MANUAL SCOREBOX...")
                time.sleep(1)
            else: self.logger.info(f"No Need To Unclick a scorebox as FacilityShape is: {facilityShape}")

            GaseousSteps.process_with_gaseous_items(self, totalItemElements, gaseousData, iLab)

            # Calculate and save results
            self.logger.info(f"apiCallForGaseousSteps ==> Calculate and save results")            
            iLab.calculate_inputVals()

            # We need to check is there an exception pop-up and then continue:
            pageRegNum = iLab.get_inquiry_number_from_the_screen()
            if pageRegNum == samplingRegNum:

                #iLab.save_inputVals()
                self.logger.info(f"apiCallForGaseousSteps ==>: close_iLabSubwindows")
                iLab.close_iLabSubwindows()


                time.sleep(0.5)
                pyautogui.press('enter') # To save input vals
                time.sleep(1)

                # Update the iLabStatus of automated samplingRegNumber in the local automation_db
                CheckLocalDb.update_samplingStatus(samplingRegNum, STATUS_APPROVED, COMPANY_CODE)
                time.sleep(0.5) #3 

                # Notify to update the iLabStatus of automated samplingRegNumber
                self.logger.info(f"Notify to update the iLabStatus of automated samplingRegNumber")
                NotifyCompletion.notify_kefalab(self, samplingId)
            else:
                CheckLocalDb.update_samplingStatus(samplingRegNum, STATUS_FAIL, COMPANY_CODE)
                NotifyCompletion.notifyFail_kefalab(self, samplingId)
                pyautogui.press('enter', 10, 0.2)
                #iLab.save_inputVals()
                iLab.close_iLabSubwindows()
                time.sleep(0.5)
                pyautogui.press('enter') # To save input vals although some them  are wrong. This gives a user to check the wrong val and avoid again input ohter not wrong vals
                time.sleep(1)

        else:
            GaseousSteps.handleApiFailure((self, iLab, GASEOUS_URL, gaseousResponse, samplingId))
