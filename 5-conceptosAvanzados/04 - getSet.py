#En Python, un getter y un setter son solo dos métodos para leer y escribir un atributo “privado”.

class Luffy:
    def __init__(self, oro):
        self.__oro = oro

    def get_oro(self):
        return self.__oro

    def set_oro(self, cantidad):
        self.__oro = cantidad

# Uso:
luffy = Luffy(100)
print(luffy.get_oro())   # 100
luffy.set_oro(250)
print(luffy.get_oro())   # 250
