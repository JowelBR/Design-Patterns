from PizzaBuilder import MargheritaBuidler, PizzaBuilder

class Cook:
    def makePizza(self, builder:PizzaBuilder):
        builder.setDough()
        builder.setSauce()
        builder.setTopping()
        return builder.pizza
    
