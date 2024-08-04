from __future__ import annotations
import abc

####ZONE FACTORY

class AbstractFactory(metaclass=abc.ABCMeta):
    
    @abc.abstractmethod
    def createA(self) -> AbstractA:
        pass

    @abc.abstractmethod
    def createB(self) -> AbstractB:
        pass

class FactoryConcrete1(AbstractFactory):
    
    def createA(self) -> AbstractA:
        return A1()

    def createB(self) -> AbstractB:
        return B1()

class FactoryConcrete2(AbstractFactory):
    
    def createA(self) -> AbstractA:
        return A2()

    def createB(self) -> AbstractB:
        return B2()

class FactoryConcrete3(AbstractFactory):
    
    def createA(self) -> AbstractA:
        return A3()

    def createB(self) -> AbstractB:
        return B3()

####ZONE A

class AbstractA(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def saludar(self):
        pass

class A1(AbstractA):
    
    def saludar(self):
        return "saludando desde a1"

class A2(AbstractA):
    
    def saludar(self):
        return "saludando desde a2"

class A3(AbstractA):
    def saludar(self):
        return "saludando desde A3"


###ZONE 

class AbstractB(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def saludar(self):
        pass

class B1(AbstractB):
    def saludar(self):
        return "saludando desde b1"


class B2(AbstractB):
    def saludar(self):
        return "saludando desde b2"

class B3(AbstractB):
    def saludar(self):
        return "saludando desde b3"

def clientCode(factory:AbstractFactory):
    productA = factory.createA()
    productB = factory.createB()

    print(productA.saludar())
    print(productB.saludar())


if __name__ == "__main__":
    clientCode(FactoryConcrete1())
    clientCode(FactoryConcrete2())
    clientCode(FactoryConcrete3())