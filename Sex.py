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


