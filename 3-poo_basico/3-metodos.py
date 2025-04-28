class Celular:
  def __init__(self, marca, modelo):
    self.marca = marca
    self.modelo = modelo
#Los metodos son funciones que estan dentro de una clase
  def llamada(self): #es el metodo, va con self para referise al atributo del objeto
    print(f"estan llamando a tu {self.marca}")

celular1 = Celular("huawei", "k43")
celular2 = Celular("apple", "m10")

print(celular1.marca)
print(celular2.marca)

celular1.llamada()