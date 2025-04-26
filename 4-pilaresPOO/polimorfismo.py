class trabajador():
  def describir(self):
    print("trabajo en una gran empresa")

class estudiante():
  def describir(self):
    print("soy un gran estudiante")

def describirPersona(persona):
  persona.describir()

doc1 = estudiante()
describirPersona(doc1)