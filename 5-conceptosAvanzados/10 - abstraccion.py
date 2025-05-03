# 🎭 Abstracción = mostrar solo lo importante y esconder los detalles

# Creamos una clase base con un método genérico
class Personaje:
    def atacar(self):
        # Esta es una idea general, no sabemos cómo ataca todavía
        print("El personaje ataca (no se sabe cómo)")

# Creamos una clase específica que hereda de Personaje
class Luffy(Personaje):
    def atacar(self):
        # Luffy ataca de una forma específica
        print("¡Luffy ataca con Gomu Gomu no Pistol!")

# Otra clase específica
class Zoro(Personaje):
    def atacar(self):
        # Zoro ataca de una forma distinta
        print("¡Zoro ataca con Santoryu: Oni Giri!")

# Ahora usamos las clases
luffy = Luffy()
zoro = Zoro()

# Cada personaje ataca, pero no necesitamos saber cómo lo hace por dentro
luffy.atacar()  # 👉 ¡Luffy ataca con Gomu Gomu no Pistol!
zoro.atacar()   # 👉 ¡Zoro ataca con Santoryu: Oni Giri!
