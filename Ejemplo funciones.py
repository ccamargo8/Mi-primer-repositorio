import misFunciones as mf

#Tambien se puede usar from misFunciones import * para importar todo y no poner mf. o misFunciones. antes de usarlas

a=int(input("Ingrese el valor de a: "))
b=int(input("Ingrese el valor de b: "))

if mf.esPrimo(a):
    print(a,"es primo")
else:
    print(a,"No es primo")
    
if mf.esPrimo(b):
    print(b,"es primo")
else:
    print(b,"No es primo")

mcd=mf.mcd(a,b)
print("El maximo común divisor de",a,"y",b,"es",mcd)

mcm=mf.mcm(a,b)
print("El minimo común multiplo de",a,"y",b,"es",mcm)

da=mf.comienzaCon(a)
print("el primer digito de",a,"es",da)

db=mf.comienzaCon(b)
print("el primer digito de",b,"es",db)         
