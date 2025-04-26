# class heladeria():
#   sabor = "chocolate"
#   def otrosabor(self):
#     self.sabor = "vainilla"

# helado = heladeria()
# helado.otrosabor()
# print(helado.sabor)

class fabricaTelefonos():
  def __init__(self, marca, modelo):
    self.marca = marca
    self.modelo = modelo

telefono1 = fabricaTelefonos("lg", "g30")

print(telefono1.marca)