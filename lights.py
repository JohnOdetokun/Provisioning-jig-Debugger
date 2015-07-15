import RPi.GPIO as GPIO
import time

class Lights:
    def __init__(self):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setwarnings(False)
        #success LED
        GPIO.setup(13,GPIO.OUT)
        GPIO.output(13,0)
        #Busy LED
        GPIO.setup(7,GPIO.OUT)
        GPIO.output(7,1)
        #fail LED
        GPIO.setup(12,GPIO.OUT)
        GPIO.output(12,0)

        GPIO.setup(15,GPIO.OUT)
        GPIO.output(15,1)
        
    def __enter__(self):
        return self   

    def success(self):
        GPIO.output(13,1)
        time.sleep(2)
        GPIO.output(13,0)
        time.sleep(1)

    def failed(self):
        GPIO.output(12,1)
        time.sleep(2)
        GPIO.output(12,0)
        time.sleep(1)     

    def clean(self):
        GPIO.cleanup()
        
    def __exit__(self, type, value, traceback):
        GPIO.cleanup()
