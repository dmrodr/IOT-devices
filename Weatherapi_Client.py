import requests
import json

class Weatherapi_Client:
    wheaterapi_payload = ''

    def execute(self):
        API_KEY = "0991a6f347c841bc865223759240711"
        city = "São Paulo"
        url = f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city}&aqi=no"

        # Fazendo a requisição à API
        response = requests.get(url)

        # Verificando se a requisição foi bem-sucedida
        if response.status_code == 200:
            self.wheaterapi_payload = response.json()
        else:
            print(f"Erro ao buscar dados: {response.status_code}")

    def getTemperature(self):
        return {'temperature': 23}
        
    def getHumidity(self):
        return {'humidity': self.wheaterapi_payload['current']['humidity']}
        
    def getInfoWind(self):
        return {'windSpeed': self.wheaterapi_payload['current']['wind_mph'], 'windDirection': self.wheaterapi_payload['current']['wind_dir']}
        