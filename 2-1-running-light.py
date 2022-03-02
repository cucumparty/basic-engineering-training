import RPi.GPIO as GPIO
import time

leds = [24, 25, 8, 7, 12, 16, 20, 21]
num = 1
GPIO.setmode(GPIO.BCM)

GPIO.setup(leds, GPIO.OUT)

while num <=3:
    for a in range(7, -1, -1):
        GPIO.setup(leds[a], GPIO.OUT)
        GPIO.output(leds[a], 1)
    
        time.sleep(0.2)
        GPIO.setup(leds[a], GPIO.OUT)
        GPIO.output(leds[a], 0)
    num +=1
    
GPIO.setup(leds, GPIO.OUT)
GPIO.output(leds, 0)

GPIO.cleanup()