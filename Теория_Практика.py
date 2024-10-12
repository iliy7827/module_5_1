class Human:
    def __init__(self, name, age):  #__init__ конструктор для создания объекта класса
        self.name = name            # в нашем случае есть два объекта den и max
        self.age = age

    def say_info(self):
        print(f'Привет, меня зовут {self.name}, мне {self.age}')

    def birthday(self):
        self.age += 1
        print(f'У меня день рождения, теперь мне {self.age}')

    def __len__(self): # при вызове функции лен будем возвращать возраст человека
        return self.age

    def __del__(self): # диструктор в нем определяется логика того что будет происходить когда наш объект перестанет существовать
        print(f'{self.name} ушел')

den = Human('Денис', 23) #Имя den ведет на объект класса Human которое содержало отрибуты name и age
max = Human('Максим',34)
print(len(den))
print(len(max))
den.say_info()
max.say_info()
den.birthday()
max.birthday()
print(len(den))
print(len(max))