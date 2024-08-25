from StrcturalPatterns.Adapter.Vehicle import Car, Bicycle

def equals(car:Car, bicycle:Bicycle):
    if car.__class__ == bicycle.__class__:
        return ("the values match")
    else:
        return ("values ​​do not match")

#Turns it into a bicycle
def convert(car:Car):
    print("-" * 40)
    instance = car
    instance.wheel = 2
    instance.brond = "Giant"
    instance.rudder = "Square"
    return Bicycle(instance.wheel, instance.brond, instance.rudder)

car = Car(4, "ferrari", "Round")
bicycle = Bicycle(2, "Giant", "square")

print(car)
print(bicycle)

instanceBicycle = convert(car)
print(instanceBicycle)

print(equals(car, bicycle))
print(equals(instanceBicycle, bicycle))
