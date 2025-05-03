class Animal:
  def comer(self):
    print(f"el animal esta comiendo")
class Mamifero(Animal):
  def amamantar(self):
    print('el animal esta amamantando')
class Ave(Animal):
  def volar(self):
    print('el animal esta volando')

class Murcielago(Mamifero, Ave):
  pass

murcielago = Murcielago()

murcielago.comer()
murcielago.amamantar()
murcielago.volar()