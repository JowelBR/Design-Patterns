from CarBase import Vehicle
from abc import abstractmethod, ABCMeta

class BuilderCar(metaclass=ABCMeta):
    
    @abstractmethod
    def setWheel(self):
        pass

    @abstractmethod
    def setColor(self):
        pass

    @abstractmethod
    def setDoors(self):
        pass

    @abstractmethod
    def setOld(self):
        pass

    @abstractmethod
    def setBrand(self):
        pass

class Ferrari(BuilderCar):
    def __init__(self) -> None:
        self.vehicle = Vehicle()
    
    def setWheel(self):
        self.vehicle.wheel = 4

    def setColor(self):
        self.vehicle.color = "Red"

    def setDoors(self):
        self.vehicle.doors = 4

    def setOld(self):
        self.vehicle.isOld = False

    def setBrand(self):
        self.vehicle.brand = "Ferrari"

class Bicycle(BuilderCar):
    def __init__(self) -> None:
        self.vehicle:Vehicle = Vehicle()
    
    def setWheel(self):
        self.vehicle.wheel = 2

    def setColor(self):
        self.vehicle.color = "Blue"

    def setDoors(self):
        self.vehicle.doors = 0

    def setOld(self):
        self.vehicle.isOld = False

    def setBrand(self):
        self.vehicle.brand = "BMC"