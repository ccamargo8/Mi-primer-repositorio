#Asignacion: llevar un dato a una posicion especifica del vector y se representa como vect[i]=dato, donde i es la posición del vector a la cual se le quiere asignar dicho dato y dato el dato que se quiere asignar a dicha posicion


#Acceso: obtener el dato almacenado en una posicion cualquiera: d1=var[k], donde se accede al dato de la posición k y se guarda en la variable d1

#Suma y mayor dato

def sumaVector(V,n):
    s=0
    for i in range(1,n):
        s = s+V[i]
    return s

def mayorDato(V,n):
    mayor=0
    for i in range(n):
        if V[i]>V[mayor]:
            mayor=i
    return mayor

n = 8

nomMpio = ["","Medellin","Bello","Envigado","Sabaneta","Itagui","Rionegro","La Ceja"] 
 
acmpio = [0]*n

mpio = int(input("Entre código de municipio "))

while mpio != 0:

            np = int(input("Entre número de personas "))

            acmpio[mpio] = acmpio[mpio] + np

            mpio = int(input("Entre código de municipio "))

for i in range(1, n):

            print(i, nomMpio[i],acmpio[i]) 
th=sumaVector(acmpio,n)
print("Total habitantes: ",th)
i=mayorDato(acmpio,n)
print("El mayor numero de habitantes está en el municipio: ",nomMpio[i],"con",acmpio[i],"habitantes")