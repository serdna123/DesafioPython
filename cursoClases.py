class Cachorro():
    def __init__(self, nombre,juguete_favorito):
        self.nombre = nombre
        self.juguete_favorito = juguete_favorito
    def jugar (self):
        print(f"{self.nombre} esta jugando con {self.juguete_favorito}")

sakura = Cachorro("Sakura", "pelota")
sakura.jugar()
