#%% Excepcion generica
a = 8
b = 2

try:
    c = a / b
    print(c)
except:
    print("No se puede dividir por: ", b)

#%% Tipos de excepciones
try:
    numero = int(input("Ingrese un numero: "))
    resultado = 10 / numero

except ZeroDivisionError:
    print("Error: No se puede dividir por cero")
except ValueError:
    print("Error: Solo se permite numero enteros")
else:
    print(f"El resultado es: {resultado}")
finally:
    print("Fin del programa")

#%% Capturar Excepciones en una variable
b = 8
c = "pepa"

try:
    a = b // c
    print(a)
except Exception as e:
    print("Error: ", e)

print("Esto se sigue ejecutando")
