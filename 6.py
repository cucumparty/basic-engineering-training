import RPi.GPIO as GPIO
import matplotlib.pyplot as plt
import time

leds = [21, 20, 16, 12, 7, 8, 25, 24]
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
        time.sleep(0.001)
        compValue = GPIO.input(comp)
        if compValue == 0 :
            break
    return i

try:
    GPIO.output(troyka, 1)
    begin = time.time()
    while True :
        znachenie = adc()
        measured_data.append(znachenie)
        GPIO.output(leds, decimal2binary(znachenie))
        if znachenie >= 253 :
            break
    GPIO.output(troyka, 0)
    while True :
        znachenie = adc()
        measured_data.append(znachenie)
        GPIO.output(leds, decimal2binary(znachenie))
        if znachenie == 5 :
            end = time.time()
            break
    lasting = end - begin

    v = len(measured_data) / lasting
    period = lasting / len(measured_data)
    quant = measured_data[2] - measured_data[1]
    plt.plot(measured_data)
    plt.show()
    
    measured_data_str = [str(item) for item in measured_data]
    v_str = str(v)
    quant_str = str(quant)
    with open("data.txt", "w") as outfile :
        outfile.write("\n".join(measured_data_str))

    with open("settings.txt", "w") as outfile1 :
        outfile1.write("\n".join(quant_str))
        outfile1.write("\n".join(v_str))
    print("Продолжительность эксперимента: ", lasting, ",период: ", period, ", частота:", v) 
        
finally:
    GPIO.output(dac, 0)
    GPIO.output(troyka, 0)
    GPIO.output(leds, 0)
    GPIO.cleanup()


