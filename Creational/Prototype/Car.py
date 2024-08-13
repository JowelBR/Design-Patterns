import copy

class CarPrototype:
    def __init__(self, wheel, color) -> None:
        self.wheel:int = wheel
        self.color:str = color
    
    def _clone(self):
        return copy.deepcopy(self)

    def __str__(self) -> str:
        return (
f"""{"-" * 25}
Wheel -> {self.wheel}
Color -> {self.color}""")

class ferrari(CarPrototype):
    def __init__(self, wheel, color) -> None:
        super().__init__(wheel, color)

class toyota(CarPrototype):
    def __init__(self, wheel, color) -> None:
        super().__init__(wheel, color)

ferrariOG = ferrari(4, "red")
ferrariClone = ferrariOG._clone()
ferrariClone.color = "blue"

print(ferrariOG)
print(ferrariClone)
