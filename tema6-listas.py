nombres = ["Juan", "Mario", "Laura"]
numeros = [1, 2, 3, 4, 5]
datos = [1, 2.5, "Mario", True]
print(nombres)

nombres[0] = "Roberto"

#Todo esto viene en tema 5 xd
print(nombres[:])
print(nombres[2])
print(nombres[:3])
print(nombres[1:])

nombres.append("Dario") #Inserta nuevo elemento en la lista
print(nombres)
nombres.insert(2, "Maria") #Inserta un nuevo elemento en el index 2 de la lista, si ya existe, lo reemplaza
print(nombres)

nombres.extend(["Chencha", "Teofila"]) #Agrega otra lista
print(nombres)

nombres.remove("Chencha") #Mata a chencha
print(nombres)

nombres.pop() #Elimina el ultimo elemento
print(nombres)

n = ["Juan"]
n2 = n*5 #Multiplica los elementos de la lista
print(n2)

del nombres[0]
print(nombres)
