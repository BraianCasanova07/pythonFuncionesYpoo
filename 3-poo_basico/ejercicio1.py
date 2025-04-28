class Estudiante:
  def __init__(self, nombre, edad, grado):
    self.nombre = nombre
    self.edad = edad
    self.grado = grado

nombre = input('Dame tu nombre: ')
edad = input('Dame tu edad: ')
grado = input('Dame tu grado: ')

Alumno1 = Estudiante(nombre, edad, grado)

print(f'''
  Datos del estudiante:
      nombre : {Alumno1.nombre}
      edad : {Alumno1.edad}
      grado : {Alumno1.grado}
''')

while True:
  estudiar = input()
  if (estudiar.lower() == "estudiar"):
    print("Estudiando...")
