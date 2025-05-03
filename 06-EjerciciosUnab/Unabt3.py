class Persona():
  def __init__(self, nombre, edad):
    self.nombre = nombre
    self.edad = edad
  def hablar(self):
    print('estoy hablando...')
  def presentarse(self):
    print(f'hola soy {self.nombre} y tengo {self.edad} años')

class Rapero(Persona):
  def __init__(self, nombre, edad, dinero, viralidad):
    super().__init__(nombre, edad)
    self.__dinero = dinero
    self.viralidad = viralidad

  @property
  def ostentar(self):
    print(f'tengo todo este dinero: {self.__dinero}')

  def fama(self):
    print(f'soy famoso? {self.viralidad}')

  def presentarse(self):  # sobrescribimos el método
    print(f"Yo soy {self.nombre}, tengo {self.edad} años y escupo fuego en mis rimas 🔥")

pepe = Persona("pepe", 22)
pepe.presentarse()
pepe.hablar()

maria = Persona("maria", 25)
maria.presentarse()
maria.hablar()

misterMC = Rapero('mauro', 23, 250.000, True)
misterMC.presentarse()
misterMC.hablar()
misterMC.ostentar
misterMC.fama()

potatoMC = Rapero('sebastian', 40, 0, False)
potatoMC.presentarse()
potatoMC.hablar()
potatoMC.ostentar
potatoMC.fama()

# Cumple con los 4 pilares