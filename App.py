from Director import Director
import Builder
import Animal
import Sex
import Color


class App:
    def __init__(self):
        self.sexs = {"male": Sex.SexMale, "m": Sex.SexMale, "female": Sex.SexFemale, "f": Sex.SexFemale, "": Sex.Sex}
        self.colors = {"white": Color.ColorWhite, "w": Color.ColorWhite, "black": Color.ColorBlack, "b": Color.ColorBlack, "": Color.Color}
        self.define_animals = {"human": Animal.Human, "dog": Animal.Dog, "alien": Animal.Alien, "h": Animal.Human, "d": Animal.Dog, "a": Animal.Alien}
        self.animals = {}

    def make_animal(make_function) -> Animal.Animal:
        # print(f"make_animal {make_function}")

        def make(*args, **kwargs):
            # print(f"Animal {args}, {kwargs}")
            try:
                args = args[:3] + (args[0].sexs[args[3]], ) + args[4:]
                args = args[:4] + (args[0].colors[args[4]], ) + args[5:]
            except KeyError as err:
                raise ValueError(f"Wrong argument: {err}") from err
            # print(f"Animal {args}, {kwargs}")

            director = make_function(*args)

            builder = Builder.AnimalBuilder()
            director.build(builder, **kwargs)
            animal = builder.getResult()

            if animal.__class__ not in args[0].animals:
                args[0].animals[animal.__class__] = [animal]
            else:
                args[0].animals[animal.__class__] += [animal]
            return animal
        return make

    @make_animal
    def make_human(self, name: str, age: int, sex: str, color: str, *args) -> Animal.Human:
        if args != ():
            raise TypeError(f"Wrong number of arguments, {args} was excess")

        return Director(Animal.Human, name, age, sex, color)

    @make_animal
    def make_dog(self, name: str, age: int, sex: str, color: str, *args) -> Animal.Dog:
        if args != ():
            raise TypeError(f"Wrong number of arguments, {args} was excess")

        return Director(Animal.Dog, name, age, sex, color)

    @make_animal
    def make_alien(self, name: str, age: int, sex: str, color: str, *args) -> Animal.Alien:
        if args != ():
            raise TypeError(f"Wrong number of arguments, {args} was excess")

        return Director(Animal.Alien, name, age, sex, color)

    def get_list_with_string_type(self, animal_species: Animal) -> list:
        list_with_string_type = []
        for animal in self.animals[animal_species]:
            list_with_string_type += [str(animal)]
        return list_with_string_type

    def get_all_animals(self, animal_species: str = None, need_to_print: bool = True) -> list:
        if need_to_print:
            all_animals = ""
        animals_to_return = []

        if animal_species is None:
            for animal_class in self.animals:
                animals_to_return += self.animals[animal_class]
                if need_to_print:
                    all_animals += "\n".join(self.get_list_with_string_type(animal_class)) + "\n"
            if need_to_print:
                print(all_animals, end="")
        else:
            try:
                animal_species = self.define_animals[animal_species.lower()]
            except KeyError as err:
                raise ValueError(f"Wrong argument: {err}") from err
            animals_to_return += self.animals[animal_species]
            if need_to_print:
                all_animals += "\n".join(self.get_list_with_string_type(animal_species))
                print(all_animals)
        return animals_to_return


if __name__ == "__main__":  # pragma: no cover
    app = App()
    bob = app.make_human("Bob", 18, "m", "b", heads=2, chest=1, arms=4, legs=2, special_feature=1)
    app.make_human("Gob", 8, "f", "w")
    app.make_dog("Dob", 5, "m", "w")
    app.make_alien("Bod", 57, "", "")
    app.get_all_animals()
