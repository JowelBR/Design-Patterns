from ObjectsAbstract import TextAbstract, ButtonAbstract

class LightButton(ButtonAbstract):
    def paint(self):
        return ("this is a light button")

class DarkButton(ButtonAbstract):
    def paint(self):
        return ("this is a dark button")

class LightText(TextAbstract):
    def paint(self):
        return ("this is a light text")

class DarkText(TextAbstract):
    def paint(self):
        return ("This is a dark text")


