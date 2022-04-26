import RPi.GPIO as GPIO
import time

dac = [26, 19, 13, 6, 5, 11, 9, 10]
comp = 4
troyka = 17
leds = [24, 25, 8, 7, 12, 16, 20, 21]

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(comp, GPIO.IN)
GPIO.setup(leds, GPIO.OUT)


def decimal2binary(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]


def adc():
    i = 0
    while i < 256:
        GPIO.output(dac, decimal2binary(i))
        time.sleep(0.01)
        compValue = GPIO.input(comp)
        if compValue == 0:
            break
        i += 1
    return i

def sled() :
    GPIO.output(leds, 0) 
    a = 0
    for a in range(9):
        if(znachenie < a * 32 + 5):
            j = 0
            for j in range(a):
                GPIO.output(leds[j], 1)
            break  



try:
    while True:
        znachenie = adc()
        voltage = znachenie * 3.3 / 256
        print(decimal2binary(znachenie), " ", znachenie, " ", voltage)
        sled()

finally:
    GPIO.output(dac, 0)
    GPIO.output(troyka, 0)
    GPIO.output(troyka, 0)
    GPIO.cleanup()
