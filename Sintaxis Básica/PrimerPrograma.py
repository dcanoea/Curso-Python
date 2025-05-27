mensaje="Hola Python"

print(mensaje)

#OPERADORES ARITMÉTICOS
print(5+6)#suma 11
print(6-2)#resta 4
print(11/2)#division 5,5
print(11//2)#division entera 5
print(2*3)#multiplicacion 6
print(10%3)#resto 1
print(5**3)#exponente 125

#En Python la variable se define por el contenedor
mi_nombre="David" #variable str
numero=5 #variable numérica int
decimal=2.5 #variable numérica float

#En Python absolutamente todo es un Objeto (variables incluidas)
print(type(mi_nombre))
print(type(numero))
print(type(decimal))

#las " definen los saltos de linea en un str
mensaje = """Esto es un mensaje
con tres saltos
de linea"""
print(mensaje)

##Condicional con operadores comparación
num1=5
num2=7
if num1>num2:
    print("El numero 1 es mayor")
else:
    print("El numero 2 es mayor")