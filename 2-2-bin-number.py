import RPi.GPIO as GPIO
import time

dac = [26, 19, 13, 6, 5, 11, 9, 10]
number = [1, 1, 1, 1, 1, 1, 1, 1]
a = 7
i = 7

GPIO.setmode(GPIO.BCM)

GPIO.setup(dac, GPIO.OUT)

while(a >= 0):
    GPIO.output(dac[a], number[i])
    a-=1
    i-=1

time.sleep(15)

GPIO.output(dac, 0)
GPIO.cleanup()
