import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Check wavefont
df = pd.read_csv("../ExperimentData/AttenuationLength/Lengtha3.csv")
t = df['Time(s)'].values
ch1 = df['CH1V'].values
ch2 = df['CH2V'].values

print("Ch1 minimum: ", np.min(ch1))
print("Ch2 minimum: ", np.min(ch2))

# Draw
plt.figure()
plt.plot(t, ch1, '-g', label='ch1')
plt.plot(t, ch2, '-r', label='ch2')
plt.legend()
plt.xlabel("Time")
plt.ylabel("Voltage")
plt.title("Wavefont03")
plt.savefig("./figs/CheckWavefont03.png")

print("End")
