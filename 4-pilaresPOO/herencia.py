class Animales():
  def habla(self):
    print("yo soy un animal")

  def descripcion(self):
    print(f"yo soy un {self.animal}")

class Perro(Animales):
  pass

class Abeja(Animales):
  def __init__(self, animal):
    self.animal = animal

animal = Animales()
animal.habla()

perro = Perro()
perro.habla()

abeja = Abeja("abejin")
abeja.descripcion()