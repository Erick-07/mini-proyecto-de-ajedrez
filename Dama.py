"""
Es la combinacion del alfil y la torre

"""


import grig_general

gridd = grig_general.gridd

class Dama():
    #esas posiciones deben de ser en enteros
    def __init__(self, bando,pieza,posicion_anterior_fila, posicion_anterior_columna, posicion_destino_fila, posicion_destino_columna):
        self.bando = bando #str
        self.pieza = pieza #str
        self.posicion_anterior_fila = posicion_anterior_fila #int
        self.posicion_anterior_columna = posicion_anterior_columna  #int
        self.posicion_destino_fila = posicion_destino_fila #int 
        self.posicion_destino_columna = posicion_destino_columna #int
    
    def movimiento(self,rey):
        casilla_actual = str(self.posicion_anterior_fila)+str(self.posicion_anterior_columna)
        casilla_destino = str(self.posicion_destino_fila)+str(self.posicion_destino_columna)
        cuenta = 0
        enable = True
        x = abs(int(casilla_actual) - int(casilla_destino))
        if x == cuenta:
            cuenta += 1
        if self.bando == "B":
            
            if casilla_actual[0] == casilla_destino[0] and casilla_actual[1] < casilla_destino[1]:
            
            #Derecha
                print("Dama moviendose a la derecha, TEST.")
                if gridd.get_Tablero(self.posicion_destino_fila,self.posicion_destino_columna) != 0:
                    Pieza_de_ocupacion = gridd.get_Tablero(self.posicion_destino_fila,self.posicion_destino_columna)
                
                    if Pieza_de_ocupacion[0] == "B":
                        enable = False

                for i in range(int(casilla_actual),int(casilla_destino)):
                    print(i+1)
                    

                    t = i+1
                    if t < 10:
                        C = str(0)+str(t)
                        fi = C[0]
                        co = C[1]
                        fila = int(fi)
                        columna = int(co)
                        
                    else: 
                        
                        fila = str(i+1)
                        columna = int(fila[1])
                        fila = int(fila[0])

                    if gridd.get_Tablero(self.posicion_destino_fila,self.posicion_destino_columna) != 0:
                        Pieza_de_ocupacion = gridd.get_Tablero(self.posicion_destino_fila,self.posicion_destino_columna)
                
                        
                        if gridd.get_Tablero(fila,columna) == 0 or Pieza_de_ocupacion[0] == "N" and enable:  
                        
                            cuenta += 1
                    elif gridd.get_Tablero(fila,columna) == 0 and enable:
                        cuenta += 1

                    else:
                        print("Casilla ocupada.")
                        return False
                
                if cuenta == x: 
                    print(gridd.printeo())
                    pieza_a_guardar = gridd.get_Tablero(self.posicion_destino_fila,self.posicion_destino_columna)
                    grig_general.gridd = gridd.set_Tablero(self.posicion_destino_fila,self.posicion_destino_columna,str(self.bando)+str(self.pieza)+str(self.posicion_destino_fila)+str(self.posicion_destino_columna))
                    grig_general.gridd = gridd.set_Tablero(self.posicion_anterior_fila,self.posicion_anterior_columna,0)

                    rey.restricciones(rey.posicion_anterior_fila,rey.posicion_anterior_columna)
                    if rey.Index_jaque >= 1:
                        grig_general.gridd = gridd.set_Tablero(self.posicion_destino_fila,self.posicion_destino_columna,pieza_a_guardar)
                        grig_general.gridd = gridd.set_Tablero(self.posicion_anterior_fila,self.posicion_anterior_columna,self.bando+self.pieza+str(self.posicion_anterior_fila)+str(self.posicion_anterior_columna))
                        print("Rey en jaque.")
                        return False
                    else:
                        print("Moviemiento valido.")
                        return True
                         
                
        
            #Abajo
            if casilla_actual[0] > casilla_destino[0] and casilla_actual[1] == casilla_destino[1]:
                print("Moviendose abajo.")
                if gridd.get_Tablero(self.posicion_destino_fila,self.posicion_destino_columna) != 0:
                    Pieza_de_ocupacion = gridd.get_Tablero(self.posicion_destino_fila,self.posicion_destino_columna)
                
                    if Pieza_de_ocupacion[0] == "B":
                        enable = False

                for i in range(int(casilla_actual),int(casilla_destino),-10):
                    print(i-10)
                    t = i-10
                    if t < 10:
                        C = str(0)+str(t)
                        fi = C[0]
                        co = C[1]
                        fila = int(fi)
                        columna = int(co)
                        
                    else: 

                        fila = str(i-10)
                        columna = int(fila[1])
                        fila = int(fila[0])

                    if gridd.get_Tablero(self.posicion_destino_fila,self.posicion_destino_columna) != 0:
                        Pieza_de_ocupacion = gridd.get_Tablero(self.posicion_destino_fila,self.posicion_destino_columna)
                
                        
                        if gridd.get_Tablero(fila,columna) == 0 or Pieza_de_ocupacion[0] == "N" and enable:  
                        
                            cuenta += 10
                    elif gridd.get_Tablero(fila,columna) == 0 and enable:
                        cuenta += 10

                    else:
                        print("Casilla ocupada.")
                        return False
                
                if cuenta == x:
                    print("Moviemiento valido.")
                    print(gridd.printeo())
                    print(gridd.printeo())
                    pieza_a_guardar = gridd.get_Tablero(self.posicion_destino_fila,self.posicion_destino_columna)
                    grig_general.gridd = gridd.set_Tablero(self.posicion_destino_fila,self.posicion_destino_columna,str(self.bando)+str(self.pieza)+str(self.posicion_destino_fila)+str(self.posicion_destino_columna))
                    grig_general.gridd = gridd.set_Tablero(self.posicion_anterior_fila,self.posicion_anterior_columna,0)

                    rey.restricciones(rey.posicion_anterior_fila,rey.posicion_anterior_columna)
                    if rey.Index_jaque >= 1:
                        grig_general.gridd = gridd.set_Tablero(self.posicion_destino_fila,self.posicion_destino_columna,pieza_a_guardar)
                        grig_general.gridd = gridd.set_Tablero(self.posicion_anterior_fila,self.posicion_anterior_columna,self.bando+self.pieza+str(self.posicion_anterior_fila)+str(self.posicion_anterior_columna))
                        print("Rey en jaque.")
                        return False
                    else:
                        print("Moviemiento valido.")
                        return True

                 

            #Izquierda
            if casilla_actual[0] == casilla_destino[0] and casilla_actual[1] > casilla_destino[1]:
                print("Moviendose a la izquierda")
                if gridd.get_Tablero(self.posicion_destino_fila,self.posicion_destino_columna) != 0:
                    Pieza_de_ocupacion = gridd.get_Tablero(self.posicion_destino_fila,self.posicion_destino_columna)
                
                    if Pieza_de_ocupacion[0] == "B":
                        enable = False

                for i in range(int(casilla_actual),int(casilla_destino),-1):
                    print(i+1)
                    

                    t = i-1
                    if t < 10:
                        C = str(0)+str(t)
                        fi = C[0]
                        co = C[1]
                        fila = int(fi)
                        columna = int(co)
                        
                    else: 
                        
                        fila = str(i-1)
                        columna = int(fila[1])
                        fila = int(fila[0])

                    if gridd.get_Tablero(self.posicion_destino_fila,self.posicion_destino_columna) != 0:
                        Pieza_de_ocupacion = gridd.get_Tablero(self.posicion_destino_fila,self.posicion_destino_columna)
                
                        
                        if gridd.get_Tablero(fila,columna) == 0 or Pieza_de_ocupacion[0] == "N" and enable:  
                        
                            cuenta += 1
                    elif gridd.get_Tablero(fila,columna) == 0 and enable:
                        cuenta += 1

                    else:
                        print("Casilla ocupada.")
                        return False
                 
                if cuenta == x:
                    print("Moviemiento valido.")
                    print(gridd.printeo(),"HEREEKjfhsjkldhfksdhfk")
                    print(gridd.printeo())
                    pieza_a_guardar = gridd.get_Tablero(self.posicion_destino_fila,self.posicion_destino_columna)
                    grig_general.gridd = gridd.set_Tablero(self.posicion_destino_fila,self.posicion_destino_columna,str(self.bando)+str(self.pieza)+str(self.posicion_destino_fila)+str(self.posicion_destino_columna))
                    grig_general.gridd = gridd.set_Tablero(self.posicion_anterior_fila,self.posicion_anterior_columna,0)

                    rey.restricciones(rey.posicion_anterior_fila,rey.posicion_anterior_columna)
                    if rey.Index_jaque >= 1:
                        grig_general.gridd = gridd.set_Tablero(self.posicion_destino_fila,self.posicion_destino_columna,pieza_a_guardar)
                        grig_general.gridd = gridd.set_Tablero(self.posicion_anterior_fila,self.posicion_anterior_columna,self.bando+self.pieza+str(self.posicion_anterior_fila)+str(self.posicion_anterior_columna))
                        print("Rey en jaque.")
                        return False
                    else:
                        print("Moviemiento valido.")
                        return True

                   

            #Arriba
            if casilla_actual[0] < casilla_destino[0] and casilla_actual[1] == casilla_destino[1]:
                print("Moviendose arriba.")
                if gridd.get_Tablero(self.posicion_destino_fila,self.posicion_destino_columna) != 0:
                    Pieza_de_ocupacion = gridd.get_Tablero(self.posicion_destino_fila,self.posicion_destino_columna)
                
                    if Pieza_de_ocupacion[0] == "B":
                        enable = False

                for i in range(int(casilla_actual),int(casilla_destino),+10):
                    print(i+10)
                    t = i+10
                    if t < 10:
                        C = str(0)+str(t)
                        fi = C[0]
                        co = C[1]
                        fila = int(fi)
                        columna = int(co)
                        
                    else: 

                        fila = str(i+10)
                        columna = int(fila[1])
                        fila = int(fila[0])

                    if gridd.get_Tablero(self.posicion_destino_fila,self.posicion_destino_columna) != 0:
                        Pieza_de_ocupacion = gridd.get_Tablero(self.posicion_destino_fila,self.posicion_destino_columna)
                
                        
                        if gridd.get_Tablero(fila,columna) == 0 or Pieza_de_ocupacion[0] == "N" and enable:  
                        
                            cuenta += 10
                    elif gridd.get_Tablero(fila,columna) == 0 and enable:
                        cuenta += 10

                    else:
                        print("Casilla ocupada.")
                        return False
                
                if cuenta == x:
                    print("Moviemiento valido.")
                    print(gridd.printeo())
                    print(gridd.printeo())
                    pieza_a_guardar = gridd.get_Tablero(self.posicion_destino_fila,self.posicion_destino_columna)
                    grig_general.gridd = gridd.set_Tablero(self.posicion_destino_fila,self.posicion_destino_columna,str(self.bando)+str(self.pieza)+str(self.posicion_destino_fila)+str(self.posicion_destino_columna))
                    grig_general.gridd = gridd.set_Tablero(self.posicion_anterior_fila,self.posicion_anterior_columna,0)

                    rey.restricciones(rey.posicion_anterior_fila,rey.posicion_anterior_columna)
                    if rey.Index_jaque >= 1:
                        grig_general.gridd = gridd.set_Tablero(self.posicion_destino_fila,self.posicion_destino_columna,pieza_a_guardar)
                        grig_general.gridd = gridd.set_Tablero(self.posicion_anterior_fila,self.posicion_anterior_columna,self.bando+self.pieza+str(self.posicion_anterior_fila)+str(self.posicion_anterior_columna))
                        print("Rey en jaque.")
                        return False
                    else:
                        print("Moviemiento valido.")
                        return True

                  
                    
            #endRegion Torre.

            #Region Alfil.
            x = abs(int(casilla_actual[0]) - int(casilla_destino[0]))
            casilla_actual = int(casilla_actual)
            casilla_destino = int(casilla_destino)
            
            if (casilla_actual + (9*x)) == casilla_destino:
                print("diagonal izquierda subiendo.")
                if gridd.get_Tablero(self.posicion_destino_fila,self.posicion_destino_columna) != 0:
                    Pieza_enemiga = gridd.get_Tablero(self.posicion_destino_fila,self.posicion_destino_columna)
                    
                    if Pieza_enemiga[0] == "N":
                        cuenta += 1
                    if  Pieza_enemiga[0] == "B":
                        enable = False

                for i in range(casilla_actual,casilla_destino,9):
                    
                    t = i+9
                    if t < 10:
                        C = str(0)+str(t)
                        fi = C[0]
                        co = C[1]
                        fila = int(fi)
                        columna = int(co)
                    
                    
                    else:

                        fila = str(i+9)
                        columna = int(fila[1])
                        fila = int(fila[0])
                        print(fila,columna)
                    
                    if gridd.get_Tablero(fila,columna) == 0 and enable:
                        cuenta += 1 
                    else:
                        print("Movimiento invalido del Alfil.")
                        break
                

                if cuenta == x:
                    print(gridd.printeo())
                    pieza_a_guardar = gridd.get_Tablero(self.posicion_destino_fila,self.posicion_destino_columna)
                    grig_general.gridd = gridd.set_Tablero(self.posicion_destino_fila,self.posicion_destino_columna,str(self.bando)+str(self.pieza)+str(self.posicion_destino_fila)+str(self.posicion_destino_columna))
                    grig_general.gridd = gridd.set_Tablero(self.posicion_anterior_fila,self.posicion_anterior_columna,0)

                    rey.restricciones(rey.posicion_anterior_fila,rey.posicion_anterior_columna)
                    if rey.Index_jaque >= 1:
                        grig_general.gridd = gridd.set_Tablero(self.posicion_destino_fila,self.posicion_destino_columna,pieza_a_guardar)
                        grig_general.gridd = gridd.set_Tablero(self.posicion_anterior_fila,self.posicion_anterior_columna,self.bando+self.pieza+str(self.posicion_anterior_fila)+str(self.posicion_anterior_columna))
                        print("Rey en jaque.")
                        return False
                    else:
                        print("Moviemiento valido.")
                        return True
                else:
                    return False

               
            #diagonal abajo derecha.
            if (casilla_actual - (9*x)) == casilla_destino:
                print("diagonal abajo derecha")
                if gridd.get_Tablero(self.posicion_destino_fila,self.posicion_destino_columna) != 0:
                    Pieza_enemiga = gridd.get_Tablero(self.posicion_destino_fila,self.posicion_destino_columna)
               
                    if Pieza_enemiga[0] == "N":
                        cuenta += 1
                    if  Pieza_enemiga[0] == "B":
                        enable = False
                for i in range(casilla_actual,casilla_destino,-9):
            
                    t = i-9
                    if t < 10:
                        C = str(0)+str(t)
                        fi = C[0]
                        co = C[1]
                        fila = int(fi)
                        columna = int(co)
                    
                    
                    else:

                        fila = str(i-9)
                        columna = int(fila[1])
                        fila = int(fila[0])
                        print(fila,columna)
                    
                    if gridd.get_Tablero(fila,columna) == 0 and enable:
                        print("Pieza a Capturar")
                        cuenta += 1 
                    else:
                        print("Movimiento invalido del Alfil.")
                        break
                print(gridd.get_Tablero(self.posicion_anterior_fila,self.posicion_anterior_columna))

                if cuenta == x:
                    print(gridd.printeo())
                    pieza_a_guardar = gridd.get_Tablero(self.posicion_destino_fila,self.posicion_destino_columna)
                    grig_general.gridd = gridd.set_Tablero(self.posicion_destino_fila,self.posicion_destino_columna,str(self.bando)+str(self.pieza)+str(self.posicion_destino_fila)+str(self.posicion_destino_columna))
                    grig_general.gridd = gridd.set_Tablero(self.posicion_anterior_fila,self.posicion_anterior_columna,0)

                    rey.restricciones(rey.posicion_anterior_fila,rey.posicion_anterior_columna)
                    if rey.Index_jaque >= 1:
                        grig_general.gridd = gridd.set_Tablero(self.posicion_destino_fila,self.posicion_destino_columna,pieza_a_guardar)
                        grig_general.gridd = gridd.set_Tablero(self.posicion_anterior_fila,self.posicion_anterior_columna,self.bando+self.pieza+str(self.posicion_anterior_fila)+str(self.posicion_anterior_columna))
                        print("Rey en jaque.")
                        return False
                    else:
                        print("Moviemiento valido.")
                        return True
                else:
                    return False

            if (casilla_actual + (11*x)) == casilla_destino:
                print("diagonal arriba derecha")

                if gridd.get_Tablero(self.posicion_destino_fila,self.posicion_destino_columna) != 0:
                    Pieza_enemiga = gridd.get_Tablero(self.posicion_destino_fila,self.posicion_destino_columna)
               
                    if Pieza_enemiga[0] == "N":
                        cuenta += 1
                    if  Pieza_enemiga[0] == "B":
                        enable = False

                for i in range(casilla_actual,casilla_destino,11):
            
                    t = i+11
                    if t < 10:
                        C = str(0)+str(t)
                        fi = C[0]
                        co = C[1]
                        fila = int(fi)
                        columna = int(co)
                    
                    
                    else:

                        fila = str(i+11)
                        columna = int(fila[1])
                        fila = int(fila[0])
                        print(fila,columna)
                    
                    if gridd.get_Tablero(fila,columna) == 0 and enable:
                        print("Pieza a Capturar")
                        cuenta += 1 
                    else:
                        print("Movimiento invalido del Alfil.")
                        break
                print(gridd.get_Tablero(self.posicion_anterior_fila,self.posicion_anterior_columna))

                if cuenta == x:
                    print(gridd.printeo())
                    pieza_a_guardar = gridd.get_Tablero(self.posicion_destino_fila,self.posicion_destino_columna)
                    grig_general.gridd = gridd.set_Tablero(self.posicion_destino_fila,self.posicion_destino_columna,str(self.bando)+str(self.pieza)+str(self.posicion_destino_fila)+str(self.posicion_destino_columna))
                    grig_general.gridd = gridd.set_Tablero(self.posicion_anterior_fila,self.posicion_anterior_columna,0)

                    rey.restricciones(rey.posicion_anterior_fila,rey.posicion_anterior_columna)
                    if rey.Index_jaque >= 1:
                        grig_general.gridd = gridd.set_Tablero(self.posicion_destino_fila,self.posicion_destino_columna,pieza_a_guardar)
                        grig_general.gridd = gridd.set_Tablero(self.posicion_anterior_fila,self.posicion_anterior_columna,self.bando+self.pieza+str(self.posicion_anterior_fila)+str(self.posicion_anterior_columna))
                        print("Rey en jaque.")
                        return False
                    else:
                        print("Moviemiento valido.")
                        return True
                else:
                    return False

            if (casilla_actual - (11*x)) == casilla_destino:
                print("diagonal abajo izquierda.")
                if gridd.get_Tablero(self.posicion_destino_fila,self.posicion_destino_columna) != 0:
                    Pieza_enemiga = gridd.get_Tablero(self.posicion_destino_fila,self.posicion_destino_columna)
               
                    if Pieza_enemiga[0] == "N":
                        cuenta += 1
                    if  Pieza_enemiga[0] == "B":
                        enable = False

                for i in range(casilla_actual,casilla_destino,-11):
            
                    t = i-11
                    if t < 10:
                        C = str(0)+str(t)
                        fi = C[0]
                        co = C[1]
                        fila = int(fi)
                        columna = int(co)
                    
                    
                    else:

                        fila = str(i-11)
                        columna = int(fila[1])
                        fila = int(fila[0])
                        print(fila,columna)
                    
                    if gridd.get_Tablero(fila,columna) == 0 and enable:
                        print("Pieza a Capturar")
                        cuenta += 1 
                    else:
                        print("Movimiento invalido del Alfil.")
                        break
                print(gridd.get_Tablero(self.posicion_anterior_fila,self.posicion_anterior_columna))

                if cuenta == x:
                    print(gridd.printeo())
                    pieza_a_guardar = gridd.get_Tablero(self.posicion_destino_fila,self.posicion_destino_columna)
                    grig_general.gridd = gridd.set_Tablero(self.posicion_destino_fila,self.posicion_destino_columna,str(self.bando)+str(self.pieza)+str(self.posicion_destino_fila)+str(self.posicion_destino_columna))
                    grig_general.gridd = gridd.set_Tablero(self.posicion_anterior_fila,self.posicion_anterior_columna,0)

                    rey.restricciones(rey.posicion_anterior_fila,rey.posicion_anterior_columna)
                    if rey.Index_jaque >= 1:
                        grig_general.gridd = gridd.set_Tablero(self.posicion_destino_fila,self.posicion_destino_columna,pieza_a_guardar)
                        grig_general.gridd = gridd.set_Tablero(self.posicion_anterior_fila,self.posicion_anterior_columna,self.bando+self.pieza+str(self.posicion_anterior_fila)+str(self.posicion_anterior_columna))
                        print("Rey en jaque.")
                        return False
                    else:
                        print("Moviemiento valido.")
                        return True
                else:
                    return False


            #endRegion Alfil.


        #Reigon Dama negra.

        elif self.bando == "N":
            #Region Torre.
            
            
        
            #Derecha
            if casilla_actual[0] == casilla_destino[0] and casilla_actual[1] < casilla_destino[1]:
                print("Torre moviendose a la derecha, TEST.")
                if gridd.get_Tablero(self.posicion_destino_fila,self.posicion_destino_columna) != 0:
                    Pieza_de_ocupacion = gridd.get_Tablero(self.posicion_destino_fila,self.posicion_destino_columna)
                
                    if Pieza_de_ocupacion[0] == "N":
                        enable = False

                for i in range(int(casilla_actual),int(casilla_destino)):
                    print(i+1)
                    

                    t = i+1
                    if t < 10:
                        C = str(0)+str(t)
                        fi = C[0]
                        co = C[1]
                        fila = int(fi)
                        columna = int(co)
                        
                    else: 
                        
                        fila = str(i+1)
                        columna = int(fila[1])
                        fila = int(fila[0])

                    if gridd.get_Tablero(self.posicion_destino_fila,self.posicion_destino_columna) != 0:
                        Pieza_de_ocupacion = gridd.get_Tablero(self.posicion_destino_fila,self.posicion_destino_columna)

                        if gridd.get_Tablero(fila,columna) == 0 or Pieza_de_ocupacion[0] == "B" and enable:  
                        
                            cuenta += 1
                    elif gridd.get_Tablero(fila,columna) == 0 and enable:
                        cuenta += 1

                    else:
                        print("Casilla ocupada.")
                        return False
                
                if cuenta == x:
                    print("Moviemiento valido.")
                    print(gridd.printeo(),"HEREEKjfhsjkldhfksdhfk")
                    print(gridd.printeo())
                    pieza_a_guardar = gridd.get_Tablero(self.posicion_destino_fila,self.posicion_destino_columna)
                    grig_general.gridd = gridd.set_Tablero(self.posicion_destino_fila,self.posicion_destino_columna,str(self.bando)+str(self.pieza)+str(self.posicion_destino_fila)+str(self.posicion_destino_columna))
                    grig_general.gridd = gridd.set_Tablero(self.posicion_anterior_fila,self.posicion_anterior_columna,0)

                    rey.restricciones(rey.posicion_anterior_fila,rey.posicion_anterior_columna)
                    if rey.Index_jaque >= 1:
                        grig_general.gridd = gridd.set_Tablero(self.posicion_destino_fila,self.posicion_destino_columna,pieza_a_guardar)
                        grig_general.gridd = gridd.set_Tablero(self.posicion_anterior_fila,self.posicion_anterior_columna,self.bando+self.pieza+str(self.posicion_anterior_fila)+str(self.posicion_anterior_columna))
                        print("Rey en jaque.")
                        return False
                    else:
                        print("Moviemiento valido.")
                        return True
                    

            #Abajo
            if casilla_actual[0] > casilla_destino[0] and casilla_actual[1] == casilla_destino[1]:
                print("Moviendose abajo.")
                if gridd.get_Tablero(self.posicion_destino_fila,self.posicion_destino_columna) != 0:
                    Pieza_de_ocupacion = gridd.get_Tablero(self.posicion_destino_fila,self.posicion_destino_columna)
                
                    if Pieza_de_ocupacion[0] == "N":
                        enable = False

                for i in range(int(casilla_actual),int(casilla_destino),-10):
                    print(i-10)
                    t = i-10
                    if t < 10:
                        C = str(0)+str(t)
                        fi = C[0]
                        co = C[1]
                        fila = int(fi)
                        columna = int(co)
                        
                    else: 

                        fila = str(i-10)
                        columna = int(fila[1])
                        fila = int(fila[0])

                    if gridd.get_Tablero(self.posicion_destino_fila,self.posicion_destino_columna) != 0:
                        Pieza_de_ocupacion = gridd.get_Tablero(self.posicion_destino_fila,self.posicion_destino_columna)

                        if gridd.get_Tablero(fila,columna) == 0 or Pieza_de_ocupacion[0] == "B" and enable:  
                        
                            cuenta += 10
                    elif gridd.get_Tablero(fila,columna) == 0 and enable:
                        cuenta += 10

                    else:
                        print("Casilla ocupada.")
                        return False
                
                if cuenta == x:
                    print("Moviemiento valido.")
                    print(gridd.printeo())
               
                    pieza_a_guardar = gridd.get_Tablero(self.posicion_destino_fila,self.posicion_destino_columna)
                    grig_general.gridd = gridd.set_Tablero(self.posicion_destino_fila,self.posicion_destino_columna,str(self.bando)+str(self.pieza)+str(self.posicion_destino_fila)+str(self.posicion_destino_columna))
                    grig_general.gridd = gridd.set_Tablero(self.posicion_anterior_fila,self.posicion_anterior_columna,0)

                    rey.restricciones(rey.posicion_anterior_fila,rey.posicion_anterior_columna)
                    if rey.Index_jaque >= 1:
                        grig_general.gridd = gridd.set_Tablero(self.posicion_destino_fila,self.posicion_destino_columna,pieza_a_guardar)
                        grig_general.gridd = gridd.set_Tablero(self.posicion_anterior_fila,self.posicion_anterior_columna,self.bando+self.pieza+str(self.posicion_anterior_fila)+str(self.posicion_anterior_columna))
                        print("Rey en jaque.")
                        return False
                    else:
                        print("Moviemiento valido.")
                        return True
                    print(gridd.printeo())

            #Izquierda
            if casilla_actual[0] == casilla_destino[0] and casilla_actual[1] > casilla_destino[1]:
                print("Moviendose a la izquierda")
                if gridd.get_Tablero(self.posicion_destino_fila,self.posicion_destino_columna) != 0:
                    Pieza_de_ocupacion = gridd.get_Tablero(self.posicion_destino_fila,self.posicion_destino_columna)
                
                    if Pieza_de_ocupacion[0] == "N":
                        enable = False

                for i in range(int(casilla_actual),int(casilla_destino),-1):
                    print(i+1)
                    

                    t = i-1
                    if t < 10:
                        C = str(0)+str(t)
                        fi = C[0]
                        co = C[1]
                        fila = int(fi)
                        columna = int(co)
                        
                    else: 
                        
                        fila = str(i-1)
                        columna = int(fila[1])
                        fila = int(fila[0])

                    if gridd.get_Tablero(self.posicion_destino_fila,self.posicion_destino_columna) != 0:
                        Pieza_de_ocupacion = gridd.get_Tablero(self.posicion_destino_fila,self.posicion_destino_columna)

                        if gridd.get_Tablero(fila,columna) == 0 or Pieza_de_ocupacion[0] == "B" and enable:  
                        
                            cuenta += 1
                    elif gridd.get_Tablero(fila,columna) == 0 and enable:
                        cuenta += 1

                    else:
                        print("Casilla ocupada.")
                        return False
                
                if cuenta == x:
                    print("Moviemiento valido.")
                    print(gridd.printeo(),"HEREEKjfhsjkldhfksdhfk")
                    print(gridd.printeo())
                    pieza_a_guardar = gridd.get_Tablero(self.posicion_destino_fila,self.posicion_destino_columna)
                    grig_general.gridd = gridd.set_Tablero(self.posicion_destino_fila,self.posicion_destino_columna,str(self.bando)+str(self.pieza)+str(self.posicion_destino_fila)+str(self.posicion_destino_columna))
                    grig_general.gridd = gridd.set_Tablero(self.posicion_anterior_fila,self.posicion_anterior_columna,0)

                    rey.restricciones(rey.posicion_anterior_fila,rey.posicion_anterior_columna)
                    if rey.Index_jaque >= 1:
                        grig_general.gridd = gridd.set_Tablero(self.posicion_destino_fila,self.posicion_destino_columna,pieza_a_guardar)
                        grig_general.gridd = gridd.set_Tablero(self.posicion_anterior_fila,self.posicion_anterior_columna,self.bando+self.pieza+str(self.posicion_anterior_fila)+str(self.posicion_anterior_columna))
                        print("Rey en jaque.")
                        return False
                    else:
                        print("Moviemiento valido.")
                        return True
                    print(gridd.printeo())

            #Arriba
            if casilla_actual[0] < casilla_destino[0] and casilla_actual[1] == casilla_destino[1]:
                print("Moviendose arriba.")
                if gridd.get_Tablero(self.posicion_destino_fila,self.posicion_destino_columna) != 0:
                    Pieza_de_ocupacion = gridd.get_Tablero(self.posicion_destino_fila,self.posicion_destino_columna)
                
                    if Pieza_de_ocupacion[0] == "N":
                        enable = False

                for i in range(int(casilla_actual),int(casilla_destino),+10):
                    print(i+10)
                    t = i+10
                    if t < 10:
                        C = str(0)+str(t)
                        fi = C[0]
                        co = C[1]
                        fila = int(fi)
                        columna = int(co)
                        
                    else: 

                        fila = str(i+10)
                        columna = int(fila[1])
                        fila = int(fila[0])

                    if gridd.get_Tablero(self.posicion_destino_fila,self.posicion_destino_columna) != 0:
                        Pieza_de_ocupacion = gridd.get_Tablero(self.posicion_destino_fila,self.posicion_destino_columna)

                        if gridd.get_Tablero(fila,columna) == 0 or Pieza_de_ocupacion[0] == "B" and enable:  
                        
                            cuenta += 10
                    elif gridd.get_Tablero(fila,columna) == 0 and enable:
                        cuenta += 10

                    else:
                        print("Casilla ocupada.")
                        return False
                
                if cuenta == x:
                    print("Moviemiento valido.")
                    print(gridd.printeo())
                    print(gridd.printeo())
                    pieza_a_guardar = gridd.get_Tablero(self.posicion_destino_fila,self.posicion_destino_columna)
                    grig_general.gridd = gridd.set_Tablero(self.posicion_destino_fila,self.posicion_destino_columna,str(self.bando)+str(self.pieza)+str(self.posicion_destino_fila)+str(self.posicion_destino_columna))
                    grig_general.gridd = gridd.set_Tablero(self.posicion_anterior_fila,self.posicion_anterior_columna,0)

                    rey.restricciones(rey.posicion_anterior_fila,rey.posicion_anterior_columna)
                    if rey.Index_jaque >= 1:
                        grig_general.gridd = gridd.set_Tablero(self.posicion_destino_fila,self.posicion_destino_columna,pieza_a_guardar)
                        grig_general.gridd = gridd.set_Tablero(self.posicion_anterior_fila,self.posicion_anterior_columna,self.bando+self.pieza+str(self.posicion_anterior_fila)+str(self.posicion_anterior_columna))
                        print("Rey en jaque.")
                        return False
                    else:
                        print("Moviemiento valido.")
                        return True 

            #endRegion Torre.

  
            #Region Alfil.
            #movimiento en diagonal izquierda subiendo.
            
            x = abs(int(casilla_actual[0]) - int(casilla_destino[0]))
            casilla_actual = int(casilla_actual)
            casilla_destino = int(casilla_destino)
             
            
            #diagonal izquierda subiendo.
            if (casilla_actual + (9*x)) == casilla_destino:
                print("diagonal izquierda subiendo.")

                if gridd.get_Tablero(self.posicion_destino_fila,self.posicion_destino_columna) != 0:
                    Pieza_enemiga = gridd.get_Tablero(self.posicion_destino_fila,self.posicion_destino_columna)
               
                    if Pieza_enemiga[0] == "B":
                        cuenta += 1
                    if  Pieza_enemiga[0] == "N":
                        enable = False

                for i in range(casilla_actual,casilla_destino,9):
            
                    t = i+9
                    if t < 10:
                        C = str(0)+str(t)
                        fi = C[0]
                        co = C[1]
                        fila = int(fi)
                        columna = int(co)
                    
                    
                    else:

                        fila = str(i+9)
                        columna = int(fila[1])
                        fila = int(fila[0])
                        print(fila,columna)
                    
                    if gridd.get_Tablero(fila,columna) == 0 and enable:
                        print("Pieza a Capturar")
                        cuenta += 1 
                    else:
                        print("Movimiento invalido del Alfil.")
                        break
                

                if cuenta == x:
                    print(gridd.printeo())
                    pieza_a_guardar = gridd.get_Tablero(self.posicion_destino_fila,self.posicion_destino_columna)
                    grig_general.gridd = gridd.set_Tablero(self.posicion_destino_fila,self.posicion_destino_columna,str(self.bando)+str(self.pieza)+str(self.posicion_destino_fila)+str(self.posicion_destino_columna))
                    grig_general.gridd = gridd.set_Tablero(self.posicion_anterior_fila,self.posicion_anterior_columna,0)

                    rey.restricciones(rey.posicion_anterior_fila,rey.posicion_anterior_columna)
                    if rey.Index_jaque >= 1:
                        grig_general.gridd = gridd.set_Tablero(self.posicion_destino_fila,self.posicion_destino_columna,pieza_a_guardar)
                        grig_general.gridd = gridd.set_Tablero(self.posicion_anterior_fila,self.posicion_anterior_columna,self.bando+self.pieza+str(self.posicion_anterior_fila)+str(self.posicion_anterior_columna))
                        print("Rey en jaque.")
                        return False
                    else:
                        print("Moviemiento valido.")
                        return True
                else:
                    return False

                print(gridd.get_Tablero(self.posicion_anterior_fila,self.posicion_anterior_columna))

            #diagonal abajo derecha.
            if (casilla_actual - (9*x)) == casilla_destino:
                print("diagonal abajo derecha")

                if gridd.get_Tablero(self.posicion_destino_fila,self.posicion_destino_columna) != 0:
                    Pieza_enemiga = gridd.get_Tablero(self.posicion_destino_fila,self.posicion_destino_columna)
               
                    if Pieza_enemiga[0] == "B":
                        cuenta += 1
                    if  Pieza_enemiga[0] == "N":
                        enable = False

                for i in range(casilla_actual,casilla_destino,-9):
            
                    t = i-9
                    if t < 10:
                        C = str(0)+str(t)
                        fi = C[0]
                        co = C[1]
                        fila = int(fi)
                        columna = int(co)
                    
                    
                    else:

                        fila = str(i-9)
                        columna = int(fila[1])
                        fila = int(fila[0])
                        print(fila,columna)
                    
                    if gridd.get_Tablero(fila,columna) == 0 and enable:
                        print("Pieza a Capturar")
                        cuenta += 1 
                    else:
                        print("Movimiento invalido del Alfil.")
                        break
                print(gridd.get_Tablero(self.posicion_anterior_fila,self.posicion_anterior_columna))

                if cuenta == x:
                    print(gridd.printeo())
                    pieza_a_guardar = gridd.get_Tablero(self.posicion_destino_fila,self.posicion_destino_columna)
                    grig_general.gridd = gridd.set_Tablero(self.posicion_destino_fila,self.posicion_destino_columna,str(self.bando)+str(self.pieza)+str(self.posicion_destino_fila)+str(self.posicion_destino_columna))
                    grig_general.gridd = gridd.set_Tablero(self.posicion_anterior_fila,self.posicion_anterior_columna,0)

                    rey.restricciones(rey.posicion_anterior_fila,rey.posicion_anterior_columna)
                    if rey.Index_jaque >= 1:
                        grig_general.gridd = gridd.set_Tablero(self.posicion_destino_fila,self.posicion_destino_columna,pieza_a_guardar)
                        grig_general.gridd = gridd.set_Tablero(self.posicion_anterior_fila,self.posicion_anterior_columna,self.bando+self.pieza+str(self.posicion_anterior_fila)+str(self.posicion_anterior_columna))
                        print("Rey en jaque.")
                        return False
                    else:
                        print("Moviemiento valido.")
                        return True
                else:
                    return False


            if (casilla_actual + (11*x)) == casilla_destino:
                print("diagonal arriba derecha")

                if gridd.get_Tablero(self.posicion_destino_fila,self.posicion_destino_columna) != 0:
                    Pieza_enemiga = gridd.get_Tablero(self.posicion_destino_fila,self.posicion_destino_columna)
               
                    if Pieza_enemiga[0] == "B":
                        cuenta += 1
                    if  Pieza_enemiga[0] == "N":
                        enable = False

                for i in range(casilla_actual,casilla_destino,11):
            
                    t = i+11
                    if t < 10:
                        C = str(0)+str(t)
                        fi = C[0]
                        co = C[1]
                        fila = int(fi)
                        columna = int(co)
                    
                    
                    else:

                        fila = str(i+11)
                        columna = int(fila[1])
                        fila = int(fila[0])
                        print(fila,columna)
                    
                    if gridd.get_Tablero(fila,columna) == 0 and enable:
                        print("Pieza a Capturar")
                        cuenta += 1 
                    else:
                        print("Movimiento invalido del Alfil.")
                        break
                print(gridd.get_Tablero(self.posicion_anterior_fila,self.posicion_anterior_columna))

                if cuenta == x:
                    print(gridd.printeo())
                    pieza_a_guardar = gridd.get_Tablero(self.posicion_destino_fila,self.posicion_destino_columna)
                    grig_general.gridd = gridd.set_Tablero(self.posicion_destino_fila,self.posicion_destino_columna,str(self.bando)+str(self.pieza)+str(self.posicion_destino_fila)+str(self.posicion_destino_columna))
                    grig_general.gridd = gridd.set_Tablero(self.posicion_anterior_fila,self.posicion_anterior_columna,0)

                    rey.restricciones(rey.posicion_anterior_fila,rey.posicion_anterior_columna)
                    if rey.Index_jaque >= 1:
                        grig_general.gridd = gridd.set_Tablero(self.posicion_destino_fila,self.posicion_destino_columna,pieza_a_guardar)
                        grig_general.gridd = gridd.set_Tablero(self.posicion_anterior_fila,self.posicion_anterior_columna,self.bando+self.pieza+str(self.posicion_anterior_fila)+str(self.posicion_anterior_columna))
                        print("Rey en jaque.")
                        return False
                    else:
                        print("Moviemiento valido.")
                        return True
                else:
                    return False

            if (casilla_actual - (11*x)) == casilla_destino:
                print("diagonal abajo izquierda.")

                if gridd.get_Tablero(self.posicion_destino_fila,self.posicion_destino_columna) != 0:
                    Pieza_enemiga = gridd.get_Tablero(self.posicion_destino_fila,self.posicion_destino_columna)
               
                    if Pieza_enemiga[0] == "B":
                        cuenta += 1
                    if  Pieza_enemiga[0] == "N":
                        enable = False

                for i in range(casilla_actual,casilla_destino,-11):
            
                    t = i-11
                    if t < 10:
                        C = str(0)+str(t)
                        fi = C[0]
                        co = C[1]
                        fila = int(fi)
                        columna = int(co)
                    
                    
                    else:

                        fila = str(i-11)
                        columna = int(fila[1])
                        fila = int(fila[0])
                        print(fila,columna)
                    
                    if gridd.get_Tablero(fila,columna) == 0 and enable:
                        print("Pieza a Capturar")
                        cuenta += 1 
                    else:
                        print("Movimiento invalido del Alfil.")
                        break
                print(gridd.get_Tablero(self.posicion_anterior_fila,self.posicion_anterior_columna))

                if cuenta == x:
                    print(gridd.printeo())
                    pieza_a_guardar = gridd.get_Tablero(self.posicion_destino_fila,self.posicion_destino_columna)
                    grig_general.gridd = gridd.set_Tablero(self.posicion_destino_fila,self.posicion_destino_columna,str(self.bando)+str(self.pieza)+str(self.posicion_destino_fila)+str(self.posicion_destino_columna))
                    grig_general.gridd = gridd.set_Tablero(self.posicion_anterior_fila,self.posicion_anterior_columna,0)

                    rey.restricciones(rey.posicion_anterior_fila,rey.posicion_anterior_columna)
                    if rey.Index_jaque >= 1:
                        grig_general.gridd = gridd.set_Tablero(self.posicion_destino_fila,self.posicion_destino_columna,pieza_a_guardar)
                        grig_general.gridd = gridd.set_Tablero(self.posicion_anterior_fila,self.posicion_anterior_columna,self.bando+self.pieza+str(self.posicion_anterior_fila)+str(self.posicion_anterior_columna))
                        print("Rey en jaque.")
                        return False
                    else:
                        print("Moviemiento valido.")
                        return True
                else:
                    return False