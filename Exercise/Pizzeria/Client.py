from ComboFactory import Combo1, Combo2

option = int(input("what combo do you want ? 1 or 2"))

def client() -> None:
    if(option >= 3 or option <= 0):
        print("option not exist")
    
    if(option == 1):
        pizza = Combo1().createPizza()
        guarnish = Combo1().createGuarnish()
        drink = Combo1().createDrink()

        print(pizza)
        print(drink)
        print(guarnish)
    
    if(option == 2):
        pizza = Combo2().createPizza()
        guarnish = Combo2().createGuarnish()
        drink = Combo2().createDrink()

        print(pizza)
        print(drink)
        print(guarnish)

client()