# El polimorfismo es el mismo metodo para los objetos pero estos tienen distintos comportamientos según el objeto
class Luffy:
    def atacar(self):
        print("Luffy lanza un Gomu Gomu no Pistol! 💥")

class Zoro:
    def atacar(self):
        print("Zoro usa su Santoryu: Oni Giri! ⚔️")

class Sanji:
    def atacar(self):
        print("Sanji da una patada con Diable Jambe! 🔥")

# Lista de piratas
lufy = Luffy()
zoro = Zoro()
sanji = Sanji()

sanji.atacar()
