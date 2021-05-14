
import RPi.GPIO as GPIO
import time
GPIO.cleanup()
PUMP_PIN = 38
GPIO.setmode(GPIO.BOARD)
GPIO.setup(PUMP_PIN, GPIO.OUT)
GPIO.output(PUMP_PIN, GPIO.LOW)
time.sleep(100)

        #return "PUMP is off"
GPIO.output(PUMP_PIN, GPIO.HIGH)
time.sleep(4)
GPIO.cleanup()