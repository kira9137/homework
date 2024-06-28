# две функции здесь нужны чтобы не выносить total_sum за пределы функций
# но можно было и вынести, а в самой функции тогда установить её как глобальную переменную

def calculate_structure_sum(data_structure):
  total_sum = 0

  def sum_elements(element):
      nonlocal total_sum
      #разбиваем словарь
      if isinstance(element, dict):
          for key, value in element.items():
              sum_elements(key)
              sum_elements(value)
      #обрабатываем каждое значение list, tuple, set
      elif isinstance(element, (list, tuple, set)):
          for i in element:
              sum_elements(i)
      elif isinstance(element, str):
          total_sum += len(element)
      elif isinstance(element, (int, float)):
          total_sum += element

  sum_elements(data_structure)
  return total_sum

# Входные данные
data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)
