texto1 = "Hola"
texto2 = "mundo!!"

textofinal = texto1+" "+texto2
print(textofinal)

print("El saludo es: %s %s" %(texto1, texto2))

cadena = "saludar dos: {} {}".format(texto1, texto2)
print(cadena)

cadena2 = "saludar tres: {1} {0}".format(texto1, texto2)
print(cadena2)

cadena3 = "Saludar quatro: {x} {y}".format(x=texto1, y=texto2)
print(cadena3)