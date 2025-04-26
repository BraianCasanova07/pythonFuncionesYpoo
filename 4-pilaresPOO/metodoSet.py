class A():
  def __init__(self):
    self._contador = 0
    self._cuenta = 0

  @property # le quita el ()
  def cuenta(self): # es el metodo get, es hacer un metodo con el mismo nombre del atributo
    return self._cuenta

  @cuenta.setter
  def cuenta(self, cuenta):
    self._cuenta = cuenta

  @property
  def contador(self):
    return self._contador

a = A()
# a.contador = 5
# print(a._cuenta)
a.cuenta = 5
print(a.cuenta)