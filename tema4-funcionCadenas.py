cadena = "Universidad Tecnologica de Leon"

print(cadena)
print(cadena.lower()) #minusculas
print(cadena.upper()) #mayusculas
print(cadena.title()) #primer letra de cada palabra en mayuscula
print(cadena.find("de")) #encuentra "de" en la cadena, si no encuentra da -1
print(cadena.count("a")) #cuenta las "a" de la cadena

textoFinal = cadena.replace("a", "4") #reemplaza a por 4
print(textoFinal)

cadenaNueva = cadena.split(" ") #crea un array con cada cadena usando como separador " "
print(cadenaNueva)