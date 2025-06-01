#Crea un programa que pida  números positivos indefinidamente.  El programa  termina 
#cuando se introduce un número negativo. Finalmente el programa muestras la suma de 
#todos los números introducidos

print("Programa que pide números positivos. El programa termina al introducir un negativo y muestra la suma de todos los números")

num=int(input("Introduce un número "))
acumulador=0
contador=0

while num>=0:
    acumulador=acumulador+num
    contador+=1
    num=int(input("Introduce un número "))

if acumulador>0 and contador>0:
    media=acumulador/contador
    print("Has introducido " + str(contador) + " números. En total suman " + str(acumulador))
    print("La media de los números introducidos es " + str(media))