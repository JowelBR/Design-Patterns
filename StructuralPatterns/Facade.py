class DVDPlayer:
    def on(self):
        print("DVD Player is ON")

    def play(self, movie:str):
        print(f"Playing: {movie}")

class Amplifier:
    def on(self):
        print("Amplifier is ON")

    def setVolume(self, volumen:int):
        print(f"Setting volumen to {volumen}")

class Projector:
    def on(self):
        print("Projector is ON")
    
    def wideScreenMode(self):
        print("Projector is set to widescreen mode")

class Home:
    def __init__(self, DVD:DVDPlayer, amplifier:Amplifier, projector:Projector) -> None:
        self.dvd = DVD
        self.amplifier = amplifier
        self.projector = projector
    
    def watchMovie(self, movie:str):
        print("Get ready to watch a movie...")
        self.dvd.on()
        self.amplifier.on()
        self.projector.on()
        self.amplifier.setVolume(50)
        self.projector.wideScreenMode()
        self.dvd.play(movie)
        return ""

dvd_player = DVDPlayer()
amplifier = Amplifier()
projector = Projector()

home = Home(dvd_player, amplifier, projector)
home.watchMovie("Scott Pilgrim")