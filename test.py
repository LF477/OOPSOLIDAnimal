class AnimalBuilder:
    def check_quantity(build_function):
        def check_positive(*args):
            if args[0] < 0:
                raise ValueError(f"{args[0]} should be positive")
            build_function(build_function.__class__, args[0])
        return check_positive

    @check_quantity
    def build_heads(self, quantity: int):
        print(f"quantity {quantity}")
        # if quantity < 0:
        #     raise ValueError(f"{quantity} should be positive")
        return f"{quantity} head" + ["", "s"][quantity > 1]


AnimalBuilder.build_heads(9)


from Director import Director
import Builder
import Animal
import Sex
import Color


sexs = {"male": Sex.SexMale, "m": Sex.SexMale, "female": Sex.SexFemale, "f": Sex.SexFemale, "": Sex.Sex}
colors = {"white": Color.ColorWhite, "w": Color.ColorWhite, "black": Color.ColorBlack, "b": Color.ColorBlack, "": Color.Color}
define_animals = {"human": Animal.Human, "dog": Animal.Dog, "alien": Animal.Alien, "h": Animal.Human, "d": Animal.Dog, "a": Animal.Alien}
animals = {}

def make_human(make_function) -> Animal.Human:
    def insert_name(*args, **kwargs):
        print(f"Human {args[0]}")
        return make_function
    return insert_name

def make_animal(animal_species: str, name: str, age: int, sex: str, color: str, *args, **kwargs) -> Animal.Animal:
    if args != ():
        raise TypeError(f"Wrong number of arguments, {args} was excess")

    try:
        animal_to_use = define_animals[animal_species]
        sex_to_use = sexs[sex]
        color_to_use = colors[color]
    except KeyError as err:
        raise ValueError(f"Wrong argument: {err}") from err

    director = Director(animal_to_use, name, age, sex_to_use, color_to_use)
    builder = Builder.AnimalBuilder()
    director.build(builder, **kwargs)
    animal = builder.getResult()
    if animal_to_use not in animals:
        animals[animal_to_use] = [animal]
    else:
        animals[animal_to_use] += [animal]
    return animal


def make_animal(make_function) -> Animal.Animal:
    print(f"make_animal {make_function}")
    def make(*args, **kwargs):
        print(f"Animal {args}, {kwargs}")
        try:
            args = (define_animals[args[0]], ) + args[1:]
            args = args[:3] + (sexs[args[3]], ) + args[4:]
            args = args[:4] + (colors[args[4]], ) + args[5:]
        except KeyError as err:
            raise ValueError(f"Wrong argument: {err}") from err
        print(f"Animal {args}, {kwargs}")

        animal = make_function(*args, **kwargs)

        if args[0] not in animals:
            animals[args[0]] = [animal]
        else:
            animals[args[0]] += [animal]
        return animal
    return make


@make_animal
def make_human(animal_species: str, name: str, age: int, sex: str, color: str, *args, **kwargs) -> Animal.Human:
    if args != ():
        raise TypeError(f"Wrong number of arguments, {args} was excess")

    director = Director(animal_species, name, age, sex, color)
    builder = Builder.AnimalBuilder()
    director.build(builder, **kwargs)
    animal = builder.getResult()
    return animal
    

make_human("human", "Bob", 18, "male", "black", heads=2, chest=1, arms=4, legs=2, special_feature=1)