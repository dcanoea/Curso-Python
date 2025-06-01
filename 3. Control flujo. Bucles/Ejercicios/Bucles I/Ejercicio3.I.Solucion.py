#Crea un programa que  evalúe si una dirección de correo electrónico es válida o no en 
#función  de  si  tiene  “@”  o  “.”  Hay  que  tener  en  cuenta  que  la  dirección  se  considera 
#correcta si solo tiene una “@” y si tiene uno o más “.” 

email=input("Introduce email: ")

contadorArroba=0
contadorPunto=0

for i in range(len(email)):
    if email[i]=="@":
        contadorArroba=contadorArroba+1

    if email[i]==".":
        contadorPunto=contadorPunto+1

if contadorPunto==0 or contadorArroba!=1:
    print("email incorrecto")
else:
    print("email correcto")