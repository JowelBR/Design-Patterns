from abc import ABCMeta, abstractmethod
import copy

class BaseDrink(metaclass=ABCMeta):

    @abstractmethod
    def content(self) -> int:
        pass

    @abstractmethod
    def type(self) -> str:
        pass

    def _clone(self) -> str:
        return copy.deepcopy(self)

    def __str__(self):
        return f"it has {self.content()} Ml and is {self.type()}"

class Soda(BaseDrink):

    def content(self) -> int:
        return 250
    
    def type(self) -> str:
        return "Soda"

class Juice(BaseDrink):

    def content(self) -> int:
        return 190
    
    def type(self) -> str:
        return "Orange Juice"