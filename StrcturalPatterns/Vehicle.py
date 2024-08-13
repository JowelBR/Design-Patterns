class Car:
    def __init__(self, wheels, brond, rudder) -> None:
        self.brond = brond
        self.wheel = wheels
        self.rudder = rudder
    
    def  __str__(self):
        return f"""
Wheels   ->    {self.wheel}
Brond    ->    {self.brond}
Rudder   ->    {self.rudder}
"""

class Bicycle:
    def __init__(self, wheels, brond, rudder) -> None:
        self.brond = brond
        self.wheel = wheels
        self.rudder = rudder
    
    def  __str__(self):
        return f"""
Wheels   ->    {self.wheel}
Brond    ->    {self.brond}
Rudder   ->    {self.rudder}
"""