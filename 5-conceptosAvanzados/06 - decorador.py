def decorador(funcion): #Los decoradores modifican una funcion y le agregan funcionalidades antes y/o despues
  def funcion_modificada():
    print("antes de llamar a la funcion")
    funcion()
    print("despues de llamar a la funcion")
  return funcion_modificada

@decorador
def saludo():
  print("Hola braian")

saludo()