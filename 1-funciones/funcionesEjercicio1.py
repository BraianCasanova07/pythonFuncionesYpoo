lista = []
num = 0

def numerosPedir():
  i = 0
  while i <= 5:
    num = int(input("Dame un numero: "))
    lista.append(num)
    i += 1
  print(lista)

numerosPedir()

def ordenar():
  lista.sort()
  par = []
  inpar = []
  for i in lista:
    if i % 2 == 0:
      par.append(i)
    else:
      inpar.append(i)
  print(par)
  print(inpar)

ordenar()