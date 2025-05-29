#Crea un programa que pida dos números por teclado. El programa tendrá una función 
#llamada “DevuelveMax” encargada de devolver el número más alto de los dos 
#introducidos.
def DevuelveMax(num1,num2):
    numMayor=0
    if num1>numMayor:
        numMayor=num1
    if num2 >numMayor:
        numMayor=num2
    return numMayor    

print("Programa que pide dos números y devuelve el más alto")
num1=int(input("Introduce el primer nº: "))
num2=int(input("Introduce el segundo nº: "))

print("El nº mayor es " + str(DevuelveMax(num1,num2)))