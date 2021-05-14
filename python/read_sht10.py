from time import sleep
import RPi.GPIO as GPIO
from pi_sht1x import SHT1x
#import bh1750
import time

def test_sht1x(DATA_PIN, SCK_PIN):
    with SHT1x(DATA_PIN, SCK_PIN, gpio_mode=GPIO.BOARD) as sensor:
        for i in range(1):
            temp = sensor.read_temperature()
            humidity = sensor.read_humidity(temp)
            sensor.calculate_dew_point(temp, humidity)
            print(temp,humidity)
            return temp, humidity
            sleep(2)
        print('Test complete.\n')
    


def main2():
    try:
        test_sht1x(22, 24)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()

