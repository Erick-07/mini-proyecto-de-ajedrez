
"""

#formulas matematicas

#diagonal izquierda subiendo

La casilla del alfil actual +(9*x)
Sea x el numero de casillas alcanzar.

    Ex: 34 + (9*3)

#diagonal derecha subiendo

    Ex: 34 + (11 * x)

#diagonal bajando derecha 

    Ex: 34 - (9*x)

#diagonal bajando izquierda

    Ex: 34 - (11*x)

Estas funciones es para descartar si esa casilla esta en el rango de movimiento disponible, y no tener que comprobar si en readlidad es cieroto esa casilla.


"""

import grig_general

gridd = grig_general.gridd

class alfill():
    #esas posiciones deben de ser en enteros
    def __init__(self, bando,pieza,posicion_anterior_fila, posicion_anterior_columna, posicion_destino_fila, posicion_destino_columna):
        self.bando = bando #str
        self.pieza = pieza #str
        self.posicion_anterior_fila = posicion_anterior_fila #int
        self.posicion_anterior_columna = posicion_anterior_columna  #int
        self.posicion_destino_fila = posicion_destino_fila #int 
        self.posicion_destino_columna = posicion_destino_columna #int
    
    def movimiento(self,rey):
        enable = False
    
        #Codigo para pieza peon blanca.
        if self.bando == "B": 
            #movimiento en diagonal izquierda subiendo.
            casilla_actual = str(self.posicion_anterior_fila) + str(self.posicion_anterior_columna)
            casilla_destino = str(self.posicion_destino_fila) + str(self.posicion_destino_columna)
            x = abs(int(casilla_actual[0]) - int(casilla_destino[0]))
            cuenta = 0
            casilla_actual = int(casilla_actual)
            casilla_destino = int(casilla_destino)
            enable = True
            if x == cuenta:
                cuenta += 1  
            #diagonal izquierda subiendo.
            if (casilla_actual + (9*x)) == casilla_destino:
                print("diagonal izquierda subiendo.")
                enable = True
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
                    enable_aux = True
                    while enable_aux:
                        

                        print(gridd.printeo())
                        pieza_a_guardar = gridd.get_Tablero(self.posicion_destino_fila,self.posicion_destino_columna)
                        grig_general.gridd = gridd.set_Tablero(self.posicion_destino_fila,self.posicion_destino_columna,self.bando+self.pieza+str(self.posicion_destino_fila)+str(self.posicion_destino_columna))
                        grig_general.gridd = gridd.set_Tablero(self.posicion_anterior_fila,self.posicion_anterior_columna,0)
                        
                        rey.restricciones(rey.posicion_anterior_fila,rey.posicion_anterior_columna)
                        if rey.Index_jaque >= 1:
                            grig_general.gridd = gridd.set_Tablero(self.posicion_destino_fila,self.posicion_destino_columna,pieza_a_guardar)
                            grig_general.gridd = gridd.set_Tablero(self.posicion_anterior_fila,self.posicion_anterior_columna,self.bando+self.pieza+str(self.posicion_anterior_fila)+str(self.posicion_anterior_columna))
                            print("Rey en jaque.")
                            enable_aux = False
                            return False
                        else:
                            enable_aux = False
                            print("Moviemiento valido.")
                            return True
                else:
                    return False
                            
                print(gridd.get_Tablero(self.posicion_anterior_fila,self.posicion_anterior_columna))

            #diagonal abajo derecha.
            if (casilla_actual - (9*x)) == casilla_destino:
                print("diagonal abajo derecha")
                enable = True
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
                    enable_aux = True
                    while enable_aux:
                        

                        print(gridd.printeo())
                        pieza_a_guardar = gridd.get_Tablero(self.posicion_destino_fila,self.posicion_destino_columna)
                        grig_general.gridd = gridd.set_Tablero(self.posicion_destino_fila,self.posicion_destino_columna,self.bando+self.pieza+str(self.posicion_destino_fila)+str(self.posicion_destino_columna))
                        grig_general.gridd = gridd.set_Tablero(self.posicion_anterior_fila,self.posicion_anterior_columna,0)
                        
                        rey.restricciones(rey.posicion_anterior_fila,rey.posicion_anterior_columna)
                        if rey.Index_jaque >= 1:
                            grig_general.gridd = gridd.set_Tablero(self.posicion_destino_fila,self.posicion_destino_columna,pieza_a_guardar)
                            grig_general.gridd = gridd.set_Tablero(self.posicion_anterior_fila,self.posicion_anterior_columna,self.bando+self.pieza+str(self.posicion_anterior_fila)+str(self.posicion_anterior_columna))
                            print("Rey en jaque.")
                            enable_aux = False
                            return False
                        else:
                            enable_aux = False
                            print("Moviemiento valido.")
                            return True
                else:
                    return False

            if (casilla_actual + (11*x)) == casilla_destino:
                print("diagonal arriba derecha")
                enable = True
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
                    enable_aux = True
                    while enable_aux:
                        

                        print(gridd.printeo())
                        pieza_a_guardar = gridd.get_Tablero(self.posicion_destino_fila,self.posicion_destino_columna)
                        grig_general.gridd = gridd.set_Tablero(self.posicion_destino_fila,self.posicion_destino_columna,self.bando+self.pieza+str(self.posicion_destino_fila)+str(self.posicion_destino_columna))
                        grig_general.gridd = gridd.set_Tablero(self.posicion_anterior_fila,self.posicion_anterior_columna,0)
                        
                        rey.restricciones(rey.posicion_anterior_fila,rey.posicion_anterior_columna)
                        if rey.Index_jaque >= 1:
                            grig_general.gridd = gridd.set_Tablero(self.posicion_destino_fila,self.posicion_destino_columna,pieza_a_guardar)
                            grig_general.gridd = gridd.set_Tablero(self.posicion_anterior_fila,self.posicion_anterior_columna,self.bando+self.pieza+str(self.posicion_anterior_fila)+str(self.posicion_anterior_columna))
                            print("Rey en jaque.")
                            enable_aux = False
                            return False
                        else:
                            enable_aux = False
                            print("Moviemiento valido.")
                            return True
                else:
                    return False

            if (casilla_actual - (11*x)) == casilla_destino:
                print("diagonal abajo izquierda.")
                enable = True
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
                    enable_aux = True
                    while enable_aux:
                        

                        print(gridd.printeo())
                        pieza_a_guardar = gridd.get_Tablero(self.posicion_destino_fila,self.posicion_destino_columna)
                        grig_general.gridd = gridd.set_Tablero(self.posicion_destino_fila,self.posicion_destino_columna,self.bando+self.pieza+str(self.posicion_destino_fila)+str(self.posicion_destino_columna))
                        grig_general.gridd = gridd.set_Tablero(self.posicion_anterior_fila,self.posicion_anterior_columna,0)
                        
                        rey.restricciones(rey.posicion_anterior_fila,rey.posicion_anterior_columna)
                        if rey.Index_jaque >= 1:
                            grig_general.gridd = gridd.set_Tablero(self.posicion_destino_fila,self.posicion_destino_columna,pieza_a_guardar)
                            grig_general.gridd = gridd.set_Tablero(self.posicion_anterior_fila,self.posicion_anterior_columna,self.bando+self.pieza+str(self.posicion_anterior_fila)+str(self.posicion_anterior_columna))
                            print("Rey en jaque.")
                            enable_aux = False
                            return False
                        else:
                            enable_aux = False
                            print("Moviemiento valido.")
                            return True
                else:
                    return False

        elif self.bando == "N":
            #movimiento en diagonal izquierda subiendo.
            casilla_actual = str(self.posicion_anterior_fila) + str(self.posicion_anterior_columna)
            casilla_destino = str(self.posicion_destino_fila) + str(self.posicion_destino_columna)
            x = abs(int(casilla_actual[0]) - int(casilla_destino[0]))
            cuenta = 0
            casilla_actual = int(casilla_actual)
            casilla_destino = int(casilla_destino)
            if x == cuenta:
                cuenta += 1  
            
            #diagonal izquierda subiendo.
            if (casilla_actual + (9*x)) == casilla_destino:
                print("diagonal izquierda subiendo.")
                enable = True

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
                    enable_aux = True
                    while enable_aux:
                        

                        print(gridd.printeo())
                        pieza_a_guardar = gridd.get_Tablero(self.posicion_destino_fila,self.posicion_destino_columna)
                        grig_general.gridd = gridd.set_Tablero(self.posicion_destino_fila,self.posicion_destino_columna,self.bando+self.pieza+str(self.posicion_destino_fila)+str(self.posicion_destino_columna))
                        grig_general.gridd = gridd.set_Tablero(self.posicion_anterior_fila,self.posicion_anterior_columna,0)
                        
                        rey.restricciones(rey.posicion_anterior_fila,rey.posicion_anterior_columna)
                        if rey.Index_jaque >= 1:
                            grig_general.gridd = gridd.set_Tablero(self.posicion_destino_fila,self.posicion_destino_columna,pieza_a_guardar)
                            grig_general.gridd = gridd.set_Tablero(self.posicion_anterior_fila,self.posicion_anterior_columna,self.bando+self.pieza+str(self.posicion_anterior_fila)+str(self.posicion_anterior_columna))
                            print("Rey en jaque.")
                            enable_aux = False
                            return False
                        else:
                            enable_aux = False
                            print("Moviemiento valido.")
                            return True
                else:
                    return False
                

                print(gridd.get_Tablero(self.posicion_anterior_fila,self.posicion_anterior_columna))

            #diagonal abajo derecha.
            if (casilla_actual - (9*x)) == casilla_destino:
                enable = True
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
                    enable_aux = True
                    while enable_aux:
                        

                        print(gridd.printeo())
                        pieza_a_guardar = gridd.get_Tablero(self.posicion_destino_fila,self.posicion_destino_columna)
                        grig_general.gridd = gridd.set_Tablero(self.posicion_destino_fila,self.posicion_destino_columna,self.bando+self.pieza+str(self.posicion_destino_fila)+str(self.posicion_destino_columna))
                        grig_general.gridd = gridd.set_Tablero(self.posicion_anterior_fila,self.posicion_anterior_columna,0)
                        
                        rey.restricciones(rey.posicion_anterior_fila,rey.posicion_anterior_columna)
                        if rey.Index_jaque >= 1:
                            grig_general.gridd = gridd.set_Tablero(self.posicion_destino_fila,self.posicion_destino_columna,pieza_a_guardar)
                            grig_general.gridd = gridd.set_Tablero(self.posicion_anterior_fila,self.posicion_anterior_columna,self.bando+self.pieza+str(self.posicion_anterior_fila)+str(self.posicion_anterior_columna))
                            print("Rey en jaque.")
                            enable_aux = False
                            return False
                        else:
                            enable_aux = False
                            print("Moviemiento valido.")
                            return True
                else:
                    return False

            if (casilla_actual + (11*x)) == casilla_destino:
                enable = True
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
                    enable_aux = True
                    while enable_aux:
                        

                        print(gridd.printeo())
                        pieza_a_guardar = gridd.get_Tablero(self.posicion_destino_fila,self.posicion_destino_columna)
                        grig_general.gridd = gridd.set_Tablero(self.posicion_destino_fila,self.posicion_destino_columna,self.bando+self.pieza+str(self.posicion_destino_fila)+str(self.posicion_destino_columna))
                        grig_general.gridd = gridd.set_Tablero(self.posicion_anterior_fila,self.posicion_anterior_columna,0)
                        
                        rey.restricciones(rey.posicion_anterior_fila,rey.posicion_anterior_columna)
                        if rey.Index_jaque >= 1:
                            grig_general.gridd = gridd.set_Tablero(self.posicion_destino_fila,self.posicion_destino_columna,pieza_a_guardar)
                            grig_general.gridd = gridd.set_Tablero(self.posicion_anterior_fila,self.posicion_anterior_columna,self.bando+self.pieza+str(self.posicion_anterior_fila)+str(self.posicion_anterior_columna))
                            print("Rey en jaque.")
                            enable_aux = False
                            return False
                        else:
                            enable_aux = False
                            print("Moviemiento valido.")
                            return True
                else:
                    return False
            
            if (casilla_actual - (11*x)) == casilla_destino:
                enable = True
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
                    enable_aux = True
                    while enable_aux:
                        

                        print(gridd.printeo())
                        pieza_a_guardar = gridd.get_Tablero(self.posicion_destino_fila,self.posicion_destino_columna)
                        grig_general.gridd = gridd.set_Tablero(self.posicion_destino_fila,self.posicion_destino_columna,self.bando+self.pieza+str(self.posicion_destino_fila)+str(self.posicion_destino_columna))
                        grig_general.gridd = gridd.set_Tablero(self.posicion_anterior_fila,self.posicion_anterior_columna,0)
                        
                        rey.restricciones(rey.posicion_anterior_fila,rey.posicion_anterior_columna)
                        if rey.Index_jaque >= 1:
                            grig_general.gridd = gridd.set_Tablero(self.posicion_destino_fila,self.posicion_destino_columna,pieza_a_guardar)
                            grig_general.gridd = gridd.set_Tablero(self.posicion_anterior_fila,self.posicion_anterior_columna,self.bando+self.pieza+str(self.posicion_anterior_fila)+str(self.posicion_anterior_columna))
                            print("Rey en jaque.")
                            enable_aux = False
                            return False
                        else:
                            enable_aux = False
                            print("Moviemiento valido.")
                            return True
                else:
                    return False