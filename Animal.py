# Colors
from typing import Any


class Color:
    color = "no color"
    
    def __init__(self):
        pass
    
    def __str__(self) -> str:
        return self.color

class ColorWhite(Color):
    def __init__(self):
        self.color = "white"

class ColorBlack(Color):
    def __init__(self):
        self.color = "black"

# Animals
class Animal:
    def __init__(self, name:str, age:int):
        self.name = name
        self.age = age
    
    def set_color(self, color: Color):
        self.color = color
    
    def __str__(self) -> str:
        return f"{self.name} is {self.age} years old {self.color} {self.__class__.__name__.lower()}"

class Human(Animal):
    pass

class Dog(Animal):
    pass

class Alien(Animal):
    pass

# Builder
class AnimalBuilder:
    def __init__(self, name:str, age:int, species:Animal, color:Color):
        self.animal = species(name, age)
        self.build_animal(color)
        
    def build_animal(self, color:Color):
        self.animal.set_color(color())
    
    def build_head(self):
        raise NotImplementedError
    
    def build_chest(self):
        raise NotImplementedError
        
    def build_arms(self):
        raise NotImplementedError

    def build_legs(self):
        raise NotImplementedError
    
    def build_special_features(self):
        raise NotImplementedError

    def __str__(self) -> str:
        return str(self.animal)

bob = AnimalBuilder("Bob", 18, Human, ColorBlack)
print(bob)

dob = AnimalBuilder("Dob", 5, Dog, ColorWhite)
print(dob)

bod = AnimalBuilder("Bod", 57, Alien, Color)
print(bod)