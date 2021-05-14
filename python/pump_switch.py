#!/usr/bin/python3
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#|R|a|s|p|b|e|r|r|y|P|i|.|c|o|m|.|t|w|
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
# Copyright (c) 2021, raspberrypi.com.tw
# All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.
#
# Author : sosorry
# Date   : 06/22/2014

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