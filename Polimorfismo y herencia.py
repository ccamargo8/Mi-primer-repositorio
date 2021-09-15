# #Ejemplo de clase cuadrado

class cuadrado(): #==> Clase
    
    def __init__(self): #==> Constructor. Tamano es una variable de paso
        tamano=int(input("Ingrese el tamaño del cuadrado: "))
        self.ancho="* "*tamano #==> ancho, alto y area son atributos del objeto
        self.alto=tamano
        self.area = tamano**2
        
        
    def __str__(self): #Metodo especial para imprimir cuando se llame la clase
        return f"""
                    Este objeto tiene ancho: {self.alto}
                                        alto: {self.alto}
                                        area: {self.area}
    
    """
    
    def mostrar(self): #==> metodo
        print("\n")
        for i in range(self.alto):
            print("   "+self.ancho)
            


# class persona():
    
#     def __init__(self,nom,ape):
#         self.nombre=nom
#         self.apellido=ape
        
    
#     def __str__(self):
#         cadena=self.nombre+" "+self.apellido
#         return cadena

# persona1=persona("Carlos","Camargo")
# print(persona1)