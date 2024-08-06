from PizzaBuilder import PizzaBuilder

class Cook:
    def makePizza(self, builder:PizzaBuilder):
        builder.setDough()
        builder.setSauce()
        builder.setTopping()
        return builder.pizza
    
