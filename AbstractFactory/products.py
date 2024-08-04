from ObjectsAbstract import TextAbstract, ButtonAbstract

class LightButton(ButtonAbstract):
    def paint(self):
        print("this is a light button")

class DarkButton(ButtonAbstract):
    def paint(self):
        print("this is a dark button")

class LightText(TextAbstract):
    def paint(self):
        print("this is a light text")

class DarkText(TextAbstract):
    def paint(self):
        print("This is a dark text")


