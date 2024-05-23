immutable_var = (42, "строка", 3.14, True)
print("Кортеж:", immutable_var)

#immutable_var[0] = 100
#print(immutable_var)
#переменные в картеже нельзя изменить потому что они неизменяемы

mutable_list = [42, "строка", 3.14, False]
print("Список", mutable_list)
mutable_list[0] = 100
mutable_list[1] = "новая строка"
print("Список", mutable_list)