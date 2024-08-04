import abc

class TextAbstract(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def paint(self):
        pass

class ButtonAbstract(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def paint(self):
        pass
