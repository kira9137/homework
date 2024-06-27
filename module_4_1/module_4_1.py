from fake_math import divide as fake_divide
from true_math import divide as true_divide

# Пример использования
fake_result = fake_divide(10, 0)
true_result = true_divide(10, 0)

print(f"Результат fake_math: {fake_result}")
print(f"Результат true_math: {true_result}")