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

    # def make_human(make_function) -> Animal.Human:
    #     def insert_name(*args, **kwargs):
    #         pass
    #     return insert_name

    def make_animal(self, animal_species: str, name: str, age: int, sex: str, color: str, *args, **kwargs) -> Animal.Animal:
        if args != ():
            raise TypeError(f"Wrong number of arguments, {args} was excess")

        try:
            animal_to_use = self.define_animals[animal_species]
            sex_to_use = self.sexs[sex]
            color_to_use = self.colors[color]
        except KeyError as err:
            raise ValueError(f"Wrong argument: {err}") from err

        director = Director(animal_to_use, name, age, sex_to_use, color_to_use)
        builder = Builder.AnimalBuilder()
        director.build(builder, **kwargs)
        animal = builder.getResult()
        if animal_to_use not in self.animals:
            self.animals[animal_to_use] = [animal]
        else:
            self.animals[animal_to_use] += [animal]
        return animal

    def get_all_animals(self, animal_species: str = None, need_to_print: bool = True) -> list:
        if need_to_print:
            all_animals = ""
        animals_to_return = []
        if animal_species is None:
            for animal_class in self.animals:
                animals_to_return += self.animals[animal_class]
                if need_to_print:
                    all_animals += "\n".join(self.animals[animal_class]) + "\n"
            if need_to_print:
                print(all_animals, end="")
        else:
            try:
                animal_species = self.define_animals[animal_species]
            except KeyError as err:
                raise ValueError(f"Wrong argument: {err}") from err
            animals_to_return += self.animals[animal_species]
            if need_to_print:
                all_animals += "\n".join(self.animals[animal_species])
                print(all_animals)
        return animals_to_return


if __name__ == "__main__":  # pragma: no cover
    app = App()
    bob = app.make_human("Bob", 18, "m", "b", heads=2, chest=1, arms=4, legs=2, special_feature=1)
    app.make_human("Gob", 8, "f", "w")
    app.make_dog("Dob", 5, "m", "w")
    app.make_alien("Bod", 57, "", "")
    app.get_all_animals()
