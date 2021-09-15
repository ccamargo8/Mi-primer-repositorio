fichas=["\u2654", "\u2655", "\u2656", "\u2657",
        "\u2658", "\u2659", "\u265A", "\u265B",
        "\u265C", "\u265D", "\u265E", "\u265F"
        ]

class Ajedrez():
    
    fichas=["\u2654", "\u2655", "\u2656", "\u2657",
        "\u2658", "\u2659", "\u265A", "\u265B",
        "\u265C", "\u265D", "\u265E", "\u265F"
        ]
    
    def __init__(self):
        self.reyN=self.fichas[0]
        self.reinaN=self.fichas[1]
        self.torreN=self.fichas[2]
        self.alfilN=self.fichas[3]
        self.caballoN=self.fichas[4]
        self.peonN=self.fichas[5]
        
        self.reyB=self.fichas[6]
        self.reinaB=self.fichas[7]
        self.torreB=self.fichas[8]
        self.alfilB=self.fichas[9]
        self.caballoB=self.fichas[10]
        self.peonB=self.fichas[11]
        
    def construir_tablero(self):
        self.tablero=[[" " for i in range (8)]for i in range (8)]
        
    def ponerfichas(self):
        for i in range(8):
            self.tablero[1][i] = self.peonB
            
        for i in range(8):
            self.tablero[6][i] = self.peonN
            
    def mostrar(self):
        
        for fil in self.tablero:
            for elementos in fil:
                print(elementos, end=" ")
            print()    

miajedrez=Ajedrez()      
miajedrez.construir_tablero()
miajedrez.ponerfichas()  
miajedrez.tablero    
    

