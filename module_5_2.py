# специальные методы
class House:       # создаем класс
    def __init__(self, name, number_of_floors): # создаем метод внутри класса с атрибутами name, number_of_floors
        self.name = name                        # указываем на объект через self
        self.number_of_floors = number_of_floors

    def __len__(self):  # при вызове функции len будем возвращать колличество этажей
        return self.number_of_floors

    def __str__(self):  # при вызове функции str будет возвращать строку из класса House
        return f'Название: {self.name}, колличество этажей: {self.number_of_floors}'

h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

# __str__
print(h1)
print(h2)

# __len__
print(len(h1))
print(len(h2))
