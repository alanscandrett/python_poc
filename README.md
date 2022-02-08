# sigfox_iot
SigFox IoT Proof of Concept

## Functional Requirements

1. Successfully connect to SigFox API and extract sensor data via a REST API call 

2. Successfully translate and periodically publish the SigFox sensor data into an AGOL feature layer 

3. Successfully trigger an email alert upon a sensor changing to a particular state 

4. Successfully delivered the AGOL web-map and ArcGIS Dashboard 


## Dependencies
* Python 3 (tested on v3.8.10 64bit)
* [python-dotenv](https://pypi.org/project/python-dotenv/)

## .ENV Variables
    API_SIGFOX_USER =
    API_SIGFOX_PASS =
    AGOL_NOVEGEN_USER =
    AGOL_NOVEGEN_PASS =
    EMAIL_ACCOUNT =
    EMAIL_PASS =
    EMAIL_RECIPIENT =
