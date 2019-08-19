# help: python3 sub.py 192.168.0.242

import paho.mqtt.client as mqtt
import sys
from gpiozero import LED
from time import sleep

ip_addr = str(sys.argv[1])
led = LED(26)

def on_connect(client, data, flags, rc):
	print("connected with return code %s" %(rc))
	client.subscribe("topic/test")

def on_message(client, data, msg):
	if msg.payload.decode() == "button press":
		print("received button press")
		led.on()
		sleep(0.5)
		led.off()

client = mqtt.Client()
client.connect(ip_addr, 1883, 60)

client.on_connect = on_connect
client.on_message = on_message

client.loop_forever()