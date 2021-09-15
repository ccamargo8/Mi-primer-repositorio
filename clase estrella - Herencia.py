class estrella():
    """
    Esta es la clase estrella, con ella se pueden crear objetos tipo estrella en los         cuales guardar un catalogo de estrellas.
    
    Para iniciar una estrella:
        miestrella=estrella(tamaño,nombre,puntas,borde,fondo)
        
    ejemplo:
        miestrella=(5,"Betelguese",5,"Roja","Roja")
        
    """
    
    tipo="Estandar"
    
    def __init__(self,
                 tamano_in,
                 nombre_in,
                 num_puntas_in,
                 color_borde_in,
                 color_fondo_in):
        
        self.tamano = tamano_in
        self.nombre = nombre_in
        self.num_puntas = num_puntas_in
        self.color_borde = color_borde_in
        self.color_fondo = color_fondo_in
        
    def color_b(self,color_nuevo):
        self.color_fondo=color_nuevo
        
    def mostrar(self):
        print(f"Soy la estrella {self.nombre} de color {self.color_fondo}")
        
    def lugar(self,lugar_in):
        self._lugar=lugar_in
    
    def _colorsec(self):
        pass
    
    def imprimir(self):
        print(f"""Esta es una estrella con:
              Nombre = {self.nombre}
              Tamaño = {self.tamano}
              Puntas = {self.num_puntas}
              Fondo = {self.color_fondo}
              Borde = {self.color_borde}
              """)
              
class marrones(estrella):
    
    def __init__(estrella,
                 tamano_in,
                 nombre_in,
                 num_puntas_in,
                 color_borde = "Marron",
                 color_fondo="Marron"
                         ):
        
        estrella.tamano = tamano_in
        estrella.nombre = nombre_in
        estrella.num_puntas = num_puntas_in
        estrella.color_borde="Marrón"
        estrella.color_fondo = "Marrón"
        
    def ponerconst(self, constelacion):
        self.constelacion = constelacion
                