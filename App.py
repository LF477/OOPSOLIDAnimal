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


if __name__ == "__main__":  # pragma: no cover
    app = App()
    bob = app.make_human("Bob", 18, "m", "b", heads=2, chest=1, arms=4, legs=2, special_feature=1)
    app.make_human("Gob", 8, "f", "w")
    app.make_dog("Dob", 5, "m", "w")
    app.make_alien("Bod", 57, "", "")
    app.get_all_animals()
