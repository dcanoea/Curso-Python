#Crea un programa que pida dos números por teclado. El programa tendrá una función 
#llamada “DevuelveMax” encargada de devolver el número más alto de los dos 
#introducidos.

num1=(int(input("Introduce el primer número: ")))
num2=(int(input("Introduce el segundo número: ")))

def DevuelveMax(n1,n2):
    if n1<n2:
        print(n2)
    elif n2<n1:
        print(n1)
    else:
        print("Son iguales")

print("El número más alto es: ")
DevuelveMax(num1,num2)