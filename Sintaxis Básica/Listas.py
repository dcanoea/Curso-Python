#SINTAXIS nombreLista=[elem0, elem1, elem2]

miLista=["David","Jimena","Luciano","Teo"]

print(miLista[:])#Imprime la Lista completa

print(miLista[2])#Imprime el índice definido 

print(miLista[-1])#Si el valor es negativo empieza a recoger el índice desde el final

print(miLista[0:3])#Recoge una porción de la lista, 0 primer indice y 3 el último
print(miLista[:2])#Si no indicamos el primer indice empieza desde el primero
print(miLista[2:])#En este caso recoge los índices desde la posición 2 hasta el final

miLista.append("Leticia") #Agrega un elemento al final de la lista
print(miLista[:])

miLista.insert(4,"Miguel") #Inserta un elemento en la posicion 4
print(miLista[:])

miLista.extend(["Sinara","Ailana"]) #Agrega varios elementos a la lista
print(miLista[:])

print(miLista.index("Teo"))#Devuelve el índice donde se encuentra "Teo"

print("pepe" in miLista) #Imprime true o false si se encuentra en la lista

#Python puede almacenar diferentes tipos en una misma lista
miLista2=["David", 1, True, 33.44]
print(miLista2[:])

miLista2.remove("David")#Elimina el elemento de la lista
print(miLista2[:])

miLista2.pop()#Elimina el ultimo elemento de la lista
print(miLista2[:])

miLista3=["Sandra", "Lucía"]

miLista4=miLista+miLista3 #Podemos concatenar listas con el símbolo +
print(miLista4[:])

miLista5=[1,2,3,4,5] * 3 #El operador * repite la lista el número de veces indicado
print(miLista5[:])