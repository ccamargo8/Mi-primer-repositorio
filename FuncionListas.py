
"""
Crear una funcion que reciba una lista y la imprima elemento por elemento
"""


def imprimir_lista(accesorios):
    for i in accesorios:
        print(i)

def imprimir_inv_lista(accesorios):
    accesorios=accesorios[::-1]
    for i in accesorios:
        print(i)
        
def organizar(numeros):
    numeros.sort()
    return numeros    

def eliminar(lista,elemento):
    lista.pop(elemento)
    
def buscar(lista,elemento):
    if elemento in lista:
        posicion=lista.index(elemento)
        return posicion
    else:
        print("El elemento no está en la lista")
        return 
    
def elim_pos(lista,posi,posf):
    lista[posi:posf+1]=[]
    
    pass

def insertar(elemento,pos):
    lista[pos:pos]=[elemento]
    return lista

def organizar_inv(numeros):
    numeros.sort(reverse=True)
    pass 

def insertar_lista(lista1,lista2,pos):
    lista1[pos:pos]=lista2
    return lista1

def buscar_cant(lista,elemento):
    contador=0
    for objeto in lista:
        if objeto==elemento:
            contador+=1
    if contador==0:
        print("El elemento",elemento,"no se encuentra en la lista")
        return
    else:
        print("El numero de elementos",elemento,"es",contador)
        return contador
        