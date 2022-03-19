#import libs
import paho.mqtt.client as mqtt
import Adafruit_DHT
import time

# At connection time the client subscribes to the 
# dh11_sensor_commands MQTT topic
def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")
    client.subscribe("raspberry/dh11_sensor_commands")

# Whenever a command is received on the dh11_sensor_commands MQTT topic, 
# the client is reading sensor data to send an update my means of 
# the dh11_sensor_data MQTT topic
def on_message(client, userdata, msg):
    #sensor version
    sensor = 11
    #number of the pin receiving data
    gpio = 4
    print("Request received")
    humidity, temperature = Adafruit_DHT.read_retry(sensor, gpio)
    data = 'Temp: {0:0.1f}°C  Humidity: {1:0.1f} %'.format(temperature, humidity)
    client.publish('raspberry/dh11_sensor_data', payload=data, qos=0, retain=False)
    print("Data Sent to MQTT Broker")

#Create client
client = mqtt.Client()

#Register callbacks
client.on_connect = on_connect
client.on_message = on_message

# create connection
client.connect("192.168.0.2", 1883, 60)

# Loop forever
client.loop_forever()