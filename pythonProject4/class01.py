# 1. Абстракция
# 2. Инкапсуляция
# 3. Наследование
# 4. Полиморфизм

class Person:
    # def __new__(cls, *args, **kwargs):
    #     print('Создание класса Person')

    def __init__(self, name, age):
        self.__name = name
        self.__age = 1
        self.set_age(age)

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_age(self, age):
        if age < 0:
            self.__age = 1
        elif age > 140:
            self.__age = 1
        else:
            self.__age = age

    def get_age(self):
        return self.__age

    # def say(self, message):
    #     print(message)
    #
    def display(self):
        print(f'Имя: {self.get_name()}, возраст: {self.get_age()}')


tom = Person('Tom', 37)
tom.display()
tom.set_name('Tomas')
tom.set_age(24)
tom.display()

bob = Person('Bob', 55445)
bob.display()
