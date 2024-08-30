from abc import ABC, abstractmethod

class Drink(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def cost(self):
        pass

class Coffee(Drink):
    def cost(self):
        return 5.0

class Soda(Drink):
    def cost(self):
        return 3.0

class DrinkDecorator(ABC):
    def __init__(self, drink: Drink):
        self._drink = drink

    @abstractmethod
    def cost(self):
        return self._drink.cost()

class Sugar(DrinkDecorator):
    def cost(self):
        return self._drink.cost() + 0.5

class MilkDecorator(DrinkDecorator):
    def cost(self) -> float:
        return self._drink.cost() + 1.5

coffee = Coffee()
coffee = MilkDecorator(coffee)
coffee = Sugar(coffee)

print(coffee.cost())