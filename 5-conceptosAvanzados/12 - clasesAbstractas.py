# Importamos lo necesario para usar clases abstractas
from abc import ABC, abstractmethod

# 👇 Esta es una clase abstracta. Sirve como molde general.
# No se puede usar sola. Solo sirve para que otros la hereden.
class Personaje(ABC):

    # 👇 Este método es abstracto.
    # Significa que todas las clases hijas DEBEN tener este método.
    @abstractmethod
    def atacar(self):
        pass  # No hace nada acá. Se define en las clases hijas.

# 👇 Esta es una clase que hereda de Personaje
# Como Personaje tiene un método abstracto, Luffy DEBE crear su propia versión
class Luffy(Personaje):
    def atacar(self):
        # 👇 Luffy ataca de su manera
        print("¡Luffy ataca con Gomu Gomu no Pistol!")

# 👇 Otra clase que también hereda y define atacar a su manera
class Zoro(Personaje):
    def atacar(self):
        print("¡Zoro ataca con Santoryu: Oni Giri!")

# ❌ Si intentás crear un objeto de Personaje directamente, da error:
# personaje = Personaje()  ← Esto NO se puede, porque es abstracta

# ✅ Pero sí podés crear objetos de Luffy y Zoro, porque completaron el método atacar()
luffy = Luffy()
zoro = Zoro()

# 👇 Usamos el método atacar. Cada uno ataca diferente.
luffy.atacar()  # 👉 ¡Luffy ataca con Gomu Gomu no Pistol!
zoro.atacar()   # 👉 ¡Zoro ataca con Santoryu: Oni Giri!
