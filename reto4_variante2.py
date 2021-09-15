

def actualizar_estado_persona(operaciones_usuario):
    
    texto_escr = []
    texto_actual = ""
    rehacer = []

    for i in operaciones_usuario:
        if ((i !='DESHACER') and (i != 'REHACER') and (i != texto_actual)):
            texto_escr.append(texto_actual)
            texto_actual = i
            rehacer.clear()
        if i == 'DESHACER':
             rehacer.append(texto_actual)
             texto_actual = texto_escr.pop()
        if i == 'REHACER':
            texto_escr.append(texto_actual)
            texto_actual = rehacer.pop()
        
    texto_escrito="".join(texto_escr)
    
    return texto_escrito
            

operaciones_usuario = ["Definamos qué es una función de Python: ","Una función es ","un arreglo unidimensional de datos", "DESHACER", "DESHACER", "REHACER", "un grupo de instrucciones "]

texto_actual = ""

texto_es = actualizar_estado_persona(operaciones_usuario)

print(texto_es)
