#Funcionamiento con una función tradicional
def generaPares(limite):
    num=1
    miLista=[]

    while num<limite:
        miLista.append(num*2)
        num+=1
    return miLista

print(generaPares(10))

#Funcionamiento con un generador
def generadorPares(limite):
    num=1
    while num<limite:
        yield num*2
        num+=1

devuelvePares=generadorPares(10) #Guardamos en un objeto el objeto iterable que devuelve la función

print(next(devuelvePares)) #mediante el método next va a devolver de uno en uno cada numero guardado
print("Aquí podría ir mas código...")
print(next(devuelvePares)) #mediante el método next va a devolver de uno en uno cada numero guardado
print("Aquí podría ir mas código...")
print(next(devuelvePares)) #mediante el método next va a devolver de uno en uno cada numero guardado