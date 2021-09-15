# salact = float(input("Ingrese el salario del trabajador: "))
# au=0

# if salact < 1000:
#     au = salact*0.1
# nuesal = salact+au
# print(f"Salario actual = {salact}", f"aumento = {au}", f"Nuevo salario = {nuesal}", sep=("; ") )    

#Usando componente else
# salact = float(input("Ingrese el salario del trabajador: "))
# au=0

# if salact < 1000:
#     au = salact*0.1
# else:
#     au = 0
# nuesal = salact+au
# print(f"Salario actual = {salact}", f"aumento = {au}", f"Nuevo salario = {nuesal}", sep=("; ") )    

#Leer dos enteros e imprimirlos en orden ascendente
# a = int(input("Ingrese el primer numero entero: "))
# b = int(input("Ingrese el segundo numero entero: "))

# if a>b:
#     print(a,b)
    
# else:
#     print(b,a)

#Sumar todos los numeros desde 1 hasta n
# n=float(input("Ingrese un numero: "))
# suma=0
# i=1

# while i<=n:
#     suma=suma+i
#     i=i+1
# print(suma)
    
# a = int(input("Ingrese el primer numero entero: "))
# b = int(input("Ingrese el segundo numero entero: "))

# if a%b ==0:
#     print(a, "es divisible por ", b)
# else:
#     print(a, "NO es divisible por ", b)
# print("Fin")

#Determina si un numero es la suma de otros dos
# a = int(input("Ingrese el primer numero entero: "))
# b = int(input("Ingrese el segundo numero entero: "))
# c = int(input("Ingrese el tercer numero entero: "))

# if a+b == c:
#     print(c, "es la suma de ",a,"con ",b)
# else:
#     if a+c == b:
#         print(b, "es la suma de ",a,"con ",c)
#     else:
#         if b+c == a:
#             print(a, "es la suma de ",b,"con ",c)
#         else:
#             print(a,",",b,"y",c,"no cumplen con la condicion")
# print("Fin")

#Determina si 3 valores pueden formar un triangulo forma 1
# a = int(input("Ingrese el primer numero entero: "))
# b = int(input("Ingrese el segundo numero entero: "))
# c = int(input("Ingrese el tercer numero entero: "))

# if a+b>c:
#     if a+c>b:
#         if b+c>a:
#             print(f"{a},{b} y {c} pueden formar un triangulo")
#         else:
#             print(f"{a},{b} y {c} NO pueden formar un triangulo")
# print("Fin triangulo con tres if")

# #Determina si 3 valores pueden formar un triangulo forma 2
# a = int(input("Ingrese el primer numero entero: "))
# b = int(input("Ingrese el segundo numero entero: "))
# c = int(input("Ingrese el tercer numero entero: "))

# if a+b>c and a+c>b and b+c>a:
#     print(f"{a},{b} y {c} pueden formar un triangulo")
# else:
#     print(f"{a},{b} y {c} NO pueden formar un triangulo")
# print("Fin triangulo con un if")

# b = input("entre un número ")
# c = input("entre otro número ")
# a = int(input("entre un tercer número "))
# d = int(input("entre un cuarto número "))

# print(b+c, end="")
# print(a+d)

# nombre = input("Ingrese su nombre: ")
# genero=int(input(f"{nombre}, Seleccione: 0:Femenino; 1:Masculino: "))
# estatura=int(input(f"{nombre}, ingresa tu estatura: "))
# peso=int(input(f"{nombre}, ingresa tu peso: "))

# if estatura >180:
#     if peso >70:
#         if genero == 0:
#             print("Reina de belleza")
#         else:
#             print("Cantautor")
#     else:
#         print("Arbitro de Futbol")
# else:
#     print("Jugador de parqués")
# print("Paciente clasificado")

#Programa para ordenar numeros de menor a mayor
a = int(input("Ingrese un numero entero: "))
b = int(input("Ingrese otro numero entero: "))
c = int(input("Ingrese un tercer entero: "))

aa=a
bb=b
cc=c 
        
print("Version 1, la comparación es compuesta solo con menor (<), y sin else",end=": \n")

if a<b and b<c:
    print("a", a,"b", b,"c", c)
if a<c and c<b:
    print("a", a,"c", c,"b", b)
if b<a and a<c:
    print("b", b,"a", a,"c", c)
if b<c and c<a:
    print("b", b, "c", c,"a", a)
if c<a and a<b:
    print("c", c,"a", a,"b", b)
if c<b and b<a:
    print("c", c, "b", b, "a", a)
print("")

a = aa
b = bb
c = cc

print("Version 2, la comparación es compuesta solo con menor o igual (<=), y sin else",end=": \n")

if a<=b and b<=c:
    print("a", a,"b", b,"c", c)
if a<=c and c<=b:
    print("a", a,"c", c,"b", b)
if b<=a and a<=c:
    print("b", b,"a", a,"c", c)
if b<=c and c<=a:
    print("b", b, "c", c,"a", a)
if c<=a and a<=b:
    print("c", c,"a", a,"b", b)
if c<=b and b<=a:
    print("c", c, "b", b, "a", a)
print("")

a = aa
b = bb
c = cc

print("Version 3, la comparación es compuesta solo con menor o igual (<=) usando else",end=": \n")

if a<=b and b<=c:
    print("a", a,"b", b,"c", c)
else:
    if a<=c and c<=b:
        print("a", a,"c", c,"b", b)
    else:
        if b<=a and a<=c:
            print("b", b,"a", a,"c", c)
        else:
            if b<=c and c<=a:
                print("b", b, "c", c,"a", a)
            else:
                if c<=a and a<=b:
                    print("c", c,"a", a,"b", b)
                else:
                    if c<=b and b<=a:
                        print("c", c, "b", b, "a", a)
print("")

a = aa
b = bb
c = cc

print("Version 4, con if anidados",end=": \n")
if a<b:
    if b<c:
        print("a", a,"b", b, "c", c)
    else:
        if a<c:
            print("a", a, "c", c, "b", b)
        else:
            print("c", c, "a", a, "b", b)
else:
    if a<c:
        print("b", b, "a", a, "c", c)
    else: 
        if b<c:
            print("b", b, "c", c, "a", a)
        else:
            print("c", c, "b", b, "a", a)
            
            
    