#Listas
datos = [3,4,"hola",True,2.8]
print(datos[2]) #Imprimir un dato especifico
datos[1]+=2 #Agregar un dato a una posicion
datos.append("Mundo") #Agregar datos
del datos[3] #Eliminar datos segun su posicion
datos.remove(2.8) #Eliminar dato por su nombre

print(datos)

#Tuplas
#No se pueden modificar sus datos. No existe Append o remove
datos_t = (2,3,4,5)
datos_t[2] #Acceder a un dato especifico por posicion

#Sets
#Representación en programación de conjuntos matematicos
#Los sets no tienen orden. por lo tanto no se les asignará indice por lo tanto no se puede usar como datos_s[0]
#No permiten datos repetidos. Si se agrega, se omite
datos_s = {5,3,4,2} 
datos_s.add(1) #Agregar un dato al set
datos_s.update([2,3]) #Agregar varios datos.
datos_s.remove(1) #Remover un dato

#Operaciones con estructuras
#Contencion: Saber si una estructura de datos contiene un dato especifico
3 in datos_s #Da como resultado un booleano
datos_s2 = {7,3,4,8}
#Union: tomar todos los datos de ambos sets y juntarlos en 1 solo
union=datos_s.union(datos_s2)
#Intercección: Datos que forman partes de ambos sets a la misma ves
inter=datos_s.intersection(datos_s2)
#Diferencia: Datos que hacen parte del primer conjunto pero no del segundo. Tiene importancia del orden
diff = datos_s.difference(datos_s2)
print(datos_s)
print(datos_s2)
print(union)
print(inter)
print(diff)

#Diccionarios: estructura desordenada pero se puede acceder a sus datos. Contienen pares de datos
datos_d={
    5:"Hola",
    8:"Mundo",
    'name': 'Andres',
    'age':18
}

#Acceder a un dato:
datos_d['name'] = 'Carlos'
#Agregar datos:
datos_d['college'] = 'Universidad Simón Bolivar'
#Eliminar datos:
del datos_d[5]

#No se puede acceder a los datos sin conocer la llave. pero se puede usar for i para recorrer los datos
for i in datos_d.values(): #Se usa para recorrer estructura de datos. i tomará el valor de la llave. Si se usa .values() recorrerá valores y no las llaves
    print(i)  #Tomará un dato en la estructura de datos. si es ordenada, la recorrerá en orden, de lo contrario, la recorre arbitrariamente
    
#Solución al problema
datos = [] #Se crea una lista

while(True): #Dentro de un while infinito, se reciben datos de interes
    nombre = input("Ingrese el nombre: ")
    numero = input("Ingrese el numero: ")
    dato = { 
        'nombre': nombre,
        'numero': numero
    } #Se guardan los datos de manera ordenada
    datos.append(dato) #Se agregan los datos a la lista
    opcion = input("¿Desea continuar? (s/n): ") #Se evalua si se desea continua
    if opcion == "n":
        break

for i in datos: #Se imprimen los datos
    print(i['nombre'])
    print(i['numero'])
    