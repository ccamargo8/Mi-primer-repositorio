import random

class vector():
    
    def __init__(self,tamano):
        self.V=[0]*(tamano+1)
        
    def construyevector(self,n,rango):
        self.V[0]=n
        for i in range(1,n+1):
            self.V[i]=random.randint(1,rango)
        return self.V
    
    def agregardato(self,d,nt):
        if self.esLleno(nt):
            return
        self.V[0]=self.V[0]+1
        self.V[self.V[0]]=d
        
    def esLleno(self,nt):
        if self.V[0]==nt:
            return True
        return False
        
a=vector(5)

a.construyevector(3,1000)

a.agregardato(10,3)

