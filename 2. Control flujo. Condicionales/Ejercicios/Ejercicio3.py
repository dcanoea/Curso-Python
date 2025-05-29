#Crea un programa que pida tres números por teclado. El programa imprime en consola 
#la media aritmética de los números introducidos.  

num1=int(input("Introduce el primer nº: "))
num2=int(input("Introduce el segundo nº: "))
num3=int(input("Introduce el tercer nº: "))

media=(num1+num2+num3)/3
print("La media es " + str(media))