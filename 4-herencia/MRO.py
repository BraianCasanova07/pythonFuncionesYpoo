#el MRO (method resolution order) es basicamente el orden en que se toma la herencia en python, primero si tenes un atributo o metodo en la misma clase toma ese, y si tenes varias clases heredadas va por la primera y si no por la segunda, y si no va por la clase madre de la herencia (si es que comparten clase madre), si no comparten clase madre heredaria primero la clase madre de la primera clase, y si no va por la segunda clase y su clase madre de no tener nada

# D > B > C > A (si b y c comparten herencia)
# D > B > A > C > F (si b y c no comparten herencia)

class A:
  def hablar(self):
    print('Hola desde A')

class F:
  def hablar(self):
    print('Hola desde F')

class B(A):
  pass

class C(F):
  def hablar(self):
    print('Hola desde C')

class D(B, C):
  def hablar(self):
    print('Hola desde D')

d = D()
C.hablar(d)

print(D.mro())