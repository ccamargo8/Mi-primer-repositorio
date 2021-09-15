import random as rd
#Clase estrella. Si se crea una clase sin atributos, se usa pass
class estrella():
    lugar="Espacio"
    #Self quiere decir que el constructor le pertenece a la clase definida
    def __init__(self,
                 color="Blanca",
                 edad=0,
                 constelacion="nula"
                 ):
        self.color=color ##Se crea un atributo para el objeto
        self.edad=edad
        self.constelacion=constelacion
        
    def __str__(self):
        return f"""Clase Estrella:
                  Las estrellas que se crean con esta clase, tienen tres        atributos:
                      color={self.color}
                      edad={self.edad}
                      Constelacion={self.constelacion}
                """
                
                
    def edad_aleatoria(self):
       self.edad = rd.randint(1,10000)
       print(f"edad = {self.edad}")

#Crear objeto de la clase estrella: Instanciar
miestrella=estrella("Azul",10000)
miestrella2=estrella("Verde")
miestrella3=estrella("Amarillo")

miestrella4=estrella("Roja")
miestrella4.lugar="Otra dimension"

miestrella5=estrella()
miestrella6=estrella(color="azul",edad=1000,constelacion="Sagitario")
