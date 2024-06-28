my_dict = {'Алиса': 1984, 'Иван': 1990, 'Аня': 1995}
print("Список:", my_dict)
print("Год рождения Алисы:", my_dict['Алиса'])
print("Год рождения Андрея:", my_dict.get('Андрей'))
my_dict['Ева'] = 2000
my_dict['Слава'] = 1988
removed_value = my_dict.pop('Аня')
print("Удаленное значение, Аня:", removed_value)
print("Измененный список:", my_dict)

my_set = {1, 'text', True, 1, 'text', False}
print("Исходное множество:", my_set)
my_set.add('кровать')
my_set.add(42)
my_set.discard('text')
print("Измененное множество:", my_set)
