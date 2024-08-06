import copy

"I will implement 3 design pattern and are: Prototipe, Builder"

class PizzaBase:
    def __init__(self) -> None:
        self.douhg = ''
        self.sauce = ''
        self.ingredients = []
    
    def _clone(self):
        return copy.deepcopy(self)
    
    def __str__(self) -> str:
        return f""" {"-" * 35 }
{self.douhg}
{self.sauce}
{self.ingredients}"""

class Chef:
    
    def setDough(self):
        pass

    def setSauce(self):
        pass

    def setIngredents(self):
        pass

class PizzaPepperoni(Chef):
    def __init__(self):
        self.pizza = PizzaBase()
    
    def setDough(self):
        self.pizza.douhg = "Regular"
    
    def setSauce(self):
        self.pizza.sauce = "Tomato"

    def setIngredents(self):
        self.pizza.ingredients = ["Cheese", "Basil"]

class PizzaCheese(Chef):
    def __init__(self):
        self.pizza = PizzaBase()
    
    def setDough(self):
        self.pizza.douhg = "Regular with cheese border"
    
    def setSauce(self):
        self.pizza.sauce = "Tomato"

    def setIngredents(self):
        self.pizza.ingredients = ["ham", "meat"]

