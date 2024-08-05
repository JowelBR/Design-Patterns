class Vehicle():
    def __init__(self):
        self.wheel:int = None
        self.color:str = None
        self.doors:int = None
        self.isOld:bool = None
        self.brand:str = None
    
    def __str__(self) -> str:
        return (
f"""{"-" * 25}
Wheel -> {self.wheel}
Color -> {self.color}
Doors -> {self.doors}
Old   -> {self.isOld}
Brand -> {self.brand}""")