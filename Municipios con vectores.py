n = 125

acmpio = [0] * (n + 1)

mpio = int(input("Entre código de municipio "))

while mpio != 0:

            np = int(input("Entre número de personas "))

            acmpio[mpio] = acmpio[mpio] + np

            mpio = int(input("Entre código de municipio "))

for i in range(1, n + 1):

            print("Municipio", i, "Habitantes = ", acmpio[i])
            
        
#Ejemplo 2. Vector con nombres asignados

n = 10

nomMpio = ["","Medellin","Bello","Envigado","Sabaneta","Itagui","Rionegro","La Ceja","Entrerrios","Andes","Abejorral"] 
 
acmpio = [0] * (n + 1)   


mpio = int(input("Entre código de municipio "))

while mpio != 0:

            np = int(input("Entre número de personas "))

            acmpio[mpio] = acmpio[mpio] + np

            mpio = int(input("Entre código de municipio "))

for i in range(1, n + 1):

            print("Municipio", nomMpio[i], "Habitantes = ", acmpio[i])   