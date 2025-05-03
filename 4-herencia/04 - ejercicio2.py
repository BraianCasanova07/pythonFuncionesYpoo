class Persona:
  def __init__(self, nombre, edad):
    self.nombre = nombre
    self.edad = edad

  def datos(self):
    print(f'''
    nombre : {self.nombre}
    edad : {self.edad}
''')

class Estudiante(Persona):
  def __init__(self, nombre, edad, grado):
    super().__init__(nombre, edad)
    self.grado = grado

  def mostrar_grado(self):
    print(f"grado del estudiante: {self.grado}")

estudiante = Estudiante("braian", 22, 2)

estudiante.datos()
estudiante.mostrar_grado()