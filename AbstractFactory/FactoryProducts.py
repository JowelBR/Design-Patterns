import abc

from products import (
    LightButton,
    DarkButton,
    LightText,
    DarkText
)

class FactoryAbstract(metaclass=abc.ABCMeta):
    
    @abc.abstractmethod
    def createButton():
        pass

    @abc.abstractmethod
    def createText():
        pass

class DarkFactory(FactoryAbstract):

    def createButton(self):
        return DarkButton()
    
    def createText(self):
        return DarkText()

class LightFactory(FactoryAbstract):

    def createButton(self):
        return LightButton()
    
    def createText(self):
        return LightText()
