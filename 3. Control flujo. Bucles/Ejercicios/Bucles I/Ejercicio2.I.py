#Crea  un  programa  que  pida  por  teclado  introducir  una  contraseña.  La  contraseña  no 
#podrá tener menos de 8 caracteres ni espacios en blanco. Si la contraseña es correcta, 
#el programa imprime “Contraseña OK”. En caso contrario imprime “Contraseña 
#errónea”

password=input("Introduce una contraseña, mínimo 8 carácteres sin espacios: ")

def comprobarPassword(password):
    comprobador=True

    if len(password)<8:
        return print("La contraseña debe contener 8 carácteres como mínimo")
    else:
        for i in password:
            if i== " ":
                comprobador=False
                break
    
    if comprobador==True:
        return print("La contraseña es correcta")
    else:
        return print("La contraseña no puede contener espacios")

comprobarPassword(password)