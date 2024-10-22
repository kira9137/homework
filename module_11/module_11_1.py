import numpy as np

# Создание массива
arr = np.array([1, 2, 3, 4, 5])

# Математические операции с массивом
squared = np.square(arr)
mean = np.mean(arr)
std_dev = np.std(arr)

print(f"Исходный массив: {arr}")
print(f"Квадрат элементов: {squared}")
print(f"Среднее значение: {mean}")
print(f"Стандартное отклонение: {std_dev}")
