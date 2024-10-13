# Перегрузка операторов
class House:       # создаем класс
    def __init__(self, name, number_of_floors): # создаем метод внутри класса с атрибутами name, number_of_floors
        self.name = name                        # указываем на объект через self
        self.number_of_floors = number_of_floors

    def __len__(self):  # при вызове функции len будем возвращать колличество этажей
        return self.number_of_floors

    def __str__(self):  # при вызове функции str будет возвращать строку из класса House
        return f'Название: {self.name}, колличество этажей: {self.number_of_floors}'

    def __eq__(self, other):  # это оператор равенства
        return self.number_of_floors == other.number_of_floors

    def __lt__(self, other): # это оператор сравнения меньше чем
        return self.number_of_floors < other.number_of_floors

    def __le__(self, other): # это оператор сравнения меньше либо равно
        return self.number_of_floors <= other.number_of_floors

    def __gt__(self, other): # это оператор сравнения больше чем
        return self.number_of_floors > other.number_of_floors

    def __ge__(self, other): # это оператор сравнения больше либо равно
        return self.number_of_floors >= other.number_of_floors

    def __ne__(self, other): # это оператор определяет не равен ли один другому
        return self.number_of_floors != other.number_of_floors

    def __add__(self, value):  #обычное сложение увеличивает кол-во этажей на переданное значение value
        if isinstance (value, int): # убеждаемся в принадлежности value к типу int.
            self.number_of_floors += value  # прибавляем переданное значение value
            return self        # возвращаем self

    def __radd__(self, value):  #отраженное сложение значения value
        if isinstance (value, int): # убеждаемся в принадлежности value к типу int.
            self.number_of_floors += value  # прибавляем переданное значение value
            return self

    def __iadd__(self, value):  #сложение с присваиванием значения value
        if isinstance (value, int): # убеждаемся в принадлежности value к типу int.
            self.number_of_floors += value  # прибавляем переданное значение value
            return self

h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1)
print(h2)

print(h1 == h2) # __eq__

h1 = h1 + 10 # __add__
print(h1)
print(h1 == h2)

h1 += 10 # __iadd__
print(h1)

h2 = 10 + h2 # __radd__
print(h2)

print(h1 > h2) # __gt__
print(h1 >= h2) # __ge__
print(h1 < h2) # __lt__
print(h1 <= h2) # __le__
print(h1 != h2) # __ne__

#1. __eq__(self, other) - должен возвращать True, если количество этажей одинаковое у self и у other.
#2. Методы __lt__(<), __le__(<=), __gt__(>), __ge__(>=), __ne__(!=) должны присутствовать в классе и возвращать
# результаты сравнения по соответствующим операторам. Как и в методе __eq__ в сравнении участвует кол-во этажей.
#3. __add__(self, value) - увеличивает кол-во этажей на переданное значение value, возвращает сам объект self.
#4. __radd__(self, value), __iadd__(self, value) - работают так же как и __add__ (возвращают результат его вызова).