#ej1

def areaCuadrado(base, altura):
  area = base * altura
  return area

print(areaCuadrado(4, 5))

def areaCirculo(radio):
  pi = 3.14
  return pi * (radio) ** 2

print(areaCirculo(5))


#ej2

def medida(*tupla):
  return len(tupla)

print(medida(4, 3, 1, 2))