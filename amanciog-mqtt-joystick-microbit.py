"""
To get started, check out the "Device Simulator Express: Getting Started" command in the command pallete, which you can access with `CMD + SHIFT + P` For Mac and `CTRL + SHIFT + P` for Windows and Linux.

Get started with micro:bit and MicroPython on:
https://microbit-micropython.readthedocs.io/en/latest/.
"""

from microbit import *
import paho.mqtt.client as mqtt

CENTER = Image("00000:00000:00000:00000:00000") # variable named CENTER is set into a color of none

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        client.subscribe("joystickguian") # client subcribed gets the value of joystickguian
        display.show(Image.YES)

def on_message(client, userdata, msg):
    if msg.payload.decode() == "S":  # checks if msg.payload is equals to S
        display.show(Image.ARROW_S)  #displays the microbit light into arrow S or arrow specifying the arrow down
    elif msg.payload.decode() == "SE": # checks if msg.payload is equals to SE
        display.show(Image.ARROW_SE)   #displays the microbit light into arrow SE or arrow specifying the arrow pointing South East
    elif msg.payload.decode() == "SW":  # checks if msg.payload is equals to SW
        display.show(Image.ARROW_SW)   #displays the microbit light into arrow SW or arrow specifying the arrow pointing South West
    elif msg.payload.decode() == "N":  # checks if msg.payload is equals to N
        display.show(Image.ARROW_N)    #displays the microbit light into arrow N or arrow specifying the arrow pointing Upwards
    elif msg.payload.decode() == "NE": # checks if msg.payload is equals to NE
        display.show(Image.ARROW_NE)   #displays the microbit light into arrow NE or arrow specifying the arrow North East
    elif msg.payload.decode() == "NW":   # checks if msg.payload is equals to NW
        display.show(Image.ARROW_NW)   #displays the microbit light into arrow NW or arrow specifying the arrow North West
    elif msg.payload.decode() == "W":  # checks if msg.payload is equals to W
        display.show(Image.ARROW_W)  #displays the microbit light into arrow W or arrow specifying the arrow pointing left
    elif msg.payload.decode() == "E": # checks if msg.payload is equals to E
        display.show(Image.ARROW_E)   #displays the microbit light into arrow E or arrow specifying the arrow pointing right
    else:
        display.show(CENTER)   # displays if the pointer is at the center and displays the color into none
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("test.mosquitto.org", 1883, 60)
client.loop_forever()

# Broker for online client: https://iamelijah2016.github.io/
# wss://mqtt.eclipse.org:443/mqtt
# wss://test.mosquitto.org:8081/mqtt