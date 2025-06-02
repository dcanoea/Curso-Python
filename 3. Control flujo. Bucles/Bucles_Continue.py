for letra in "Python":
    if letra == "h": 
        continue #Si el carácter es h, lo ignora y continua el bucle
    print("Viendo la letra " + letra)

print("---------------------------------------------------------------")

nombre="Pildoras Informaticas"
print(len(nombre)) #La longitud nos dice que contiene 21 carácteres(incluye el espacio)

#Ahora vamos a contar unicaménte las letras
contador=0
for i in nombre:
    if i==" ":
        continue #Con esto conseguimos que no cuente el espacio
    contador+=1

print(contador)