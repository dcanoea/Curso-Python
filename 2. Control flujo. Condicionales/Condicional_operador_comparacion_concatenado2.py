salarioPresidente = int(input("Introduce salario del Presidente "))
print("Salario Presidente: " + str(salarioPresidente))

salarioDirector = int(input("Introduce salario del Director "))
print("Salario Director: " + str(salarioDirector))

salarioJefeArea = int(input("Introduce salario del Jefe de Area "))
print("Salario Jefe de Area: " + str(salarioJefeArea))

salarioAdministrativo = int(input("Introduce salario del Administrativo "))
print("Salario Administrativo: " + str(salarioAdministrativo))

if salarioAdministrativo<salarioJefeArea<salarioDirector<salarioPresidente:
    print("Todo funciona correctamente")
else:
    print("Algo falla en esta empresa")