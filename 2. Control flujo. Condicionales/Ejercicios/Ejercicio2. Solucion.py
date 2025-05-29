#Crea un programa que pida por teclado “Nombre”, “Dirección” y “Tfno”. Esos tres datos 
#deberán  ser  almacenados  en  una  lista  y  mostrar  en  consola  el  mensaje:  “Los  datos 
#personales  son:  nombre  apellido  teléfono”  (Se  mostrarán  los  datos  introducidos  por 
#teclado).
Nombre=input("Introduce el nombre: ")
Direccion=input("Introduce la dirección: ")
Tfno=input("Introduce el teléfono: ")

listaDatos=[Nombre,Direccion,Tfno]

print("Los datos personales son: " + listaDatos[0] + " " +
      listaDatos[1] + " " + listaDatos[2])