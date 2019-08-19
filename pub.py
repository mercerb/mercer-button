import paho.mqtt.client as mqtt
import sys
from gpiozero import Button
from time import sleep

client = mqtt.Client()

def publish_msg():
        client.publish("topic/test", "button press")

button = Button(26)
button.when_pressed = publish_msg

client.connect("localhost", 1883, 60)
client.loop_forever()