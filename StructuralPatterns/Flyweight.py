import abc

class Chair(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def position(self, x, y):
        pass

class ConcreteChair(Chair):
    def __init__(self, chairType) -> None:
        super().__init__()
        self._chairType = chairType
    
    def position(self, x, y):
        print(f"the position to {self._chairType} chair at ({x}, {y})")

class FactoryChair:
    _chairs = {}

    @staticmethod
    def buildChair(chairType):
        if chairType not in FactoryChair._chairs:
            FactoryChair._chairs[chairType] = ConcreteChair(chairType)
        return FactoryChair._chairs[chairType]

def customerClient():
    chairs:list[ConcreteChair] = [
        FactoryChair.buildChair("mahogany"),
        FactoryChair.buildChair("oak"),
        FactoryChair.buildChair("pine"),
        FactoryChair.buildChair("Birch"),
        FactoryChair.buildChair("mahogany"),
        FactoryChair.buildChair("oak"),
        FactoryChair.buildChair("pine"),
    ]

    for index, chair in enumerate(chairs):
        chair.position(index * 10, index * 10)

customerClient()