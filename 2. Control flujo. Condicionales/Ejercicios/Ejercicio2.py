#Crea un programa que pida por teclado “Nombre”, “Dirección” y “Tfno”. Esos tres datos 
#deberán  ser  almacenados  en  una  lista  y  mostrar  en  consola  el  mensaje:  “Los  datos 
#personales  son:  nombre  apellido  teléfono”  (Se  mostrarán  los  datos  introducidos  por 
#teclado).

nombre=input("Introduce tu nombre: ")
direccion=input("Introduce tu dirección: ")
telefono=input("Introduce tu telefono: ")

lista=[nombre,direccion,telefono]

print("---------------------------")
print("Los datos personales son: ")
print("Nombre: " + lista[0])
print("Dirección: " + lista[1])
print("Teléfono: " + lista[2])