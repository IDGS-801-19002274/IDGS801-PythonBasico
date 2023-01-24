class OperasBas:
    #Propiedades de clase
    num1 = 0
    num2 = 0
    resu = 0
    #Constructor
    def __init__(self, num1 : int, num2 : int):
        self.num1 = num1
        self.num2 = num2
    #Métodos de clase
    def suma(self):
        self.resu = self.num1 + self.num2
    
    def resta(self):
        self.resu = self.num1 - self.num2
    
    def multi(self):
        self.resu = self.num1 * self.num2
    
    def div(self):
        self.resu = self.num1 / self.num2

def main():
    obj = OperasBas(10, 5)
    obj.suma()
    print(obj.resu)

if __name__ == '__main__':
    main()