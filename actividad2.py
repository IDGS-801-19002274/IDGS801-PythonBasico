class Calculadora:
    
    def suma(self, num1, num2) -> str:
        return "la suma es: {}".format(num1 + num2)
    
    def resta(self, num1, num2) -> str:
        return "la resta es: {}".format(num1 - num2)
    
    def multi(self, num1, num2) -> str:
        return "la multiplicacion es: {}".format(num1 * num2)
    
    def div(self, num1, num2) -> str:
        return "la division es: {}".format(num1 / num2)

import os

def main():
    calc = Calculadora()
    opt = -1
    
    while opt != 0:
        print("---------- CALCULADORA ----------\nEscriba una opcion:\n1.-Suma\n2.-Resta\n3.-Multiplicacion\n4.-Division\n0.-Salir")
        opt = int(input('Accion: '))
        os.system('clear')
        match opt:
            case 1:
                num1 = int(input('Numero 1: '))
                num2 = int(input('Numero 2: '))
                print(calc.suma(num1, num2))
            case 2:
                num1 = int(input('Numero 1: '))
                num2 = int(input('Numero 2: '))
                print(calc.resta(num1, num2))
            case 3:
                num1 = int(input('Numero 1: '))
                num2 = int(input('Numero 2: '))
                print(calc.multi(num1, num2))
            case 4:
                num1 = int(input('Numero 1: '))
                num2 = int(input('Numero 2: '))
                print(calc.div(num1, num2))
            case 0:
                print("Nos vemos!")
                break
            case _:
                print("Entrada Invalido")

if __name__ == '__main__':
    main()