import numpy as np
import matplotlib.pyplot as plt

def generate_triangle_wave(amplitude, frequency, sample_rate, duration):
    # Создаем массив времени
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    
    # Генерируем треугольный сигнал
    signal = 2 * amplitude * np.abs(0.5 - (frequency * t % 1))
    
    return t, signal

# Параметры сигнала
amplitude = 2.0  # Амплитуда сигнала
frequency = 10    # Частота сигнала (Гц)
sample_rate = 1000  # Частота дискретизации (Гц)
duration = 0.5     # Длительность сигнала (сек)

# Генерируем сигнал
t, signal = generate_triangle_wave(amplitude, frequency, sample_rate, duration)

# Строим график
plt.figure(figsize=(10, 5))  # задаем размер графика
plt.plot(t, signal, label=f'Треугольный сигнал: {frequency} Гц, {amplitude} В',  linewidth=3)

plt.title(f'Треугольный сигнал')
plt.xlabel('Время, с')
plt.ylabel('Амплитуда, В')
plt.grid(True)
plt.legend()

# Сохраняем график в файл (dpi определяет разрешение изображения)
plt.savefig('Переход из цифрового мира в аналоговый/Задания/pics/triangle-signal.png', dpi=92, transparent=False)

# Показываем график
plt.show()
