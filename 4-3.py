import RPI.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(24, GPIO.OUT)

p = GPIO.PWM(24, 1000)
p.start(1)
try:
    while True :
        a = input("Введите коэффициент заполнения:")
        if a == 0 :
            a = 1
        p.start(a)
        time.sleep(5)
        p.stop()

finally:
    GPIO.cleanup()