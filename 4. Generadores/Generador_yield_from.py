def devuelve_ciudades(*ciudades): #con el * indicamos un nº indeterminado de elementos y además los va a recibir en forma de tupla
    for elemento in ciudades:
        #for subelemento in elemento:
            yield from elemento #yield from sustituye al bucle for anidado, simplifica el código


ciudades_devueltas=devuelve_ciudades("Madrid", "Barcelona", "Bilbao", "Valencia", "Zaragoza")

print(next(ciudades_devueltas))
print(next(ciudades_devueltas))
print(next(ciudades_devueltas))
print(next(ciudades_devueltas))