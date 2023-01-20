tupla = (1, 2, 3)

print(tupla)
print(type(tupla))

tupla2 = (7, "Roberto", True, 23.8, 16+7j)
print(tupla2)

print(tupla2[1]) #Imprime el elemento 2 de la tupla
print(tupla2[-1]) #imprime el ultimo elemento de la tupla
print(tupla2[0:3]) #imprime del elemento 1 al 3 de la tupla
print(tupla2[:3]) #lo mismo de arriba, el programa interpreta que el faltante es 0
print(tupla2[2:]) #Imprime toda la tupla, el programa interpreta que el faltante es el limite

a, b, c = tupla
print(a)
print(b)
print(c)

tuplaN = tupla + tupla2 #Suma ambas tuplas
print(tuplaN)
print(tuplaN.count(2)) #El numero de apariciones del 2 en la tuplaN