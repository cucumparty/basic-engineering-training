import RPI.GPIO as GPIO
import time

dac = [26, 19, 13, 6, 5, 11, 9, 10]

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.out)

def decimal2binary(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]

try:
    while True :
        period = 10
        i = 0
        while i < 256 :
            GPIO.output(dac, decimal2binary(i))
            i+=1
            time.sleep (period / 512)
        while i > 0 :
            GPIO.output(dac, decimal2binary(i))
            i-=1
            time.sleep (period / 512)

finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()