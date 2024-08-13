from FactoryProducts import DarkFactory, LightFactory,FactoryAbstract

def client(factory:FactoryAbstract):
    button = factory.createButton()
    text = factory.createText()

    print(button.paint())
    print(text.paint())

client(DarkFactory())
print("-" *15)
client(LightFactory())
