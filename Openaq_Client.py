import requests
import json

class Openaq_Client:

    openaq_payload = ''

    def execute(self):
        url = "https://api.openaq.org/v2/latest/5301"

        headers = {
            'X-API-Key': 'be201ec2e8955e36af43f4ff873f0cbe766adc05f37b7066085662138895fc31'
        }

        # Realizando a requisição GET para a API do OpenAQ
        response = requests.get(url, headers=headers)

        # Verificando o status da resposta
        if response.status_code == 200:
            data = response.json()  # Convertendo a resposta para JSON
            result = str(data.get('results', []))

            result = result.replace("'", '"')
            self.openaq_payload = json.loads(result)
        else:
          print(f"Erro ao acessar a API: {response.status_code}")

    def getO3(self):
        return {
            'o3': self.openaq_payload[0]['measurements'][0]['value']
        }


    def getCo(self):
        return {
            'Co': self.openaq_payload[0]['measurements'][1]['value']
        }

    def getPm10(self):
        return {
            'pm10': self.openaq_payload[0]['measurements'][2]['value']
        }
    
    
