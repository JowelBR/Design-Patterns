class singleton:
    _instance = None 
    def __new__(cls, *args, **kwargs):
        if cls._instance == None:
            cls._instance = super(singleton, cls).__new__(cls)
        return cls._instance
    
    def __init__(self, value) -> None:
        if not hasattr(self, "isFirt"):
            self.value = value
            self.isFirt = True

s1 = singleton("First")
print(s1.value)

s2 = singleton("Second")
print(s2.value)

print(s1 is s2)