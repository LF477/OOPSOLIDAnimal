# Sex
class Sex:
    sex = "no sex"

    def __init__(self):  # pragma: no cover
        pass

    def __str__(self) -> str:
        return self.sex


class SexDontWantToUse(Sex):
    def __init__(self):
        self.sex = ""


class SexMale(Sex):
    def __init__(self):
        self.sex = "male"


class SexFemale(Sex):
    def __init__(self):
        self.sex = "female"


class SexOther(Sex):
    def __init__(self, sex: str = "other"):
        self.sex = sex
