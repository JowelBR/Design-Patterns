from abc import ABC, abstractmethod

class employe(ABC):
    def __init__(self, name, position):
        self.name = name
        self.position = position
    
    @abstractmethod
    def showDetails(self):
        pass

class developer(employe):

    def __init__(self, name, position):
        super(developer, self).__init__(name, position)
    
    
    def showDetails(self):
        print(f"my name is {self.name} and my position is {self.position}")


class leadDeveloper(employe):
    def __init__(self, name, position):
        super().__init__(name, position)
        self.subordinates = []
    
    def add(self, employee):
        self.subordinates.append(employee)
    
    def remove(self, employee):
        self.subordinates.remove(employee)
    
    def showDetails(self):
        print(f"my name is {self.name} and my position is {self.position}")
        for subordinate in self.subordinates:
            subordinate.showDetails()

dev1 = developer("Joh BR", "backend")
dev2 = developer("Maria BR", "backend")

dev3 = developer("Anthony BR", "Frontend")
dev4 = developer("Perez BR", "Frontend")

lead1 = leadDeveloper("Andrew Petterson", "Manager Leed Developer Backend")
lead2 = leadDeveloper("Emily", "Manager Leed Developer Frontend")
lead3 = leadDeveloper("The Boss", "Manager Leed Developer ")

lead1.add(dev1)
lead1.add(dev2)

lead2.add(dev3)
lead2.add(dev4)

lead3.add(lead1)
lead3.add(lead2)

print("lead 1 -------------------->")
lead1.showDetails()
print("\nlead 2 -------------------->")
lead2.showDetails()
print("\nlead 3 -------------------->")
lead3.showDetails()