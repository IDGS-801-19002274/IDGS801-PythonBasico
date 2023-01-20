#Programa que le pida al usuario via teclado un numero e imprima la tabla de multiplicar de ese numero
num = int(input('Inserte el numero a multiplicar: '))
for n in range(1, 11):
    print("{} x {} = ".format(num, n), (num * n))