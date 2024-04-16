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


