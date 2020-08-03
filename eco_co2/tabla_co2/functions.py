from datetime import datetime
import requests

def convertToDateTime(d):
    new_tab = d
    for i in new_tab:
        i['datetime'] = datetime.strptime(i['datetime'], "%Y-%m-%dT%H:%M:%S")
    return new_tab

def getCO2Data():
    url = "http://api-recrutement.ecoco2.com/v1/data?start=1483225200&end=1546297199"
    response = requests.get(url)
    return response.json()
