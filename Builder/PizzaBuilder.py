from pizza import Pizza

class PizzaBuilder():
    def setDough(self):
        pass

    def setSauce(self):
        pass

    def setTopping(self):
        pass


class MargheritaBuidler(PizzaBuilder):

    def __init__(self) -> None:
        self.pizza = Pizza()
    
    def setDough(self):
        self.pizza.dough = "regular"
    
    def setSauce(self):
        self.pizza.sauce = "tomato"
    
    def setTopping(self):
        self.pizza.topping = "Mozzarella"
    
