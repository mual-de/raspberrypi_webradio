import RPi.GPIO as GPIO



class Switches():


    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(24, GPIO.IN)
        GPIO.setup(23, GPIO.IN)
        GPIO.setup(22, GPIO.IN)


    def getModeState(self):
        return GPIO.input(24)

    def getBroadcastTechnology(self):
        if GPIO.input(23):
            return "AM"
        elif GPIO.input(22):
            return "FM"
        else:
            return "LW"