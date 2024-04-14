# Colors
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
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        self.parts = []

    def set_sex(self, sex: Sex):
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
class Builder:
    def __init__(self):
        pass

    def build_animal(self):
        pass

    def build_heads(self):
        pass

    def build_chests(self):
        pass

    def build_arms(self):
        pass

    def build_legs(self):
        pass

    def build_special_features(self):
        pass


class AnimalBuilder(Builder):
    def set_animal(self, animal: Animal):
        self.animal = animal

    def build_animal(self, sex: Sex, color: Color):
        self.animal.set_sex(sex())
        self.animal.set_color(color())

    def build_heads(self, quantity: int):
        self.animal.heads = f"{quantity} head" + ["", "s"][quantity > 1]
        self.animal.parts += [self.animal.heads]
        # raise NotImplementedError

    def build_chests(self, quantity: int):
        self.animal.chests = f"{quantity} chest" + ["", "s"][quantity > 1]
        self.animal.parts += [self.animal.chests]
        # raise NotImplementedError

    def build_arms(self, quantity: int):
        self.animal.arms = f"{quantity} arm" + ["", "s"][quantity > 1]
        self.animal.parts += [self.animal.arms]
        # raise NotImplementedError

    def build_legs(self, quantity: int):
        self.animal.legs = f"{quantity} leg" + ["", "s"][quantity > 1]
        self.animal.parts += [self.animal.legs]
        # raise NotImplementedError

    def build_special_features(self, quantity: int):
        self.animal.special_features = f"{quantity} special feature" + ["", "s"][quantity > 1]
        self.animal.parts += [self.animal.special_features]
        # raise NotImplementedError

    def getResult(self):
        return str(self) + f" with {', '.join(self.animal.parts)}"

    def __str__(self) -> str:
        return str(self.animal)


class Director:
    def __init__(self, species: Animal, name: str, age: int, sex: Sex, color: Color):
        self.check_types(species, name, age, sex, color)
        self.animal = species(name, age)
        self.sex = sex
        self.color = color

    def check_types(self, *args):
        list_of_needed_types = [Animal, str, int, Sex, Color]
        for index in range(len(list_of_needed_types)):  # args
            arg = args[index]
            if arg.__class__ is not type:
                if not issubclass(arg.__class__, list_of_needed_types[index]):
                    raise TypeError(f"{arg} must has wrong type")
            else:
                if arg.__base__ is not object:
                    if not issubclass(arg.__base__, list_of_needed_types[index]):
                        raise TypeError(f"{arg} must has wrong type")

    def build(self, builder: AnimalBuilder, **kwargs):
        builder.set_animal(self.animal)
        builder.build_animal(self.sex, self.color)
        builder.build_heads(kwargs["heads"] if "heads" in kwargs else kwargs["head"] if "head" in kwargs else 1)
        builder.build_chests(kwargs["chests"] if "chests" in kwargs else kwargs["chest"] if "chest" in kwargs else 1)
        builder.build_arms(kwargs["arms"] if "arms" in kwargs else kwargs["arm"] if "arm" in kwargs else 2)
        builder.build_legs(kwargs["legs"] if "legs" in kwargs else kwargs["leg"] if "leg" in kwargs else 2)
        builder.build_special_features(kwargs["special_features"] if "special_features" in kwargs else kwargs["special_feature"] if "special_feature" in kwargs else 0)


class App:
    def __init__(self):
        self.sexs = {"male": SexMale, "m": SexMale, "female": SexFemale, "f": SexFemale}
        self.colors = {"white": ColorWhite, "w": ColorWhite, "black": ColorBlack, "b": ColorBlack}
        self.animals = {}

    def make_human(self, name: str, age: int, sex: str, color: str, *args, **kwargs) -> Human:
        if args != ():
            raise TypeError(f"Wrong number of arguments, {args} was excess")
        director = Director(Human, name, age, self.sexs[sex] if sex in self.sexs else Sex, self.colors[color] if color in self.colors else Color)
        builder = AnimalBuilder()
        director.build(builder, **kwargs)
        human = builder.getResult()
        if Human not in self.animals:
            self.animals[Human] = [human]
        else:
            self.animals[Human] += [human]
        return human

    def make_dog(self, name: str, age: int, sex: str, color: str) -> Dog:
        director = Director(Dog, name, age, self.sexs[sex] if sex in self.sexs else Sex, self.colors[color] if color in self.colors else Color)
        builder = AnimalBuilder()
        director.build(builder)
        dog = builder.getResult()
        if Dog not in self.animals:
            self.animals[Dog] = [dog]
        else:
            self.animals[Dog] += [dog]
        return dog

    def make_alien(self, name: str, age: int, sex: str, color: str) -> Alien:
        director = Director(Alien, name, age, self.sexs[sex] if sex in self.sexs else Sex, self.colors[color] if color in self.colors else Color)
        builder = AnimalBuilder()
        director.build(builder)
        alien = builder.getResult()
        if Alien not in self.animals:
            self.animals[Alien] = [alien]
        else:
            self.animals[Alien] += [alien]
        return alien

    def get_all_animals(self, animal: Animal = None, need_to_print: bool = True) -> list:
        if need_to_print:
            all_animals = ""
        animals_to_return = []
        if animal is None:
            for animal in self.animals:
                animals_to_return += self.animals[animal]
                if need_to_print:
                    all_animals += "\n".join(self.animals[animal]) + "\n"
            if need_to_print:
                print(all_animals, end="")
        else:
            animals_to_return += self.animals[animal]
            if need_to_print:
                all_animals += "\n".join(self.animals[animal])
                print(all_animals)
        return animals_to_return


if __name__ == "__main__":
    app = App()
    bob = app.make_human("Bob", 18, "m", "b", heads=2, chest=1, arms=4, legs=2, special_feature=1)
    app.make_human("Gob", 8, "f", "w")
    app.make_dog("Dob", 5, "m", "w")
    app.make_alien("Bod", 57, "", "")
    app.get_all_animals()
