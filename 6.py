import RPI.GPIO as GPIO
import myplotlib.pyplot as plt
import time

leds = []
dac = [26, 19, 13, 6, 5, 11, 9, 10]
comp = 4
troyka = 17

GPIO.setmode(GPIO.BCM)

GPIO.setup(troyka, GPIO.OUT)
GPIO.setup(comp, GPIO.IN)
GPIO.setup(dac, GPIO.OUT)
GPIO.setup(leds, GPIO.OUT)

measured_data = []

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

try:
    GPIO.output(troyka, 1)
    begin = time.time()
    while True :
        znachenie = adc()
        voltage = znachenie * 3.3 / 256
        measured_data.append(znachenie)
        GPIO.output(leds, decimal2binary(znachenie))
        if znachenie >= 255 :
            GPIO.output(troyka, 0)
        if znachenie == 0 :
            end = time.time()
            break
    lasting = end - begin
    plt.plot(measured_data)
    plt.show

    measured_data_str = [str(item) for item in measured_data]
    print(measured_data, measured_data_str)

    with open("data.txt", "w") as outfile :
    outfile.write("\n".join(measured_data_str))
        
finally:
    GPIO.output(dac, 0)
    GPIO.output(troyka, 0)
    GPIO.cleanup()


