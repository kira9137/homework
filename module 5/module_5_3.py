class House:
  def __init__(self, name, number_of_floors):
      self.name = name
      self.number_of_floors = number_of_floors

  def __eq__(self, other):
      if isinstance(other, House):
          return self.number_of_floors == other.number_of_floors
      return NotImplemented

  def __lt__(self, other):
      if isinstance(other, House):
          return self.number_of_floors < other.number_of_floors
      return NotImplemented

  def __le__(self, other):
      if isinstance(other, House):
          return self.number_of_floors <= other.number_of_floors
      return NotImplemented

  def __gt__(self, other):
      if isinstance(other, House):
          return self.number_of_floors > other.number_of_floors
      return NotImplemented

  def __ge__(self, other):
      if isinstance(other, House):
          return self.number_of_floors >= other.number_of_floors
      return NotImplemented

  def __ne__(self, other):
      if isinstance(other, House):
          return self.number_of_floors != other.number_of_floors
      return NotImplemented

  def __add__(self, value):
      if isinstance(value, int):
          self.number_of_floors += value
          return self
      return NotImplemented

  __radd__ = __iadd__ = __add__

  def __str__(self):
      return f"Название: {self.name}, кол-во этажей: {self.number_of_floors}"

house1 = House("ЖК 'Эльбрус'", 30)
house2 = House("ЖК 'Казбек'", 30)
house3 = House("ЖК 'Арарат'", 35)

# Сравнение количества этажей
print(house1 == house2)  # __eq__
print(house1 < house3)   # __lt__
print(house3 > house2)   # __gt__
print(house1 != house3)  # __ne__

# Изменение количества этажей
house1 += 5 # __iadd__
print(house1)

house2 = 10 + house2 # __radd__
print(house2)

house1 = house1 + 10 # __add__
print(house1)