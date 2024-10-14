# Различие атрибутов класса и экземпляра
class House:       # создаем класс
    houses_history = [] # создаем атрибут, который будет хранить названия созданных объектов.

    def __new__(cls, *args, **kwargs): # метод возвращает ссылку на класс House
        cls.houses_history.append(args[0])  # обращаемся к атрибуту houses_history и добавляем в список позиционный аргумент с нулевого индекса
        return object.__new__(cls) # вызываем метод new передавая ссылку cls


    def __init__(self, name, number_of_floors): # создаем метод внутри класса с атрибутами name, number_of_floors
        self.name = name                        # указываем на объект через self
        self.number_of_floors = number_of_floors


    def __del__(self):  # диструктор в нем определяется логика того что будет происходить когда наш объект перестанет существовать
        print(f'{self.name} снесён, но он останется в истории')


h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

# Удаление объектов
del h2
del h3

print(House.houses_history)

