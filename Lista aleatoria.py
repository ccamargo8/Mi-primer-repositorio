from misFunciones import lista_aleatoria

lista=lista_aleatoria(50,340)

if len(lista)%2==0:
    print(lista,"la lista es de tamaño par")
else:
    print(lista,"es de tamaño impar")
print(lista)