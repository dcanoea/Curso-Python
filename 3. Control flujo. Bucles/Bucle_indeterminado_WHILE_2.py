edad=int(input("Introduce la edad "))

while edad<5 or edad>100:
    print("Has introducido una edad negativa, vuelve a intentarlo")
    edad=int(input("Introduce la edad "))

print("Edad del aspirante " + str(edad))
print("Gracias por colaborar. Puedes pasar")