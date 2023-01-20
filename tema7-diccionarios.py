miDiccionario = {
    "Matricula" : "19002274",
    "Nombre" : "Dario",
    "Edad" : 23
}

print(type(miDiccionario))
print(miDiccionario)
print(miDiccionario["Edad"])

miDiccionario["Nombre"] = "Panfilo"
print(miDiccionario)
print(miDiccionario.values()) #Imprime nomas los valores
print(miDiccionario.keys()) #Imprime nomas las llaves