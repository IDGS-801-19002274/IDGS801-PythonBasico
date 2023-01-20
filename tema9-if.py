print("Valores de Usuario")

num1 = int(input('Dame Valor 1: '))
num2 = int(input('Dame Valor 2: '))

if num1 > num2:
    print ("{} es mayor que {}".format(num1, num2))
else:
    print ("{1} es mayor que {0}".format(num1, num2))