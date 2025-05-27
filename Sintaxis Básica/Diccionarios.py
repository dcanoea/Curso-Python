#La principal característica de los diccionarios es que los datos se almacenan asociados tipo clave:valor
#Los elementos almacenados no están ordenados

#Creación de un diccionario mediante clave:valor entre {}
miDiccionario={"Alemania":"Berlin", "Francia":"Paris", "Reino Unido":"Londres", "España":"Madrid"}
print(miDiccionario)

#Busqueda de un valor mediante su clave
print(miDiccionario["Francia"])

#Agregar elementos a un diccionario
miDiccionario["Italia"]="Lisboa"
print(miDiccionario)

#Modificar un valor de una clave, sobreescribiendolo
miDiccionario["Italia"]="Roma"
print(miDiccionario)

#Eliminar un elemento
del miDiccionario["Reino Unido"]
print(miDiccionario)

#Imprimir las claves
print(miDiccionario.keys())

#Imprimir los valores
print(miDiccionario.values())

#Longitud del diccionario
print(len(miDiccionario))

#Diccionario con distintos tipos de elementos
miDiccionario2={"Portugal":"Lisboa", 23:"Jordan", "Mosqueteros":3}
print(miDiccionario)

#En un diccionario podemos incluir elementos de una tupla como campos clave
miTupla=["España","Francia","Reino Unido","Alemania"]
#Ahora le damos el valor a cada clave
miDiccionario={miTupla[0]:"Madrid", miTupla[1]:"Paris",miTupla[2]:"Londres",miTupla[3]:"Berlin"}
print(miDiccionario)

#Un diccionario puede almacenar una tupla entera
miDiccionario={23:"Jordan","Nombre":"Michael","Equipo":"Chicago","anillos":[1991,1992,1993,1996,1997,1998]}
print(miDiccionario)
#Acceder a la tupla
print(miDiccionario["anillos"])

#Un diccionario también puede almacenar diccionarios
miDiccionario={23:"Jordan","Nombre":"Michael","Equipo":"Chicago","anillos":{"temporadas":[1991,1992,1993,1996,1997,1998]}}
print(miDiccionario)
print(miDiccionario["anillos"])