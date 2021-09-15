libro={}


while True:
    
    print("Datos que puede ingresar:",
          "Titulo[T]",
          "Capitulo[C]",
          "Glosario[G]",
          "Bibliografia[B]",
          "Apendice[A]",
          sep="\n"
          
          )
    dato=input("Que dato desea ingresar?")
    
    if dato.upper()=="T":        
        libro["Titulo"]=input("Ingrese el titulo: ")
    elif dato.upper()=="C":
        while True:
            capitulo=input("Ingrese el nombre del capitulo: ")
            
            
            libro[capitulo]={"Resumen":"",
                             "Numero de paginas":0,
                             "Numero de ilustraciones":0
                             }
            libro[capitulo]["Resumen"]=input(f"Ingrese el resumen del capitulo: {capitulo}: ") 
            libro[capitulo]["numero de paginas"]=input(f"Ingrese el numero de paginas del capitulo: {capitulo}: ") 
            libro[capitulo]["Numero de ilustraciones"]=input(f"Ingrese el numero de ilustraciones del capitulo: {capitulo}: ")                        
                
            temp=input("Desea ingresar otro capitulo? ")
            if temp=="s":
                continue
            else:
                break
                    
                    
        
        
    elif dato.upper()=="G":
        print("Seleccionó Glosario")
    elif dato.upper()=="B":
        print("Seleccionó Bibliografia")
    elif dato.upper()=="A":
        print("Seleccionó apendice")
    
    #Estructura de control de repetición
    var=input("¿Quiere ingresar mas datos?: ")
    
    if var.lower()=="s":
        continue
    elif var.lower()=="n":
        print("Terminó el ingreso de datos")
        break
    else:
        print("No es un caracter valido")



# libro_2 = {"Titulo" : "Titulo del libro",
#          "Capitulo 1: Introducción" :{"Resumen":"el resumen",
#                                       "Numero de paginas": 125,
#                                       "Numero de ilustraciones":4           
             
#                                      },
#          "Capitulo 2: parte 1" :{"Resumen":"el resumen",
#                                  "Numero de paginas": 125,
#                                  "Numero de ilustraciones":4  
#                                  },
#          "Glosario" :{"Palabra":"significado",
#                       "Palabra 1":"Significado1"
#                      },
#          "Bibliografia":"Referencias",
#          "Apendice":"Apendices"
         
#         }

