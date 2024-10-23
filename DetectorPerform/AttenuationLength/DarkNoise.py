import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Check wavefont
df = pd.read_csv("../../ExperimentData/darknoise/darknoise0.csv")
t = df['Time(s)'].values
ch1 = df['CH1V'].values

# Draw
plt.figure()
plt.plot(t, ch1, '-g', label='ch1')
plt.legend()
plt.xlabel("Time")
plt.ylabel("Voltage")
plt.title("DarkNoise")
plt.savefig("./figs/DarkNoise.png")

print("End")
