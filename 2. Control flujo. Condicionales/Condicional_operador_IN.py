print("Asignaturas optativas año 2025")
print("Informática gráfica - Pruebas de software - Usabilidad y accesibilidad")
opcion=input("Escribe la asignatura escogida: ")

asignatura=opcion.lower()

if asignatura in ("informática gráfica", "pruebas de software", "usabilidad y accesibilidad"):
    print("Asignatura elegida " + asignatura)
else:
    print("La asignatura elegida no está contemplada")