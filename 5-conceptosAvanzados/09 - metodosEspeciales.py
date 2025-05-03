# 🧠 ¿Qué son los métodos especiales?
# Son métodos con nombres raros, que empiezan y terminan con doble guion bajo (__).
# Python los usa para hacer cosas automáticamente.

# Se llaman también "métodos mágicos" o "dunder methods" (de double underscore).

class Pirata:
    def __init__(self, nombre):
        self.nombre = nombre  # este método se llama al crear el objeto

    def __str__(self):
        return f"Soy el pirata {self.nombre}"  # este se usa cuando hacés print()

    def __len__(self):
        return len(self.nombre)  # devuelve la cantidad de letras del nombre

# Crear un objeto
luffy = Pirata("Luffy")

# __str__ se activa con print()
print(luffy)  # 👉 Soy el pirata Luffy

# __len__ se activa con len()
print(len(luffy))  # 👉 5
