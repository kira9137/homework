def print_params(a=1, b='строка', c=True):
  print(a, b, c)

print_params()
print_params(b=25)
print_params(c=[1, 2, 3])

values_list = ['text', 42, False]
values_dict = {'a': 5.1, 'b': False, 'c': None}
print_params(*values_list)
print_params(**values_dict)

values_list_2 = ['текст', True]
print_params(*values_list_2, 42)
