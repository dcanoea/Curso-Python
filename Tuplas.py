#Las tuplas son listas inmutables, es decir, no se pueden modificar después de su creación
#No permiten añadir, eliminar o mover elementos
#Permite extraer porciones, pero el resultado es una nueva tupla
#No permite búquedas (no index), aunque si permite comprobar si se encuentra un elemento en la tupla
#Más rapidas, menos espacio, formatean Strings, pueden usarse como claves en un diccionario

#SINTAXIS     nombreTupla=(elem0,elem1,elem2)

miTupla=("David",23,10,1985,"David")
print(miTupla)
print(miTupla[2])

#Método para convertir una tupla en una lista
miLista=list(miTupla)
print(miLista)

#Método para convertir una lista en una tupla
miTupla2=tuple(miLista)
print(miTupla2)

#Método para buscar si un elemento se encuentra dentro de la tupla (true/false)
print("David" in miTupla)
print(33333 in miTupla)

#Método para averiguar cuantas veces aparece un elemento dentro de una tupla
print(miTupla.count("David"))

#Método para contar los elementos de una tupla
print(len(miTupla))

#Tupla con un único elemento, hay que añadir una coma
miTuplaUnitaria=("David",)
print(miTuplaUnitaria)
print(len(miTuplaUnitaria))

#En una tupla los parentesis son opcionales (aunque no es recomendable). Se denomina "empaquetado de tupla"
miTupla3="David",11,3,1111
print(miTupla3)

#También existe el "desempaquetado de tupla"
miTupla4=("David",23,4,1899)
nombre, dia, mes, anyo=miTupla4
print(nombre)
print(dia)
print(mes)
print(anyo)

#Vemos como no se puede modificar ni agregar nada a una tupla
miTupla.append("Paco")