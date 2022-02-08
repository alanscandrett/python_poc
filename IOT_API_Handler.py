# -*- coding: utf-8 -*-
"""Internet of Things Module

This module handles SigFox API sensor data, it pushes this data to an AGOL 
feature layer. Emails are triggered when a sensor meets certain conditions.
"""
import logging
import requests
import emailSMTP
from assets.settings import *
setupLogging()
logger = logging.getLogger(__name__)

def main():
    """Controller
    Entrypoint for the application; controls submodules and core functions.
    """
    logger.info("\n>> STARTED")
    jsonSensors = GetSensorData()
    logger.info("\n>> COMPLETED")
    alertedSensors = filterByState(MISC_CONFIG["WARNING_STATE"], jsonSensors)
    if len(alertedSensors):
        generateEmail(alertedSensors)
    


def GetSensorData():
    """return sensor json data
    Connect to SigFox REST API and extract sensor data as json
    """
    url = API_SIGFOX["URL"] + API_SIGFOX["DEVICES_QUERY"]["ENDPOINT"]
    credentials = (API_SIGFOX["USER"], API_SIGFOX["PASS"])
    payload = API_SIGFOX["DEVICES_QUERY"]["PARAMS"]
    logger.info('Handling request to %s with params: %s', url, payload)
    response = requests.get(url, auth=credentials, params=payload)
    if response.status_code != requests.codes.ok:
        response.raise_for_status()
    return response.json()['data']

def generateEmail(jsonSensors):
    emailSMTP.configure(EMAIL["SMTP_SERVER"], EMAIL["ACCOUNT"], EMAIL["PASS"])
    message = EMAIL["TEMPLATE_WARNING"]
    recipient = EMAIL["RECIPIENT"]
    # Format Message
    sensorDetails = []
    for sensor in jsonSensors:
        sensorString = f"{sensor['id']} - {sensor['name']}"
        sensorDetails.append(sensorString)
    message += "\n" + "\n".join(sensorDetails)
    #
    emailSMTP.sendEmail(recipient, message)

def filterByState(state, sensorJson):
    alerted = [sensor for sensor in sensorJson if sensor['state'] == state]
    return alerted   

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        logger.error(e, exc_info=True)