class PersonAgeException(Exception):
    def __init__(self, age, minage, maxage):
        self.age = age
        self.minage = minage
        self.maxage = maxage

    def __str__(self):
        return f'Недопустимое значение {self.age}. \nВозраст должен быть в диапазоне от {self.minage} до {self.maxage}'


class Person:
    def __init__(self, name, age):
        self._name = name
        minage = 1
        maxage = 110
        if minage < age < maxage:
            self._age = age
        else:
            raise PersonAgeException(age, minage, maxage)

    def display_info(self):
        print(f'Имя: {self._name}, возраст: {self._age}')

try:
    tom = Person('Tom', 37)
    tom.display_info()
    bob = Person('Bob', -5)
    bob.display_info()
except PersonAgeException as e:
    print(e)
    print(e)