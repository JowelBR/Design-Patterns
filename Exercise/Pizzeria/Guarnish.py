import abc
import copy

class GuarnishBase(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def type(self) -> str:
        pass

    def _clone(self) -> str:
        return copy.deepcopy(self)

    def __str__(self) -> str:
        return f"I am a {self.type()}"

class Potato(GuarnishBase):
    def type(self) -> str:
        return "Potato"

class Hamburger(GuarnishBase):
    def type(self) -> str:
        return "Hamburguer"