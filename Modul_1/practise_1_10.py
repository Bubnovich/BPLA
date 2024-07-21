import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# ID БПЛА | Время полета (минуты) | Расстояние (километры) | Средняя скорость (км.ч) | Высота полета |
drones_data = np.array([
    [1, 30, 10, 20, 500],
    [2, 45, 15, 20, 600],
    [3, 25, 8, 19.2, 550],
    [4, 60, 25, 25, 700],
    [5, 35, 12, 20.6, 580]
])

altitudes = drones_data[:, 4]
max_altitudes = np.max(altitudes)
print(f'Максимальная высота полета: {max_altitudes}')

long_flight_drones = drones_data[drones_data[:, 1] > 30]
print(f"Дроны летающие дольше 30 минут:")
print(long_flight_drones)

total_dist = np.sum(drones_data[:, 2])
print(f"\n Всего пройдено расстояние: {total_dist}")

#drones_df.plot(x='ID БПЛА', y='Время полета', kind='bar')
drone_ids = drones_data[:, 0]
flight_times = drones_data[:, 4]

plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1) # 1 строка, 2 столбца, 1й график
plt.bar(drone_ids, flight_times, color="blue")
plt.xlabel('ID БПЛА')
plt.ylabel('Время полета (минуты)')
plt.title('Время полета БПЛА')

plt.subplot( 1, 2, 2)
plt.bar(drone_ids, altitudes, color="green")
plt.xlabel('ID БПЛА')
plt.ylabel('Высота полета (метры)')
plt.title('Высота полета БПЛА')

plt.savefig("mygraph.png")

convertation_matrix = np.array([
    [1, 0],
    [0, 0.277778]
])

speed_kmk = drones_data[:, 3]
speed_ms = speed_kmk * convertation_matrix[1, 1]

print(f"speed_kmk: {speed_kmk}")
print(f"speed_ms: {speed_ms}")