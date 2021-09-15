def buscarDato(V,d):
    """Programa para buscar un dato en un vector"""
    i=1
    while i<=V[0] and V[i]!=d:
        i=i+1
    if i <= V[0]:
        return i
    return -1

def borrar(V,i):
    """Programa para borrar un dato de un vector"""
    for j in range(i,V[0]):
        V[j]=V[j+1]
    V[0]=V[0]-1    
    
    
def ordenaAscen(V):
      for i in range(1, V[0]):
          k = i
          for j in range(i+1, V[0] + 1):
                if V[j] < V[k]:
                    k = j
                intercambiar(V, i, k)
                
def ordenaAscen(V):
    for i in range(1, V[0]):
        for j in range(1, V[0] – I + 1):
             if V[j] > V[j + 1]:
                    intercambiar(V, j, j + 1)