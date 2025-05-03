def tripulacion(function):
  def funcion_modificada():
    print("🦜 Tripulación lista!")
    function()
  return funcion_modificada()

@tripulacion
def navegar():
  print("¡Zarpamos al Grand Line!")

@tripulacion
def comer_carne():
  print("¡A comer carne!")