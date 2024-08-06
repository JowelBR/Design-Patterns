from Chef import makePizza
from Pizzas import PizzaCheese, PizzaPepperoni, PizzaBase
from Drinks import Juice, Soda, BaseDrink
from Guarnish import Potato, Hamburger, GuarnishBase
from abc import ABCMeta, abstractmethod

"1 -> pizzapepproni + Soda + Potato"
"2 -> PizzaCheese + Juice + Hamburguer"

class Factory(metaclass=ABCMeta):

    @abstractmethod
    def createPizza(self) -> PizzaBase:
        pass

    @abstractmethod
    def createGuarnish(self) -> GuarnishBase:
        pass

    @abstractmethod
    def createDrink(Self) -> BaseDrink:
        pass

class Combo1(Factory):
    def createPizza(self) -> PizzaBase:
        return makePizza(PizzaPepperoni())
    
    def createGuarnish(self) -> GuarnishBase:
        return Potato()
    
    def createDrink(Self) -> BaseDrink:
        return Soda()

class Combo2(Factory):

    def createPizza(self) -> PizzaBase:
        return makePizza(PizzaCheese())
    
    def createGuarnish(self) -> GuarnishBase:
        return Hamburger()
    
    def createDrink(Self) -> BaseDrink:
        return Juice()

