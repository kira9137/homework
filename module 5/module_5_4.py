class House:
  houses_history = []

  def __new__(cls, *args, **kwargs):
      instance = super(House, cls).__new__(cls)
      if args:
          cls.houses_history.append(args[0])
      return instance

  def __init__(self, name, number_of_floors):
      self.name = name
      self.number_of_floors = number_of_floors

  def __del__(self):
      print(f"{self.name} снесён, но он останется в истории")

# Создание объектов класса House
house1 = House("ЖК Эльбрус", 30)
print(House.houses_history)
house2 = House("ЖК Казбек", 25)
print(House.houses_history)
house3 = House("ЖК Вершина", 2)
print(House.houses_history)

# удаление объекта
del house2
del house3

print(House.houses_history)