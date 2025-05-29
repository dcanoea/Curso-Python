for i in range(5): #del 0 al 4
    print(f"Valor de la variable: {i}")
print()

for i in range(5,10): #del 5 al 9
    print(f"Valor de la variable: {i}")
print()

for i in range(5,50,3): #del 5 al 49, de 3 en 3
    print(f"Valor de la variable: {i}")



valido=False
email=input("Introduce tu email ")
for i in range(len(email)): #el rango es la longitud del str de email
    if email[i]=="@": #evalua cada caracter del rango
        valido=True

if valido:
    print("Email correcto")
else:
    print("Email incorrecto")