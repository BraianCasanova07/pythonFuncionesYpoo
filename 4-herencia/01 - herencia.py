class Persona: # Clase padre en la herencia
  def __init__(self, nombre, edad, nacionalidad):
    self.nombre = nombre
    self.edad = edad
    self.nacionalidad = nacionalidad

  def hablar(self):
    print(f'{self.nombre} esta hablando...')

class Empleado(Persona): #Clase hija en la herencia, hereda atributos y metodos de la clase padre
  def __init__(self, nombre, edad, nacionalidad, trabajo, salario):
    super().__init__(nombre, edad, nacionalidad) #super().__init__ sirve para usar atributos de la clase padre
    self.trabajo = trabajo
    self.salario = salario

class Estudiante(Persona):
  def __init__(self, nombre, edad, nacionalidad, universidad, notas):
    super().__init__(nombre, edad, nacionalidad)
    self.universidad = universidad
    self.notas = notas

class random(Persona):
  pass

estudiante1 = Estudiante('braian', 22, 'argentina', 'unab', 'regulares')
print(estudiante1.universidad)
estudiante1.hablar()
persona2 = random('braian', 22, 'argentina')
print(persona2.nombre)

