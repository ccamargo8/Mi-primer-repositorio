def actualizar_estado_persona(operaciones_usuario, pagina_default):
    
    pila_atras = []
    pagina_actual = pagina_default
    pila_adelante = []

    for i in operaciones_usuario:
        if ((i !='atras') and (i != 'adelante') and (i != pagina_actual)):
            pila_atras.append(pagina_actual)
            pagina_actual = i
            pila_adelante.clear()
        if i == 'atras':
             pila_adelante.append(pagina_actual)
             pagina_actual = pila_atras.pop()
        if i == 'adelante':
            pila_atras.append(pagina_actual)
            pagina_actual = pila_adelante.pop()
    
    return pila_atras, pagina_actual, pila_adelante
            

operaciones_usuario = ['udea.edu.co', 'ingeniaudea.co,', 'twitter.com', 'atras', 'atras', 
'adelante', 'facebook.com', 'facebook.com']

pagina_default = 'google.com'

pila_atr, pila_act, pila_ad = actualizar_estado_persona(operaciones_usuario,pagina_default)

print(
    f''' Las paginas anteriores son: {pila_atr}
         La página actual es: {pila_act}
         Las páginas adelantes son: {pila_ad}
    '''
)


