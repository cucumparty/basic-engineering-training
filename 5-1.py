import RPi.GPIO as GPIO
import time

dac = [26, 19, 13, 6, 5, 11, 9, 10]
comp = 4
troyka = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial = GPIO.HIGH)
GPIO.setup(comp, GPIO.IN)

def decimal2binary(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]

def adc() :
    i = 0
    while i < 256 :
        GPIO.output(dac, decimal2binary(i))
        time.sleep(0.01)
        compValue = GPIO.input(comp)
        if compValue == 0 :
            break
        i+= 1
    return i

try:
    while True:
        znachenie = adc()
        voltage = znachenie * 3.3 / 256
        print( decimal2binary(znachenie)," ", znachenie," ", voltage)
        
finally:
    GPIO.output(dac, 0)
    GPIO.output(troyka, 0)
    GPIO.cleanup()
    
