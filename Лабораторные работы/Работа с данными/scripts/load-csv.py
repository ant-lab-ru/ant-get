import numpy as np

data = np.loadtxt('data.csv',
                  delimiter=',',
                  skiprows=1,
                  encoding='utf-8')

time = data[:, 0].astype(float)
voltage = data[:, 1].astype(float)

print(time)
print(voltage)
