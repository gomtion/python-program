
from gpiozero import LED, Button
from signal import pause
import os


button = Button(2)

def message(r):
    print("opening app")
    r = os.system("chromium-browser --app=http://patientino.herokuapp.com")
    print(r)

button.when_pressed = message


pause()