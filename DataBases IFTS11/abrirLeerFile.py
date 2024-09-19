#%% Crear/Abrir file
try:
    file = open("FileCreado.txt", "w")
    file.write("Esto se creo desde python") #Si el file existe, se reemplaza el texto
    file.close() #Siempre cerrar el file, buena practica
except FileNotFoundError:
    print("El archivo no se encontro")

#%% Otra forma de Crear/Abrir file
try:
    with open("OtroArchivo.txt","w") as file2: #Con with el file se cierra solo
        file2.write("Otra forma de abrir/crear un file")
except FileNotFoundError:
    print("No se encontro el archivo")

#%% Leer un file
try:
    file = open("FileCreado.txt","r")
    contenido = file.read()
    file.close()
    print(contenido)
except FileNotFoundError:
    print("El archivo no se encontro")

#%% Otra forma de leer un file
try:
    with open("OtroArchivo.txt","r") as file2:
        contenido = file2.read()
        print(contenido)
except FileNotFoundError:
    print("No se encontro el archivo")

#%% JSON
import json

try:
    with open("data.json","r") as file:
        dic = json.load(file)
        print(type(dic))
        print(dic["nombre"])
        print(dic["edad"])
except FileNotFoundError:
    print("No se encontro el archivo")
