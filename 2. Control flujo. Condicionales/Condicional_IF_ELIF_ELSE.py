print("Verificacion de aprobado")

notaAlumno=int(input("Introduce tu nota: "))

if notaAlumno<5:
    print("Insuficiente")
elif notaAlumno<6:
    print("Suficiente")
elif notaAlumno<7:
    print("Bien")
elif notaAlumno<9:
    print("Notable")
else:
    print("Sobresaliente")

print("El programa ha finalizado")