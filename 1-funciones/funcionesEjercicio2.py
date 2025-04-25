def factorial():
  num = int(input("dame un numero: "))
  if num > 0:
    factor = 1
    for i in range(1, num + 1):
      factor = factor * i
    print(factor)


factorial()