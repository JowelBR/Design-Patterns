class Car:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance == None:
            cls._instance = super(Car, cls).__new__(cls)
        return cls._instance
    
    def __init__(self, wheel, color, brond) -> None:
        if not hasattr(self, "isFirts"):
            self.isFirts = True
            self.wheel = wheel
            self.color = color
            self.brond = brond

car1 = Car(4, "red", "ferrari")
car2 = Car(4, "blue", "Lambo")

def showParams(obj:Car):
    aux = obj.__dict__["isFirts"]
    del obj.__dict__["isFirts"]
    
    for key, value in obj.__dict__.items():
        print(f"{key}   --->   {value}")
    obj.__dict__["isFirts"] = aux
    
    print("-" * 30)

showParams(car1)
showParams(car2)