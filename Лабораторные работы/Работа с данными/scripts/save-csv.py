import numpy as np

time = [0.01, 0.02, 0.03, 0.04, 0.05]
voltage = [0.1, 1.2, 2.3, 3.45, 4.678]

data = np.column_stack((time, voltage))

np.savetxt('data.csv',
           data, delimiter=',',
           fmt='%.4f',
           header='Время[c],Напряжение[В]',
           comments='',
           encoding='utf-8')
