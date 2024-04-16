from Animal import Animal
from Sex import Sex
from Color import Color


# Builder
class Builder:   # pragma: no cover
    def __init__(self):
        pass

    def set_animal(self):
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
