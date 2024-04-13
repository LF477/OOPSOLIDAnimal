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

# Sex
class Sex:
    sex = "no sex"
    def __init__(self):
        pass
    
    def __str__(self) -> str:
        return self.sex

class SexMale(Sex):
    def __init__(self):
        self.sex = "male"

class SexFemale(Sex):
    def __init__(self):
        self.sex = "female"

# Animals
class Animal:
    def __init__(self, name:str, age:int):
        self.name = name
        self.age = age
    
    def set_sex(self, sex:Sex):
        self.sex = sex
    
    def set_color(self, color: Color):
        self.color = color
    
    def __str__(self) -> str:
        return f"{self.name} is {self.age} years old {self.sex} {self.color} {self.__class__.__name__.lower()}"

class Human(Animal):
    pass

class Dog(Animal):
    pass

class Alien(Animal):
    pass

# Builder
class AnimalBuilder:
    def __init__(self, species:Animal, name:str, age:int, sex:Sex, color:Color):
        self.check_types(species, name, age, sex, color)
        self.animal = species(name, age)
        self.build_animal(sex, color)
    
    def check_types(self, *args):
        list_of_needed_types = [Animal, str, int, Sex, Color]
        for index in range(len(list_of_needed_types)): # args
            arg = args[index]
            if (arg.__class__ is not type and not issubclass(arg.__class__, list_of_needed_types[index])) or (arg.__class__ is type and arg.__base__ is not object and not issubclass(arg.__base__, list_of_needed_types[index])):
                raise TypeError(f"{arg} must has wrong type")
        
            
    def build_animal(self, sex:Sex, color:Color):
        self.animal.set_sex(sex())
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
    

bob = AnimalBuilder(Human, "Bob", 18, SexMale, ColorBlack) 
print(bob)

dob = AnimalBuilder(Dog, "Dob", 5, SexMale, ColorWhite)
print(dob)

bod = AnimalBuilder(Alien, "Bod", 57, SexFemale, Color)
print(bod)