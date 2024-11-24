import paho.mqtt.client as mqtt
import json

class Mqtt_Client_Humidity:
    # Configurações do MQTT
    THINGSBOARD_HOST = 'mqtt.thingsboard.cloud'
    PORT = 1883
    ACCESS_TOKEN = 'n4by4ZQfXEe41o7CWxWU'
    client = mqtt.Client()

    def on_connect(client, rc):
        if rc == 0:
            print("Conectado ao ThingsBoard com sucesso!")
        else:
            print(f"Falha na conexão. Código: {rc}")


    def __init__(self) -> None:
        # Configurando as credenciais (Token de Acesso)
        self.client.username_pw_set(self.ACCESS_TOKEN)

        # Definindo o callback de conexão
        self.client.on_connect = self.on_connect

        # Conectando ao broker MQTT (ThingsBoard)
        self.client.connect(self.THINGSBOARD_HOST, self.PORT, 60)

        # Iniciando loop de rede
        self.client.loop_start()

    def execute(self, telemetry_payload):
        self.client.publish('v1/devices/me/telemetry', json.dumps(telemetry_payload), qos=1)
        print(f"Dados enviados: {telemetry_payload}")

    def disconect(self) -> None:
        self.client.loop_stop()
        self.client.disconnect()
