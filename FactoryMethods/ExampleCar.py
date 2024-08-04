from __future__ import annotations
from abc import ABCMeta, abstractmethod

class car(metaclass=ABCMeta):

    @abstractmethod
    def typeCar(self):
        pass

    def result(self):
        return f"you are driving with a {self.typeCar()}"

class Toyota(car):

    def typeCar(self):
        return self.__class__.__qualname__

class Honda(car):

    def typeCar(self):
        return self.__class__.__qualname__


class FactoryAbstract(metaclass=ABCMeta):
    @abstractmethod
    def createCar(self):
        pass

class FactoryToyota(FactoryAbstract):
    def createCar(self):
        return Toyota()

class FactoryHonda(FactoryAbstract):
    def createCar(self):
        return Honda()

def client(factory):
    car = factory.createCar()
    print(car.result())

client(FactoryHonda())
client(FactoryToyota())