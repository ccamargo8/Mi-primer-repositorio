# count = 10
# count_2 = 0
# print("empezando...")

# while count>0:
#     count -=2
#     print(f"contador = {count}")
#     #Parte del ciclo
    
#     while count_2<3:
#         count_2+=1
#         print(f"Contador 2= {count_2}")
        
#         if count_2 ==2:
#             count_2=3
#             break
    
    
# print() #No hace parte del ciclo
# print("Hecho")

#Continue

# contras=""
# while contras!="holamundo":
#     contras=input("Ingrese la contraseña: ")
#     if contras=="HolaMundo":
#         print("Ya usaste esa contraseña")
#         continue
# print("Contraseña correcta... Bienvenido")
    
#Ejemplo costo de tiquete segun edad, origen y destino
nombre=input("Por favor ingrese su nombre: ")
origen = int(input(f"{nombre}, por favor seleccione su ciudad origen: "))
destino = int(input(f"{nombre}, por favor seleccione su ciudad destino: "))
edad=int(input(f"{nombre} por favor ingrese su edad: "))

if origen==5 or destino==5:
    costoTiquete=980000
else:
    if origen==1:
        if destino==2:
            costoTiquete=200000
            if edad<60:
                costoTiquete=210000
        elif destino==3:
            costoTiquete=250000-.1*edad*1000
        elif destino==4:
            costoTiquete = 300000+edad*1000
    elif origen==2:
        if destino==1:
            if edad>80:
                costoTiquete=0
            else:
                costoTiquete=200000
        elif destino==3:
            costoTiquete=200000
            if edad<60:
                diferencia=60-edad
                if diferencia>20:
                    sobrecosto=20000
                else:
                    sobrecosto=diferencia*1000
                costoTiquete=200000+sobrecosto
        elif destino==4:
            costoTiquete=400000
            if edad>60:
                costoTiquete=400000+.05*edad*10000
    elif origen==3:
        if destino==1:
            costoTiquete=350000
        elif destino==2:
            costoTiquete=280000
            if edad<60:
                costoTiquete=300000
        elif destino==4:
            costoTiquete=190000
            if edad<60:
                costoTiquete=200000
    elif origen==4:
        if destino==1:
            costoTiquete=500000
            if edad<10:
                costoTiquete=250000
        elif destino==2:
            costotiquete=210000
            if edad<30:
                costoTiquete=240000
        elif destino==3:
            costoTiquete=350000
            if edad>60:
                costoTiquete=350000+(edad-60)*10000
print(nombre," el costo del tiquete es ",costoTiquete)  