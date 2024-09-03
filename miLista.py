# Ejemplo de uso de listas
misNovias = ["Agripina", "Anastasia", "Maria"]
misNumeros = [666, 77, 10]

#Mostrando mis novias
print(misNovias)

#Mostrando mis números raros
print(misNumeros)

print("---Accediendo a los elementos de la lista---")
print(misNovias[-2])


if "Ana" in misNovias:
    print("sí, 'Ana' está en la lista de mis novias")

else:
    print("Chale, no eres mi novia ")

print("Número de novias")
posicion = 0
Nnovias = len(misNovias)
print(f"Número de novias: {Nnovias}")

print("Ciclo for en listas")
for mediaNaranja in misNovias:
    print(posicion, " ",mediaNaranja)
    posicion+=1

