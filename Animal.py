from Sex import Sex
from Color import Color


# Animals
class Animal:
    def __init__(self, name: str, age: int):
        if type(name) is not str:
            raise TypeError("Name should be string")
        if type(age) is not int:
            raise TypeError("Age should be integer")
        self.name = name
        self.age = age
        self.parts = []

    def set_sex(self, sex: Sex):
        if not isinstance(sex, Sex) and not issubclass(sex, Sex):
            raise TypeError(f"{sex} should be class Sex")
        self.sex = sex

    def set_color(self, color: Color):
        if not isinstance(color, Color) and not issubclass(color, Color):
            raise TypeError(f"{color} should be class Color")
        self.color = color

    def __str__(self) -> str:
        return f"{self.name} is {self.age} years old {self.sex} {self.color} {self.__class__.__name__.lower()}" + [f" with {', '.join(self.parts)}", ""][self.parts == []]


class Human(Animal):
    pass


class Dog(Animal):
    pass


class Alien(Animal):
    pass
