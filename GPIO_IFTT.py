# a program that sends a message to your phone when abutton is pressed("IFTTT was used")
from gpiozero import LED, Button
from signal import pause
import requests


button = Button(2)

def message(r):
    print(r)
    r = requests.get("https://maker.ifttt.com/trigger/globalcode/with/key/lYPq_WoPi63iCTm22xsarLBQS8aHR6ietLkJP7u7vNJ")
    print(r)

button.when_pressed = message


pause()
