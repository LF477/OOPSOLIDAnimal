from Builder import Builder
from Animal import Animal
from Sex import Sex
from Color import Color


class Director:
    def __init__(self, species: Animal, name: str, age: int, sex: Sex, color: Color):
        self.animal = species(name, age)
        self.sex = sex
        self.color = color

    def build(self, builder: Builder, **kwargs):
        builder.set_animal(self.animal)
        builder.build_animal(self.sex, self.color)
        builder.build_heads(kwargs["heads"] if "heads" in kwargs else kwargs["head"] if "head" in kwargs else 1)
        builder.build_chests(kwargs["chests"] if "chests" in kwargs else kwargs["chest"] if "chest" in kwargs else 1)
        builder.build_arms(kwargs["arms"] if "arms" in kwargs else kwargs["arm"] if "arm" in kwargs else 2)
        builder.build_legs(kwargs["legs"] if "legs" in kwargs else kwargs["leg"] if "leg" in kwargs else 2)
        builder.build_special_features(kwargs["special_features"] if "special_features" in kwargs else kwargs["special_feature"] if "special_feature" in kwargs else 0)
