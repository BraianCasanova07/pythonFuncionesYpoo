class A():
  def __init__(self):
    self.contador = 0
  def incrementar(self):
    self.contador += 1
  def cuenta(self):
    return self.contador

a = A()
print(a.cuenta())
a.incrementar()
print(a.cuenta())
print(a.contador)

class B():
  def __init__(self):
    self.__contador = 0
  def incrementar(self):
    self.__contador += 1
  def cuenta(self):
    return self.__contador

b = B()
print(b.cuenta())
b.incrementar()
print(b.cuenta())
print(b.__contador)

class C(): #con un solo _ no lockea pero documenta el codigo para que otro sepa que no debe tocar los atributos
  def __init__(self):
    self._contador = 0
  def incrementar(self):
    self._contador += 1
  def cuenta(self):
    return self._contador

c = C()
print(c.cuenta())
c.incrementar()
print(c.cuenta())
print(c._contador)