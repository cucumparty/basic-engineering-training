import RPi.GPIO as GPIO

leds = [21, 20, 16, 12, 7, 8, 25, 24]
aux = [22, 23, 27, 18, 15, 14, 3, 2]
a = 7
i = 7

GPIO.setmode(GPIO.BCM)

GPIO.setup(leds, GPIO.OUT)
GPIO.setup(aux, GPIO.IN)

GPIO.output (leds, GPIO.LOW)

while True:
    while(a >= 0):
        GPIO.output(leds[a], GPIO.input(aux[i]))
        a-=1
        i-=1
    a = 7
    i = 7
