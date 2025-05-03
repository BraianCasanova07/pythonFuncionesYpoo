class Luffy:
    def __init__(self):
        # Atributo privado: Luffy empieza con carne
        self.__carne = "Costillar"

    # 🎯 GETTER: permite leer el valor como si fuera un atributo
    @property
    def carne(self):
        # Cuando accedés a luffy.carne, se ejecuta esto
        return self.__carne

    # 🛠️ SETTER: permite cambiar el valor con luffy.carne = ...
    @carne.setter
    def carne(self, nueva_carne):
        # Acá podrías validar o modificar antes de asignar
        self.__carne = nueva_carne

    # 🗑️ DELETER: permite borrar el valor con del luffy.carne
    @carne.deleter
    def carne(self):
        print("¡Luffy se quedó sin carne!")
        del self.__carne

luffy = Luffy()

# Leer el valor con el getter
print(luffy.carne)  # 👉 Costillar

# Cambiar el valor con el setter
luffy.carne = "Asado"
print(luffy.carne)  # 👉 Asado

# Borrar el valor con el deleter
del luffy.carne     # 👉 ¡Luffy se quedó sin carne!
