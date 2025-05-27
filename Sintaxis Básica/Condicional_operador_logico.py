print("Programa de becas año 2025")

distanciaEscuela=int(input("Introduce la distancia a la escuela en km "))
print(distanciaEscuela)

numeroHermanos=int(input("Introduce el nº de hermanos en el centro "))
print(numeroHermanos)

salarioFamiliar=int(input("Introduce salario anual bruto "))
print(salarioFamiliar)

if distanciaEscuela>40 and numeroHermanos>2 or salarioFamiliar<=20000:
    print("Tienes derecho a beca")
else:
    print("No tienes derecho a beca")