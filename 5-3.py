import RPI.GPIO as GPIO
import time

dac = [26, 19, 13, 6, 5, 11, 9, 10]
comp = 4
troyka = 17
leds = [21, 20, 16, 12, 7, 8, 25, 24]

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
        i+= 1
        time.sleep(0.01)
        compValue = GPIO.input(comp)
        if compValue == 0 :
            break
    return i

#def adc() :
    i = 7
    a = 0 
    while i <= 0 :
        GPIO.output(dac, 1)
        time.sleep(0.01)
        compValue = GPIO.input(comp)
        if compValue == 0 :
            GPIO.output(dac[i], 0)
        if compValue == 1 :
            a = 2 ** i + a
        i-= 1
    return a

try:
    while True:
        znachenie = adc()
        voltage = znachenie * 3.3 / 256
        GPIO.output(leds, decimal2binary(znachenie))
        print( decimal2binary(znachenie)," ", znachenie," ", voltage)
        
finally:
    GPIO.output(dac, 0)
    GPIO.output(troyka, 0)
    GPIO.cleanup()
    