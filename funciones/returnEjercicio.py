def mayormenor():
  num1 = int(input("dame un numero: "))
  num2 = int(input("dame un numero: "))
  if num1 > num2:
    return 1
  elif num2 > num1:
    return -1
  else:
    return 0

print(mayormenor())