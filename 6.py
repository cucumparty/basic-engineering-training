import myplotlib.pyplot as plt
measured_data = [10, 23]
plt.plot(measured_data)
plt.show

measured_data_str = [str(item) for item in measured_data]
print(measured_data, measured_data_str)

with open("data.txt", "w") as outfile :
    outfile.write("\n".join(measured_data_str))