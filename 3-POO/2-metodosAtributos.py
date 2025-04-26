class FabricaTelefonos():
  marca = "motorola"
  modelo = "g20"
  def linterna(self):
    print("linterna on")
  def mensaje(self):
    print("mensaje enviado")

telefono1 = FabricaTelefonos()
telefono1.marca
telefono1.modelo
print(telefono1.linterna())
print(telefono1.mensaje())