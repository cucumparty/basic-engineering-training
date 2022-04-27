import numpy as np
import matplotlib.pyplot as plt
with open("/home/b01-101/settings.txt", "r") as settings:
    tmp = [float(i) for i in settings.read().split("\n")]

with open("/home/b01-101/data.txt", "r") as settings:
    tmp = [float(i) for i in settings.read().split("\n")]

data_array = np.loadtxt("/home/b01-101/data.txt", dtype = int)
settings_array = np.loadtxt("/home/b01-101/settings.txt", dtype = float)

voltage = data_array * 3.3 / 256 

x = [0] * 973
for i in range(973):
    x[i] = i * settings_array[1]

print(x)

fig, ax= plt.subplots(figsize = (16, 11), dpi = 200)
plt.plot(x, voltage, color = "red", marker='o', linestyle='dashed',
     linewidth=2, markersize=5, markevery = 70)

plt.title("Процесс заряда и разряда конденсатора в RС - цепи") # заголовок
ax.grid(which='major',
        color = 'k', 
        linewidth = 2)
ax.minorticks_on()
ax.grid(which='minor', 
        color = 'k', 
        linestyle = ':')
plt.legend(['v(t)'])
ax.set_xlabel("Время, с", fontsize=14)        
ax.set_ylabel("Напряжение, В", fontsize=14)

t_charge = x[np.argmax(data_array)]
t_down =  (937 - np.argmax(data_array)) * settings_array[1]

plt.text(6, 2.5, 'Время зарядки:%f' % t_charge, fontsize=7, color = "blue")
plt.text(6, 2, 'Время разрядки:%f' % t_down, fontsize=7, color = "blue")
plt.xlim(0, 10)
plt.ylim(0, 4)
fig.savefig("test.png")
plt.show()
