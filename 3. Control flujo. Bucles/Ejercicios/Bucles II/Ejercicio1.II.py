#Crea  un  programa  que  pida  números  infinitamente.  Los  números  introducidos  deben 
#ser cada vez mayores El programa finalizará cuando se introduce un número menor que 
#el anterior
print("Programa que evalúa si un número es mayor que el anterior")
num=int(input("Introduce un número "))
numMayor=0

while num>numMayor:
    print("El nº introducido es mayor")
    numMayor=num
    num=int(input("Introduce un número "))

print("El nº introducido es menor")