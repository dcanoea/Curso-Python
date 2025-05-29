def mensaje():#declaracion de la función

    print("Estamos aprendiendo Python")
    print("Poco a poco")                    ##CUERPO DE LA FUNCIÓN
    print("Seguiremos aprendiendo")
    print()

mensaje()#llamada a la función
mensaje()

print("Ejecutando código fuera de función")
mensaje()


def suma(num1, num2): #Función con parámetros
    print(num1+num2)

suma(1,2)#pasamos los parámetros
suma(111,222)


def sumaReturn(num1,num2): #Función que devuelve un resultado (return)
    resultado=num1+num2
    return resultado

print(sumaReturn(123,1))

almacena_resultado = sumaReturn(5,8) #Almacenamos en una variable el return de la funcion sumaReturn
print(almacena_resultado)