from time import sleep
import RPi.GPIO as GPIO
from pi_sht1x import SHT1x
#import bh1750
import time

def test_sht1x(DATA_PIN, SCK_PIN):
    print('Test: using default values: 3.5V, High resolution, no heater, otp_no_reload off, CRC checking enabled...')
    with SHT1x(DATA_PIN, SCK_PIN, gpio_mode=GPIO.BOARD) as sensor:
        for i in range(3):
            temp = sensor.read_temperature()
            humidity = sensor.read_humidity(temp)
            sensor.calculate_dew_point(temp, humidity)
            print(sensor)
            print('1111111')
            sleep(2)
    print('Test complete.\n')


def main():
    print("\n\n========= SHT1X P1 ===========")
    try:
        test_sht1x(12, 11)
    except Exception as e:
        print(e)

    print("\n\n========= SHT1X P2 ===========")
    try:
        test_sht1x(13, 15)
    except Exception as e:
        print(e)

    print("\n\n========= SHT1X P3 ===========")
    try:
        test_sht1x(16, 18)
    except Exception as e:
        print(e)

    print("\n\n========= SHT1X P4 ===========")
    try:
        test_sht1x(22, 24)
    except Exception as e:
        print(e)



if __name__ == "__main__":
    main()

