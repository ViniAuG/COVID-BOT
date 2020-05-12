from client.covidClient import getCovidData

class covidService:

    def __init__(self, numberOfSuspects, numberOfConfirmed, numberOfDeaths, numberOfRecovered):
        self.numberOfSuspects = numberOfSuspects
        self.numberOfConfirmed = numberOfConfirmed
        self.numberOfDeaths = numberOfDeaths
        self.numberOfRecovered = numberOfRecovered

    def covidData():
        data = getCovidData()
        dataPath = data['data']
        response = covidService(dataPath['cases'], dataPath['confirmed'], dataPath['deaths'], dataPath['recovered'])
        return response

