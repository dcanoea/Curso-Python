email=input("Introduce tu email ")

for i in email:
    if i=="@":
        arroba=True
        break #Cuando encuentre una @ saldrá del bucle
else: #Este else forma parte del bucle for
    arroba=False       

print(arroba)