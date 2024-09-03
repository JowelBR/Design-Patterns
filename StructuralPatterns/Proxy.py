import abc

class Image(abc.ABC):
    @abc.abstractmethod
    def display(self):
        pass

class RealImage(Image):
    def __init__(self, file):
        self.file = file
        self.loadImage()
        
    def loadImage(self):
        print(f"Loading the image {self.file} ")
    
    def display(self):
        print(f"you are watching the {self.file}")

class proxy:
    def __init__(self, file) -> None:
        self.file = file
        self.image = None
    
    def load(self):
        if self.image is None:
            self.image = RealImage(self.file)
        return self.image.display()

proxyImage = proxy("photo.png")
proxyImage.load()