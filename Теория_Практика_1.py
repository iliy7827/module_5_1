class Human:
# __init__ конструктор

    head = True

    def __init__(self, name, age):  #__init__ конструктор для создания объекта класса
        self.name = name            # в нашем случае есть два объекта den и max
        self.age = age

    def __str__(self): #Определяет строковое значение нашего объекта
        return f'{self.name}'

    def say_info(self):
        print(f'Привет, меня зовут {self.name}, мне {self.age}')

    def birthday(self):
        self.age += 1
        print(f'У меня день рождения, теперь мне {self.age}')

    def __len__(self): # при вызове функции лен будем возвращать возраст человека
        return self.age

# это те методы которые позволяют перегружать стандартные операторы, для сравнения одного значения с другим
    def __lt__(self, other): # это оператор сравнения меньше чем
        return self.age < other.age # если истина то выведет True если нет то False

    def __gt__(self, other): # это оператор сравнения больше чем
        return self.age > other.age # если истина то выведет True если нет то False

    def __eq__(self, other):  # это оператор равенства
        return self.name == other.name and self.age == other.age # сравниваем имена и возраст будет False потому-что разные имена

# проверяет истинно или не истинно
    def __bool__(self):
        return bool(self.age)

# диструктор
    def __del__(self): # диструктор в нем определяется логика того что будет происходить когда наш объект перестанет существовать
        print(f'{self.name} ушел')

den = Human('Денис', 23) #Имя den ведет на объект класса Human которое содержало отрибуты name и age
max = Human('Максим',34)
a = 6
print(max)
print(Human.head)
#if den:
#    den.say_info()
#print(len(den))
#print(len(max))
#den.say_info()
#max.say_info()
#den.birthday()
#max.birthday()
#print(den < max)
#print(den == max)
