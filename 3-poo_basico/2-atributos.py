# # clases
# class celulares(): # asi se invocan, contienen atributos
#   marca = "motorola"
#   modelo = "mp40"

# celular1 = celulares() # celular1 seria un objeto, es la instancia de una clase
# print(celular1.modelo)

# Si queres tener diferentes atributos para nuestros objetos debemos de hacerlo de esta forma

class Celular: # sin el ()
  def __init__(self, marca, modelo): # Init es metodo especial para clases, es el constructor
    self.marca = marca
    self.modelo = modelo

celular1 = Celular("huawei", "k43")
celular2 = Celular("apple", "m10")
print(celular1.marca)
print(celular2.marca)