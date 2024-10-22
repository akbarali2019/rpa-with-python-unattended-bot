import requests
from iLab_automation_log import LoggerConfig

class NotifyCompletion:

    def __init__(self):
        self.logger = LoggerConfig.setup_logger()

    def notify_kefalab(self, samplingId):
        notificationUrl = f"http://192.168.0.30:8080/api/v1/auth/samplings/state/{samplingId}"
        self.logger.info(f"notify_kefalab ==> Call for api: {notificationUrl} to update iLab status of sampling into APPROVED")
        updateState = {"state": "APPROVED"}
        response = requests.put(notificationUrl, json=updateState)
        if response.status_code == 200:
            self.logger.info(f"notify_kefalab ==> Sampling {samplingId} updated successfully!")
            print(f"Sampling {samplingId} updated successfully!")
        else:
            self.logger.warning(f"notify_kefalab ==> Api Call for {notificationUrl} Failed. Response: {response.text}")
            print(f"Response: {response.text}")