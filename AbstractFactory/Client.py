from FactoryProducts import DarkFactory, LightFactory

### Dark ZONE
darkFactory:DarkFactory = DarkFactory() #instanciate Dark Factory

button = darkFactory.createButton()
button.paint()
text = darkFactory.createText()
text.paint()


print("-" * 15)


###Light ZONE
lightFactory:LightFactory = LightFactory() #instanciate Light Factory

button = lightFactory.createButton()
button.paint()
text = lightFactory.createText()
text.paint()