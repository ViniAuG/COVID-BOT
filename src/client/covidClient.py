import requests

req = requests.get('https://covid19-brazil-api.now.sh/api/report/v1/brazil')
data = req.json()

def getCovidData():
    return data


