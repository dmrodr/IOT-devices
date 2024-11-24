import paho.mqtt.client as mqtt
import time

from Mqtt_Client_Temperature import Mqtt_Client_Temperature
from Mqtt_Client_Co import Mqtt_Client_Co
from Mqtt_Client_O3 import Mqtt_Client_O3
from Mqtt_Client_Pm10 import Mqtt_Client_Pm10
from Mqtt_Client_Humidity import Mqtt_Client_Humidity
from Mqtt_Client_Wind import Mqtt_Client_Wind


from Openaq_Client import Openaq_Client
from Weatherapi_Client import Weatherapi_Client

def publish_telemetry(mqtt_Client_Temperature = Mqtt_Client_Temperature, mqtt_Client_Co = Mqtt_Client_Co, mqtt_Client_O3 = Mqtt_Client_O3, mqtt_Client_Pm10 = Mqtt_Client_Pm10, mqtt_Client_Humidity = Mqtt_Client_Humidity, mqtt_Client_Wind = Mqtt_Client_Wind):
        openaq_client = Openaq_Client()
        openaq_client.execute()

        mqtt_Client_Co.execute(openaq_client.getCo())
        mqtt_Client_O3.execute(openaq_client.getO3())
        mqtt_Client_Pm10.execute(openaq_client.getPm10())


        weatherapi_Client = Weatherapi_Client()
        weatherapi_Client.execute()
        
        mqtt_Client_Temperature.execute(weatherapi_Client.getTemperature())
        mqtt_Client_Humidity.execute(weatherapi_Client.getHumidity())
        mqtt_Client_Wind.execute(weatherapi_Client.getInfoWind())
    


mqtt_Client_Temperature = Mqtt_Client_Temperature()
mqtt_Client_Humidity = Mqtt_Client_Humidity()
mqtt_Client_Wind = Mqtt_Client_Wind()

mqtt_Client_Co = Mqtt_Client_Co()
mqtt_Client_O3 = Mqtt_Client_O3()
mqtt_Client_Pm10 = Mqtt_Client_Pm10()

try:
    while True:
        publish_telemetry(mqtt_Client_Temperature, mqtt_Client_Co, mqtt_Client_O3, mqtt_Client_Pm10, mqtt_Client_Humidity, mqtt_Client_Wind)
        time.sleep(10)
except KeyboardInterrupt:
    pass

mqtt_Client_Temperature.disconect()
mqtt_Client_Humidity.disconect()
mqtt_Client_Wind.disconect()


mqtt_Client_Co.disconect()
mqtt_Client_O3.disconect()
mqtt_Client_Pm10.disconect()