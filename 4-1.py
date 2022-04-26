import RPi.GPIO as GPIO

dac = [26, 19, 13, 6, 5, 11, 9, 10]

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)

def decimal2binary(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]

try:
    while True:
        a = input("Введите значение от 0 до 256: ")
        if ( a == "q") :
            break
        a = int(a)
        if ( a > 255 or a < 0 ) :
            print ("Некорректное значение")
            break
        GPIO.output(dac, decimal2binary(a))
        voltage = a / 255 * 3.3
        print (voltage)
except TypeError :
    print ("Нечисловое значение")
except ValueError :
    print ("Нецелое число")

finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()
