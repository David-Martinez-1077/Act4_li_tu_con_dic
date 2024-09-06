informacionPersonal = {
    "nombre": "Luis",
    "Apellido": "Lopez", 
    "Edad": 32,
    "telefono": "456 5434 321", 
    "email": "frgmail.com"
    
}
print(informacionPersonal)
print("")
for key, value in informacionPersonal.items():
    print(f"{key}: {value}")