def test_function():
  def inner_function():
      print("Я в области видимости функции test_function")
  inner_function()
test_function()

# вызов inner_function() выдает ошибку так как эта функция вложена в другую функцию
# попасть в inner_function() можно только вызвав test_function()
# inner_function()