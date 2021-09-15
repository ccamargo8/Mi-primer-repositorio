import datetime

p=int(input("Ingrese la cantidad de piso del parqueadero: "))
e=int(input("Ingrese la cantidad de parqueaderos por piso: "))

parking=[[0]*e for i in range (p)]

class vehiculo:
    
    def __init__(self,placa):
        self.placa = placa
        self.ingreso = datetime.datetime.now()
        
    def info(self):
        return f"El vehiculo con placas {self.placa}, fecha de ingreso {self.ingreso}"
        
while True:
    x=int(input("Ingrese una opción: "))
    if(x==1):
        for i in range(len(parking)):
            for j in range(len(parking[0])):
                           if(parking[i][j]==0):
                               print(f"Piso {i}, espacio {j} ==> está vacio")
                               
    elif(x==2):
        p=int(input("Ingrese el piso a parquear: "))
        e=int(input("Ingrese el espacio: "))
        if parking[p][e]==0:
            pl=input("Ingrese la placa del vehiculo: ")
            pl.upper()
            parking[p][e]=vehiculo(pl)
        else:
            print("Hay un vehiculo parqueado y el espacio no está disponible")
            
    elif(x==3):
        for i in range(len(parking)):
            for j in range(len(parking[0])):
                           if(parking[i][j]==0):
                               print(f"Piso {i}, espacio {j} ==> está vacio")
                           else:
                               print(f"Piso {i}, espacio {j} ==> {parking[i][j].info()}")
                        
        
    else:
        print("Saliendo del sistema...")
        break                       