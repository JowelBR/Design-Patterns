from BuilderCar import BuilderCar

class Fabricator:
    def makeVehicle(self, Builder:BuilderCar) -> BuilderCar:
        Builder.setWheel()
        Builder.setOld()
        Builder.setBrand()
        Builder.setColor()
        Builder.setDoors()
        return Builder.vehicle
