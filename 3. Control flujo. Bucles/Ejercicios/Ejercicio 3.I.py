#Crea un programa que  evalúe si una dirección de correo electrónico es válida o no en 
#función  de  si  tiene  “@”  o  “.”  Hay  que  tener  en  cuenta  que  la  dirección  se  considera 
#correcta si solo tiene una “@” y si tiene uno o más “.” 

def comprobarEmail(email):
    arroba=0
    punto=0

    for i in email:
        if i=="@":
            arroba+=1
        if i==".":
            punto+=1
    
    if arroba==1 and punto >=1:
        return print("Email correcto")
    else:
        return print("Email incorrecto")

email=input("Introduce un email: ")
comprobarEmail(email)
