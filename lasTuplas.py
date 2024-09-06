arcoiris = ("Azul", "Verde", "Rojo", "Amarillo")
print(arcoiris)

print("--Longitud arcoiris--")
print(len(arcoiris))

animales = ("pantera", 20, "estatura", 1.7)
print(animales)
print("elementos de la tupla")
print(animales[1])




rateros= ("Juan", "Ana", "Pedro")
y = list(rateros)
y[1] = "Polainas"
x = tuple(y)

print(x)


print("Agregando elementos")
Nanimal = ("boby", "Chetos")
y=list(Nanimal)
y.append("Tontolín")
otraTupla = tuple(y)
print(otraTupla)


print("Uso de For en tuplas")
for color in arcoiris:
    print(color)

