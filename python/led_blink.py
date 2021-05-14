
import RPi.GPIO as GPIO
import time
LED_PIN = 37
GPIO.setmode(GPIO.BOARD)
GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.output(LED_PIN, GPIO.LOW)
time.sleep(5)
GPIO.output(LED_PIN, GPIO.HIGH)
GPIO.cleanup()
def led():


    LED_PIN = 37
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(LED_PIN, GPIO.OUT)

    try:
        while True:
            #return "LED is on"
            GPIO.output(LED_PIN, GPIO.LOW)
            time.sleep(5)
            #return "LED is off"
            GPIO.output(LED_PIN, GPIO.HIGH)
            time.sleep(5)

    except KeyboardInterrupt:
        return "Exception: KeyboardInterrupt"

    finally:
        GPIO.cleanup()