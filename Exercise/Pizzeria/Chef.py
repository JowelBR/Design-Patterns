from Pizzas import Chef, PizzaBase

def makePizza(oven:Chef) -> PizzaBase:
    oven.setDough()
    oven.setSauce()
    oven.setIngredents()
    return oven.pizza