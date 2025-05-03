# Clase Luffy, un personaje de One Piece
class Luffy:
    def __init__(self):
        # El poder de Luffy es privado, nadie puede cambiarlo directamente
        self.__poder = "Gomu Gomu no Pistol"

    # Método para ver el poder de Luffy (público)
    def ver_poder(self):
        return self.__poder

    # Método para cambiar el poder de Luffy (público)
    def cambiar_poder(self, nuevo_poder):
        self.__poder = nuevo_poder

# Crear un objeto Luffy
luffy = Luffy()

# Ver el poder de Luffy
print(luffy.ver_poder())  # 👉 Gomu Gomu no Pistol

# Cambiar el poder de Luffy
luffy.cambiar_poder("Gomu Gomu no Gatling")

# Ver el nuevo poder de Luffy
print(luffy.ver_poder())  # 👉 Gomu Gomu no Gatling
