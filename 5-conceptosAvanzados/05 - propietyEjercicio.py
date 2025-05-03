class Zoro():
  def __init__(self):
    self.__espadas = "3 espadas"

  @property
  def espada(self):
    return self.__espadas

  @espada.setter
  def espada(self, cantidad):
    self.__espadas = f'{cantidad} espadas'

  @espada.deleter
  def espada(self):
    print("¡Zoro perdió sus espadas!")
    del self.__espadas

zoro = Zoro()
print(zoro.espada)   # 👉 3 espadas

zoro.espada = "2 espadas"
print(zoro.espada)   # 👉 2 espadas

del zoro.espada      # 👉 ¡Zoro perdió sus espadas!
