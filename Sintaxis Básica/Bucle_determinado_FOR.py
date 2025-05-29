print("1")
for i in [1,2,3]:
    print("Hola", end=" ") #con el parámetro end="" le decimos que no haga un salto de línea y ponga un espacio en su lugar
print()
print()


print("2")
for i in ["primavera","verano","otoño","invierno"]:
    print(i)
print()


print("3")
for i in "ddddd@mail.com":
    print("hola", end=" ") #imprime "hola" tantas veces como carácteres hay en la instrucción in
print()
print()


print("4")
contador=0
miEmail=input("Introduce tu dirección de email:")
for i in miEmail:
    if(i=="@" or i =="."):#comprueba caracter a caracter si contiene una @ o contiene . para verificar si es un email 
        contador=contador+1

if contador>=2:
    print("El email es correcto")
else:
    print("El email no es correcto")
print()

print("5")
for i in range(5): #función range (hace el bucle for más parecido a otros lenguajes de programación)
    print(i)