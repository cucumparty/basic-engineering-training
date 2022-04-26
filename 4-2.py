import RPi.GPIO as GPIO
import time

dac = [26, 19, 13, 6, 5, 11, 9, 10]

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)

def decimal2binary(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]

try:
    while True :
        period = 20
        i = 0
        for i in range(255) :
            GPIO.output(dac, decimal2binary(i))
            i+=1
            print (i)
            time.sleep (period / 512)

        while i >= 0 :
            GPIO.output(dac, decimal2binary(i))
            i-=1
            print (i)
            time.sleep (period / 512)

finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()
