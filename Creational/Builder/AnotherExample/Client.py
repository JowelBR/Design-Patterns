from ManufactureVehicle import Fabricator
from BuilderCar import Bicycle, Ferrari

fabricator:Fabricator = Fabricator()
car:Ferrari = fabricator.makeVehicle(Ferrari())
bicycle:Bicycle = fabricator.makeVehicle(Bicycle())

print(bicycle)
print(car)