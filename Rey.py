 
from Dama import Dama
 
import grig_general

gridd = grig_general.gridd

class Rey():
    Index_jaque = 0
    Direccion = []
    Casilla = {"Izquierda":[],"Derecha":[],"Arriba":[],"Abajo":[],"DigIzAb":[],"DigIzArr":[],"DigDrAb":[],"DigDrArr":[],"Caballo":[]}
        
    #esas posiciones deben de ser en enteros
    
    def __init__(self, bando,pieza,posicion_anterior_fila, posicion_anterior_columna, posicion_destino_fila, posicion_destino_columna):
        self.bando = bando #str
        self.pieza = pieza #str
        self.posicion_anterior_fila = posicion_anterior_fila #int
        self.posicion_anterior_columna = posicion_anterior_columna  #int
        self.posicion_destino_fila = posicion_destino_fila #int 
        self.posicion_destino_columna = posicion_destino_columna #int

    #movmiento a 8 posibilidades.
   
    def movimiento(self,fila,columna):
        enable = True

        if self.bando == "B":
            
                    
                casilla_actual = str(self.posicion_anterior_fila)+str(self.posicion_anterior_columna)
                casilla_destino = str(fila)+str(columna)
                if (abs(self.posicion_anterior_fila - fila) == 1 or abs(self.posicion_anterior_fila - fila) == 0 ) and (abs(self.posicion_anterior_columna-columna) == 1 or abs(self.posicion_anterior_columna-columna) == 0):

                    if gridd.get_Tablero(fila,columna) != 0:
                        Pieza_enemiga = gridd.get_Tablero(fila,columna)
                        
                        if Pieza_enemiga[0] == "B" or Pieza_enemiga[0] == "N":
                            enable = False
                            
                    
                    if gridd.get_Tablero(fila,columna) == 0   or enable: 
                        grig_general.gridd = gridd.set_Tablero(fila,columna,str(self.bando)+str(self.pieza)+str(fila)+str(columna))
                        grig_general.gridd = gridd.set_Tablero(self.posicion_anterior_fila,self.posicion_anterior_columna,0)
                        if self.restricciones(fila,columna):
                            print("movimiento invalido por jaque")
                            gridd.set_Tablero(self.posicion_anterior_fila,self.posicion_anterior_columna,self.bando+self.pieza+str(self.posicion_anterior_fila)+str(self.posicion_anterior_columna))
                            gridd.set_Tablero(fila,columna,0)

                            return False
                        print("movimiento valido")
                        return True
                    else:
                        print("Casilla ocupada o movimiento invalido.") 
                        return False
                else:
                    print("Casilla ocupada o movimiento invalido, segundo nivel.") 
                    return False

        elif self.bando == "N":
            casilla_actual = str(self.posicion_anterior_fila)+str(self.posicion_anterior_columna)
            casilla_destino = str(fila)+str(columna)
            if (abs(self.posicion_anterior_fila - fila) == 1 or abs(self.posicion_anterior_fila - fila) == 0 ) and (abs(self.posicion_anterior_columna-columna) == 1 or abs(self.posicion_anterior_columna-columna) == 0):

                if gridd.get_Tablero(fila,columna) != 0:
                    Pieza_enemiga = gridd.get_Tablero(fila,columna)
                    
                    if Pieza_enemiga[0] == "N" or Pieza_enemiga[0] == "B":
                        enable = False
                 
                
                if gridd.get_Tablero(fila,columna) == 0   or enable: 
                    grig_general.gridd = gridd.set_Tablero(fila,columna,str(self.bando)+str(self.pieza)+str(fila)+str(columna))
                    grig_general.gridd = gridd.set_Tablero(self.posicion_anterior_fila,self.posicion_anterior_columna,0)
                    if self.restricciones(fila,columna):
                        print("movimiento invalido por jaque")
                        gridd.set_Tablero(self.posicion_anterior_fila,self.posicion_anterior_columna,self.bando+self.pieza+str(self.posicion_anterior_fila)+str(self.posicion_anterior_columna))
                        gridd.set_Tablero(fila,columna,0)

                        return False

                    print("movimiento valido")
                    return True
                else:
                    print("Casilla ocupada.")  
                    return False
            else:
                print("Casilla ocupada o movimiento invalido, segundo nivel.") 
                return False

    #las restricciones de movimiento, con el rey enemigo.
    def restricciones(self,filas,columnas):
        #Verificacion del area interna del Rey.
        Reyy = str(filas)+str(columnas)
        fila = filas
        columna = columnas
        #Reinicio de variables
        Rey.Index_jaque = 0
        Rey.Casilla = {"Izquierda":[],"Derecha":[],"Arriba":[],"Abajo":[],"DigIzAb":[],"DigIzArr":[],"DigDrAb":[],"DigDrArr":[],"Caballo":[]}
        Rey.Direccion = []

        casilla_a_comparar = int(str(filas) + str(columnas))
        
        enable = False

        if gridd.get_Tablero(filas,columnas) != 0:
            peon_blanco = gridd.get_Tablero(filas,columnas)
            if peon_blanco[0] == "B" and peon_blanco[1] == "P":
                enable = True
                    

        for x in range(fila-1,fila+2):
            for y in range(columna-1,columna+2):
                if x >= 0 and x <= 7:
                    if y >= 0 and y <= 7:
                        combinacion = int(str(x)+str(y))
                        if casilla_a_comparar != combinacion:
                            #Esta parte imprime todos los movimientos validos y no analiza la casilla ocupada por el rey
                            #Region Verificador de jaque de peones para rey negro y blanco.
                            if self.bando == "N": #Si el rey es negro.
                                if x < fila and y != columna:

                                    if gridd.get_Tablero(x,y) != 0 :

                                        peon_blanco = gridd.get_Tablero(x,y)
                                        if peon_blanco[0] == "B" and peon_blanco[1] == "P":
                                            print(x,y,"Jaque de Peon.") 
                                            Rey.Index_jaque += 1

                            if self.bando == "B":
                                if x > fila and y != columna:
                                     if gridd.get_Tablero(x,y) != 0 :

                                        peon_blanco = gridd.get_Tablero(x,y)
                                        if peon_blanco[0] == "N" and peon_blanco[1] == "P":
                                            print(x,y,"Jaque de Peon.") 
                                            Rey.Index_jaque += 1
                                            
                            #EndRegion 

                            
                            #Region Jaque para las torres.

                            #Fila
                            if x == fila and y != columna:

                                if self.bando == "N":

                                    if gridd.get_Tablero(x,y) != 0 :

                                        Torre = gridd.get_Tablero(x,y)
                                        if Torre[0] == "B" and Torre[1] == "T":
                                            print(x,y,"Jaque de Torre") 
                                            Rey.Index_jaque += 1
                                        

                                elif self.bando == "B":

                                    if gridd.get_Tablero(x,y) != 0 :

                                        Torre = gridd.get_Tablero(x,y)
                                        if Torre[0] == "N" and Torre[1] == "T":
                                            print(x,y,"Jaque de Torre") 
                                            Rey.Index_jaque += 1
                            #EndRegion
                             
                            #Region 
                            #Columna

                            if x != fila and y == columna :
                                if self.bando == "N":
                                    if gridd.get_Tablero(x,y) != 0 :

                                        Torre = gridd.get_Tablero(x,y)
                                        if Torre[0] == "B" and Torre[1] == "T":
                                            print(x,y,"Jaque de Torre.") 
                                            Rey.Index_jaque += 1

                                elif self.bando == "B":
                                    if gridd.get_Tablero(x,y) != 0 :

                                        Torre = gridd.get_Tablero(x,y)
                                        if Torre[0] == "N" and Torre[1] == "T":
                                            print(x,y,"Jaque de Torre.") 
                                            Rey.Index_jaque += 1
                            #EndRegion

                            #EndRegion Para torres.

                            #Region Para Rey enemigo.
                            if gridd.get_Tablero(x,y) != 0 :
                                if self.bando == "N":
                                    Reyy = gridd.get_Tablero(x,y)
                                    if Reyy[0] == "B" and Reyy[1] == "R":
                                        print("Movimiento invalido.")
                                        Rey.Index_jaque += 1
                                elif self.bando == "B":
                                    Reyy = gridd.get_Tablero(x,y)
                                    if Reyy[0] == "N" and Reyy[1] == "R":
                                        print("Movimiento invalido.")
                                        Rey.Index_jaque += 1
                            #EndRegion para Rey enemigo.


                            #Fuera del circulo interno.
                else:
                    print(x,y,"Numero no permitido")
                    pass

        #Busqueda de alfil.

        #Busqueda de alfil bajo hacia la derecha

        enable = True
        fila_aux = filas 
        colum_aux = columnas
        while enable:
            

            fila_aux -= 1
            colum_aux += 1
            if self.bando == "B":
                if fila_aux >= 0 and colum_aux >= 0 and fila <= 7 and colum_aux <= 7:
                    if gridd.get_Tablero(fila_aux,colum_aux) != 0:
                        casilla = gridd.get_Tablero(fila_aux,colum_aux)
                        if casilla[0] == "N" and casilla[1] == "A":
                            print("Jaque por Alfil bajo hacia la derecha.")
                            enable = False
                            Rey.Index_jaque += 1
                            Rey.Direccion.append("DigIzArr")
                            Rey.Casilla["DigIzArr"].append(casilla)
                        if casilla[0] == "N" and casilla[1] == "D":
                            print("Jaque por Dama bajo hacia la derecha.")
                            enable = False
                            Rey.Index_jaque += 1
                            Rey.Direccion.append("DigIzArr")
                            Rey.Casilla["DigIzArr"].append(casilla)
                        if (casilla[0] == "B" and casilla[1] != "R") or  casilla[0] == "N":
                            enable = False
                           
                else:
                    print("Casilla fuera del Tablero.")
                    enable =False
            elif self.bando == "N" and enable:
                if fila_aux >= 0 and colum_aux >= 0 and fila <= 7 and colum_aux <= 7:
                    if gridd.get_Tablero(fila_aux,colum_aux) != 0:
                        casilla = gridd.get_Tablero(fila_aux,colum_aux)
                        if casilla[0] == "B" and casilla[1] == "A":
                            print("Jaque por Alfil.")
                            
                            enable = False
                            Rey.Index_jaque += 1
                            Rey.Direccion.append("DigIzArr")
                            Rey.Casilla["DigIzArr"].append(casilla)
                        if casilla[0] == "B" and casilla[1] == "D":
                            print("Jaque por Dama.")
                            enable = False
                            Rey.Index_jaque += 1
                            Rey.Direccion.append("DigIzArr")
                            Rey.Casilla["DigIzArr"].append(casilla)
                        if (casilla[0] == "N" and casilla[1] != "R") or casilla[0] == "B":
                            enable = False
                            
                else:
                    print("Casilla fuera del Tablero.")
                    enable =False

        #Diagonal abajo izquierda.
        enable = True
        fila_aux = filas 
        colum_aux = columnas
        while enable:
            
            fila_aux -= 1
            colum_aux -= 1
            if self.bando == "B":
                if fila_aux >= 0 and colum_aux >= 0 and fila_aux <= 7 and colum_aux <= 7:
                    if gridd.get_Tablero(fila_aux,colum_aux) != 0:
                        casilla = gridd.get_Tablero(fila_aux,colum_aux)
                        if casilla[0] == "N" and casilla[1] == "A":
                            print("Jaque por Alfil abajo izquierda.")
                            enable = False
                            Rey.Index_jaque += 1
                            Rey.Direccion.append("DigDrArr")
                            Rey.Casilla["DigDrArr"].append(casilla)
                        if casilla[0] == "N" and casilla[1] == "D":
                            print("Jaque por Dama abajo izquierda.")
                            enable = False
                            Rey.Index_jaque += 1
                            Rey.Direccion.append("DigDrArr")
                            Rey.Casilla["DigDrArr"].append(casilla)
                        if (casilla[0] == "B" and casilla[1] != "R") or casilla[0] == "N":
                            enable = False
                            
                else:
                    print("Casilla fuera del Tablero.")
                    enable = False

            elif self.bando == "N" and enable:
                if fila_aux >= 0 and colum_aux >= 0 and fila_aux <= 7 and colum_aux <= 7:
                    if gridd.get_Tablero(fila_aux,colum_aux) != 0:
                        casilla = gridd.get_Tablero(fila_aux,colum_aux)
                        if casilla[0] == "B" and casilla[1] == "A":
                            print("Jaque por Alfil.") 
                            enable = False
                            Rey.Index_jaque += 1
                            Rey.Direccion.append("DigDrArr")
                            Rey.Casilla["DigDrArr"].append(casilla)
                        if casilla[0] == "B" and casilla[1] == "D":
                            print("Jaque por Dama.")
                            enable = False
                            Rey.Index_jaque += 1
                            Rey.Direccion.append("DigDrArr")
                            Rey.Casilla["DigDrArr"].append(casilla)
                        if (casilla[0] == "N" and casilla[1] != "R") or casilla[0] == "B":
                            enable = False
                            
                else:
                    print("Casilla fuera del Tablero.")
                    enable = False
        
        #Diagonal subiendo izquierda.
        enable = True
        fila_aux = filas 
        colum_aux = columnas
        while enable:
            fila_aux += 1
            colum_aux -= 1
            if self.bando == "B": 
                if fila_aux >= 0 and colum_aux >= 0 and fila_aux <= 7 and colum_aux <= 7:
                    if gridd.get_Tablero(fila_aux,colum_aux) != 0:
                        casilla = gridd.get_Tablero(fila_aux,colum_aux)
                        if casilla[0] == "N" and casilla[1] == "A":
                            print("Jaque por Alfil.") 
                            enable = False
                            Rey.Index_jaque += 1
                            Rey.Direccion.append("DigDrAb")
                            Rey.Casilla["DigDrAb"].append(casilla)
                        if casilla[0] == "N" and casilla[1] == "D":
                            print("Jaque por Dama.")
                            enable = False
                            Rey.Index_jaque += 1
                            Rey.Direccion.append("DigDrAb")
                            Rey.Casilla["DigDrAb"].append(casilla)
                        if (casilla[0] == "B" and casilla[1] != "R")  or casilla[0] == "N":
                            enable = False
                            
                else:
                    print("Casilla fuera del Tablero.")
                    enable = False

            elif self.bando == "N" and enable:
                if fila_aux >= 0 and colum_aux >= 0 and fila_aux <= 7 and colum_aux <= 7:
                    if gridd.get_Tablero(fila_aux,colum_aux) != 0:
                        casilla = gridd.get_Tablero(fila_aux,colum_aux)
                        if casilla[0] == "B" and casilla[1] == "A":
                            print("Jaque por Alfil.") 
                            enable = False
                            Rey.Index_jaque += 1
                            Rey.Direccion.append("DigDrAb")
                            Rey.Casilla["DigDrAb"].append(casilla)
                        if casilla[0] == "B" and casilla[1] == "D":
                            print("Jaque por Dama.")
                            enable = False
                            Rey.Index_jaque += 1
                            Rey.Direccion.append("DigDrAb")
                            Rey.Casilla["DigDrAb"].append(casilla)
                        if (casilla[0] == "N" and casilla[1] != "R") or casilla[0] == "B":
                            enable = False
                             
                else:
                    print("Casilla fuera del Tablero.")
                    enable = False

        #Diagonal subiendo derecha.
        fila_aux = filas 
        colum_aux =  columnas
        enable = True
        while enable:
            fila_aux += 1
            colum_aux += 1
            if self.bando == "B":
                if fila_aux >= 0 and colum_aux >= 0 and fila_aux <= 7 and colum_aux <= 7:
                    if gridd.get_Tablero(fila_aux,colum_aux) != 0:
                        casilla = gridd.get_Tablero(fila_aux,colum_aux)
                        if casilla[0] == "N" and casilla[1] == "A":
                            print("Jaque por Alfil.")                            
                            enable = False
                            Rey.Index_jaque += 1
                            Rey.Direccion.append("DigIzAb")
                            Rey.Casilla["DigIzAb"].append(casilla)
                        if casilla[0] == "N" and casilla[1] == "D":
                            print("Jaque por Dama.")
                            enable = False
                            Rey.Index_jaque += 1
                            Rey.Direccion.append("DigIzAb")
                            Rey.Casilla["DigIzAb"].append(casilla)
                        if (casilla[0] == "B" and casilla[1] != "R") or casilla[0] == "N":
                            enable = False
                             
                else:
                    print("Casilla fuera del Tablero.")
                    enable = False
            elif self.bando == "N" and enable:
                if fila_aux >= 0 and colum_aux >= 0 and fila_aux <= 7 and colum_aux <= 7:
                    if gridd.get_Tablero(fila_aux,colum_aux) != 0:
                        casilla = gridd.get_Tablero(fila_aux,colum_aux)
                        if casilla[0] == "B" and casilla[1] == "A":
                            print("Jaque por Alfil.")
                            enable = False
                            Rey.Index_jaque += 1
                            Rey.Direccion.append("DigIzAb")
                            Rey.Casilla["DigIzAb"].append(casilla)
                        if casilla[0] == "B" and casilla[1] == "D":
                            print("Jaque por Dama.")
                            enable = False
                            Rey.Index_jaque += 1
                            Rey.Direccion.append("DigIzAb")
                            Rey.Casilla["DigIzAb"].append(casilla)
                        if (casilla[0] == "N" and casilla[1] != "R") or casilla[0] == "B":
                            enable = False
                             
                else:
                    print("Casilla fuera del Tablero.")
                    enable = False
        #EndRegion de Alfil.

        #Region para la Torre y Dama.
        #Derecha.
        enable = True
        fila_aux = filas
        colum_aux = columnas
        while enable:
            
            colum_aux += 1
            if self.bando == "B":
                if fila_aux >= 0 and colum_aux >= 0 and fila_aux <= 7 and colum_aux <= 7:
                    if gridd.get_Tablero(fila_aux,colum_aux) != 0:
                        casilla = gridd.get_Tablero(fila_aux,colum_aux)
                        if casilla[0] == "N" and casilla[1] == "T":
                            print("Jaque por Torre.")
                            enable = False
                            Rey.Index_jaque += 1
                            Rey.Direccion.append("Izquierda")
                            Rey.Casilla["Izquierda"].append(casilla)
                        if casilla[0] == "N" and casilla[1] == "D":
                            print("Jaque por Dama.")
                            enable = False
                            Rey.Index_jaque += 1
                            Rey.Direccion.append("Izquierda")
                            Rey.Casilla["Izquierda"].append(casilla)
                        if (casilla[0] == "B" and not casilla[1] == "R") or casilla[0] == "N":
                            
                            enable = False
                            
                            
                else:
                    print("Casilla fuera del Tablero.")
                    enable = False
                    
            elif self.bando == "N" and enable:
                if fila_aux >= 0 and colum_aux >= 0 and fila_aux <= 7 and colum_aux <= 7:
                    if gridd.get_Tablero(fila_aux,colum_aux) != 0:
                        casilla = gridd.get_Tablero(fila_aux,colum_aux)
                        if casilla[0] == "B" and casilla[1] == "T":
                            print("Jaque por Torre.")
                            enable = False
                            Rey.Index_jaque += 1
                            Rey.Direccion.append("Izquierda")
                            Rey.Casilla["Izquierda"].append(casilla)
                        if casilla[0] == "B" and casilla[1] == "D":
                            print("Jaque por Dama.")
                            enable = False
                            Rey.Index_jaque += 1
                            Rey.Direccion.append("Izquierda")
                            Rey.Casilla["Izquierda"].append(casilla)
                        if (casilla[0] == "N" and casilla[1] != "R") or casilla[0] == "B":
                            enable = False
                             
                else:
                    print("Casilla fuera del Tablero.")
                    enable = False

        #Izquierda.
        enable = True
        fila_aux =filas 
        colum_aux = columnas
        while enable:
            
            colum_aux -= 1
            if self.bando == "B":
                if fila_aux >= 0 and colum_aux >= 0 and fila_aux <= 7 and colum_aux <= 7:
                    if gridd.get_Tablero(fila_aux,colum_aux) != 0:
                        casilla = gridd.get_Tablero(fila_aux,colum_aux)
                        if casilla[0] == "N" and casilla[1] == "T":
                            print("Jaque por Torre.")
                            enable = False
                            Rey.Index_jaque += 1
                            Rey.Direccion.append("Derecha")
                            Rey.Casilla["Derecha"].append(casilla)
                        if casilla[0] == "N" and casilla[1] == "D":
                            print("Jaque por Dama.")
                            enable = False
                            Rey.Index_jaque += 1
                            Rey.Direccion.append("Derecha")
                            Rey.Casilla["Derecha"].append(casilla)
                        if (casilla[0] == "B" and not casilla[1] == "R") or casilla[0] == "N":
                            enable = False
                             
                else:
                    print("Casilla fuera del Tablero.")
                    enable = False

            elif self.bando == "N" and enable:
                if fila_aux >= 0 and colum_aux >= 0 and fila_aux <= 7 and colum_aux <= 7:
                    if gridd.get_Tablero(fila_aux,colum_aux) != 0:
                        casilla = gridd.get_Tablero(fila_aux,colum_aux)
                        if casilla[0] == "B" and casilla[1] == "T":
                            print("Jaque por Torre.")
                            enable = False
                            Rey.Index_jaque += 1
                            Rey.Direccion.append("Derecha")
                            Rey.Casilla["Derecha"].append(casilla)
                        if casilla[0] == "B" and casilla[1] == "D":
                            print("Jaque por Dama.")
                            enable = False 
                            Rey.Index_jaque += 1
                            Rey.Direccion.append("Derecha")
                            Rey.Casilla["Derecha"].append(casilla)
                        if (casilla[0] == "N" and casilla[1] != "R") or casilla[0] == "B":
                            enable = False
                             
                else:
                    print("Casilla fuera del Tablero.")
                    enable = False
        
        #Abajo.
        enable = True
        fila_aux =filas
        colum_aux = columnas
        while enable:
            
            fila_aux -= 1
            if self.bando == "B":
                if fila_aux >= 0 and colum_aux >= 0 and fila_aux <= 7 and colum_aux <= 7:
                    if gridd.get_Tablero(fila_aux,colum_aux) != 0:
                        casilla = gridd.get_Tablero(fila_aux,colum_aux)
                        if casilla[0] == "N" and casilla[1] == "T":
                            print("Jaque por Torre.")
                            enable = False 
                            Rey.Index_jaque += 1
                            Rey.Direccion.append("Arriba")
                            Rey.Casilla["Arriba"].append(casilla)
                        if casilla[0] == "N" and casilla[1] == "D":
                            print("Jaque por Dama.")
                            enable = False
                            Rey.Index_jaque += 1
                            Rey.Direccion.append("Arriba")
                            Rey.Casilla["Arriba"].append(casilla)

                        if (casilla[0] == "B" and casilla[1] != "R") or casilla[0] == "N":
                            enable = False
                             
                else:
                    print("Casilla fuera del Tablero.")
                    enable = False

            elif self.bando == "N" and enable:
                if fila_aux >= 0 and colum_aux >= 0 and fila_aux <= 7 and colum_aux <= 7:
                    if gridd.get_Tablero(fila_aux,colum_aux) != 0:
                        casilla = gridd.get_Tablero(fila_aux,colum_aux)
                        if casilla[0] == "B" and casilla[1] == "T":
                            print("Jaque por Torre.")
                            enable = False   
                            Rey.Index_jaque += 1                         
                            Rey.Direccion.append("Arriba")
                            Rey.Casilla["Arriba"].append(casilla)
                        if casilla[0] == "B" and casilla[1] == "D":
                            print("Jaque por Dama.")
                            enable = False
                            Rey.Index_jaque += 1
                            Rey.Direccion.append("Arriba")
                            Rey.Casilla["Arriba"].append(casilla)
                        if (casilla[0] == "N" and casilla[1] != "R") or casilla[0] == "B":
                            enable = False
                             
                else:
                    print("Casilla fuera del Tablero.")
                    enable = False

        #Arriba.
        enable = True
        fila_aux =filas 
        colum_aux = columnas
        while enable:
            
            fila_aux += 1
            if self.bando == "B":
                if fila_aux >= 0 and colum_aux >= 0 and fila_aux <= 7 and colum_aux <= 7:
                    if gridd.get_Tablero(fila_aux,colum_aux) != 0:
                        casilla = gridd.get_Tablero(fila_aux,colum_aux)
                        if casilla[0] == "N" and casilla[1] == "T":
                            print("Jaque por Torre.")
                            enable = False
                            Rey.Index_jaque += 1                            
                            Rey.Direccion.append("Abajo")
                            Rey.Casilla["Abajo"].append(casilla)
                        if casilla[0] == "N" and casilla[1] == "D":
                            print("Jaque por Dama.")
                            enable = False    
                            Rey.Index_jaque += 1                         
                            Rey.Direccion.append("Abajo")
                            Rey.Casilla["Abajo"].append(casilla)
                        if (casilla[0] == "B" and casilla[1] != "R") or casilla[0] == "N":
                            enable = False
                            
                else:
                    print("Casilla fuera del Tablero.")
                    enable = False

            elif self.bando == "N" and enable:
                if fila_aux >= 0 and colum_aux >= 0 and fila_aux <= 7 and colum_aux <= 7:
                    if gridd.get_Tablero(fila_aux,colum_aux) != 0:
                        casilla = gridd.get_Tablero(fila_aux,colum_aux)
                        if casilla[0] == "B" and casilla[1] == "T":
                            print("Jaque por Torre.")
                            enable = False 
                            Rey.Index_jaque += 1                           
                            Rey.Direccion.append("Abajo")
                            Rey.Casilla["Arriba"].append(casilla)
                        if casilla[0] == "B" and casilla[1] == "D":
                            print("Jaque por Dama.")
                            enable = False 
                            Rey.Index_jaque += 1
                            Rey.Direccion.append("Abajo")
                            Rey.Casilla["Arriba"].append(casilla)
                        if(casilla[0] == "N" and casilla[1] != "R") or casilla[0] == "B":
                            print("Casilla amiga")
                            enable = False
                             
                else:
                    print("Casilla fuera del Tablero.")
                    enable = False

        #EndRegion Torre y Dama.

        #Region Caballo.

        casilla_actual = int(str(filas)+str(columnas))
        lista_index = [21,19,12,8]
        fila_aux =  filas 
        colum_aux = columnas

        if self.bando == "B":
            for i in range(0, len(lista_index)):
                operacion = casilla_actual + lista_index[i]
                operacion_c = -1
                operacion_f = -1
                if operacion < 10 and operacion >= 0 :

                    operacion = str(0)+str(operacion)
                    operacion_f = int(operacion[0])
                    operacion_c = int(operacion[1])
                elif operacion >= 0:
                    operacion = str(operacion)
                    operacion_f = int(operacion[0])
                    operacion_c = int(operacion[1])

                
                if operacion_f <= 7 and operacion_f >=0 and operacion_c <= 7 and operacion_c >= 0:
                    if gridd.get_Tablero(operacion_f,operacion_c) != 0:
                        casilla_analizar = gridd.get_Tablero(operacion_f,operacion_c)
                        if casilla_analizar[0] == "N" and casilla_analizar[1] == "C":
                            print("Jaque con caballo.")
                            Rey.Index_jaque += 1                                                     
                            Rey.Direccion.append("Caballo")
                            Rey.Casilla["Caballo"].append(casilla_analizar)


            for i in range(0, len(lista_index)):
                operacion = casilla_actual - lista_index[i]
                operacion_c = -1
                operacion_f = -1
                if operacion < 10 and operacion >= 0 :

                    operacion = str(0)+str(operacion)
                    operacion_f = int(operacion[0])
                    operacion_c = int(operacion[1])
                elif operacion >= 0:
                    operacion = str(operacion)
                    operacion_f = int(operacion[0])
                    operacion_c = int(operacion[1])

                if operacion_f <= 7 and operacion_f >=0 and operacion_c <= 7 and operacion_c >= 0:
                    if gridd.get_Tablero(operacion_f,operacion_c) != 0:
                        casilla_analizar = gridd.get_Tablero(operacion_f,operacion_c)
                        if casilla_analizar[0] == "N" and casilla_analizar[1] == "C":
                            print("Jaque con caballo.")
                            Rey.Index_jaque += 1
                            Rey.Direccion.append("Caballo")
                            Rey.Casilla["Caballo"].append(casilla_analizar)

        elif self.bando == "N":
            for i in range(0, len(lista_index)):
                operacion = casilla_actual + lista_index[i]
                operacion_c = -1
                operacion_f = -1
                if operacion < 10 and operacion >= 0 :

                    operacion = str(0)+str(operacion)
                    operacion_f = int(operacion[0])
                    operacion_c = int(operacion[1])
                elif operacion >= 0:
                    operacion = str(operacion)
                    operacion_f = int(operacion[0])
                    operacion_c = int(operacion[1])
                
                if operacion_f <= 7 and operacion_f >=0 and operacion_c <= 7 and operacion_c >= 0:
                    if gridd.get_Tablero(operacion_f,operacion_c) != 0:
                        casilla_analizar = gridd.get_Tablero(operacion_f,operacion_c)
                        if casilla_analizar[0] == "B" and casilla_analizar[1] == "C":
                            print("Jaque con caballo.")
                            Rey.Index_jaque += 1
                            Rey.Direccion.append("Caballo")
                            Rey.Casilla["Caballo"].append(casilla_analizar)

            for i in range(0, len(lista_index)):
                operacion = casilla_actual - lista_index[i]
                operacion_c = -1
                operacion_f = -1
                if operacion < 10 and operacion >= 0 :

                    operacion = str(0)+str(operacion)
                    operacion_f = int(operacion[0])
                    operacion_c = int(operacion[1])
                elif operacion >= 0:
                    operacion = str(operacion)
                    operacion_f = int(operacion[0])
                    operacion_c = int(operacion[1])
                
                if operacion_f <= 7 and operacion_f >=0 and operacion_c <= 7 and operacion_c >= 0:
                    if gridd.get_Tablero(operacion_f,operacion_c) != 0:
                        casilla_analizar = gridd.get_Tablero(operacion_f,operacion_c)
                        if casilla_analizar[0] == "B" and casilla_analizar[1] == "C":
                            print("Jaque con caballo.")
                            Rey.Index_jaque += 1
                            Rey.Direccion.append("Caballo")
                            Rey.Casilla["Caballo"].append(casilla_analizar) 

        #EndRegion Caballo.
        if Rey.Index_jaque >= 1:
            return True
        return False

    def checkPawns(self,d,fila_peon,columan_peon,enable_2,final):
        
        if d-10 >= 0:

            fila_peon = str(d-10)

            if int(fila_peon) < 10 and int(fila_peon) >= 0:
                fila_peon = str(0) + str(fila_peon)                            
                columan_peon = int(fila_peon[1])
                fila_peon = int(fila_peon[0])

            if int(fila_peon) > 9:
                fila_peon = str(fila_peon)                            
                columan_peon = int(fila_peon[1])
                fila_peon = int(fila_peon[0])

            if self.bando == "B":

                if fila_peon >= 0 and fila_peon <=7 and columan_peon >= 0  and columan_peon <= 7:
                    if gridd.get_Tablero(fila_peon,columan_peon) != 0:                                 
                        peon = gridd.get_Tablero(fila_peon,columan_peon)
                        if  peon[0] == "B" and peon[1] == "P":
                            print("No hay jaque")
                            enable_2 = False
                            final = False

        fila_peon = str(d+10)
        columan_peon = int(fila_peon[1])
        fila_peon = int(fila_peon[0])
        if self.bando == "N":

            if fila_peon >= 0 and fila_peon <=7 and columan_peon >= 0  and columan_peon <= 7:
                if gridd.get_Tablero(fila_peon,columan_peon) != 0:
                    peon  = gridd.get_Tablero(fila_peon,columan_peon)                                    
                    if  peon[0] == "N" and peon[1] == "P":
                        print("No hay jaque")
                        enable_2 = False
                        final = False

        if d-20 >= 0:
            fila_peon = str(d-20)

            if int(fila_peon) < 10 and int(fila_peon) >= 0:
                fila_peon = str(0) + str(fila_peon)                            
                columan_peon = int(fila_peon[1])
                fila_peon = int(fila_peon[0])

            if int(fila_peon) > 9:
                fila_peon = str(fila_peon)                            
                columan_peon = int(fila_peon[1])
                fila_peon = int(fila_peon[0])

            if self.bando == "B":

                if fila_peon >= 0 and fila_peon <=7 and columan_peon >= 0  and columan_peon <= 7:
                    
                    if fila_peon == 2:
                        if gridd.get_Tablero(fila_peon,columan_peon) != 0:                                 
                            peon = gridd.get_Tablero(fila_peon,columan_peon)
                            
                            if  peon[0] == "B" and peon[1] == "P":
                                print("No hay jaque")
                                enable_2 = False
                                final = False


        fila_peon = str(d+20)
        columan_peon = int(fila_peon[1])
        fila_peon = int(fila_peon[0])

        if self.bando == "N":

            if fila_peon >= 0 and fila_peon <=7 and columan_peon >= 0  and columan_peon <= 7:
                
                if fila_peon == 6:
                    if gridd.get_Tablero(fila_peon,columan_peon) != 0:                                 
                        peon = gridd.get_Tablero(fila_peon,columan_peon)
                        
                        if  peon[0] == "N" and peon[1] == "P":
                            print("No hay jaque")
                            enable_2 = False
                            final = False


        if enable_2 == False and final == False:
            return False
        else:
            return True
    
    def CheckDirrections(self,enable_2,final,fila_aux,columna_aux):
         
        if self.bando == "B":
            if fila_aux <= 7 and fila_aux >=0 and columna_aux <= 7 and columna_aux >= 0:
                if gridd.get_Tablero(fila_aux,columna_aux) != 0:
                    pieza_aliada = gridd.get_Tablero(fila_aux,columna_aux)

                    if pieza_aliada[0] == "B" and pieza_aliada == "T":
                        enable_2 = False
                        print("No hay jaque mate.")
                        final = False
                    elif pieza_aliada[0] == "B" and pieza_aliada == "D":
                        enable_2 = False
                        print("No hay jaque mate.")
                        final = False
                    elif pieza_aliada[0] == "N" or pieza_aliada[0] == "B":
                        enable_2 = False
                else:
                    enable_2 = False
                        
                        
            else:
                enable_2 = False
                
        elif self.bando == "N":
            
            if fila_aux <= 7 and fila_aux >=0 and columna_aux <= 7 and columna_aux >= 0:
                if gridd.get_Tablero(fila_aux,columna_aux) != 0:
                    pieza_aliada = gridd.get_Tablero(fila_aux,columna_aux)

                    if pieza_aliada[0] == "N" and pieza_aliada == "T":
                        enable_2 = False
                        print("No hay jaque mate.")
                        final = False
                    elif pieza_aliada[0] == "N" and pieza_aliada == "D":
                        enable_2 = False
                        print("No hay jaque mate.")
                        final = False
                    elif pieza_aliada[0] == "N" or pieza_aliada[0] == "B":
                        enable_2 = False

                else:
                    enable_2 = False 
            else:
                enable_2 = False
        if final == False:
            return False
        if enable_2 == False:
            return True
                                    
    def CheckTheHourse(self,lista_index,d,final):
     
        if self.bando == "B":
            for t in range(0, len(lista_index)):
                operacion = d + lista_index[t]
                operacion_c = -1
                operacion_f = -1
                if operacion < 10 and operacion >= 0 :

                    operacion = str(0)+str(operacion)
                    operacion_f = int(operacion[0]) 
                    operacion_c = int(operacion[1])
                elif operacion >= 0:
                    operacion = str(operacion)
                    operacion_f = int(operacion[0]) 
                    operacion_c = int(operacion[1])

                
                if operacion_f <= 7 and operacion_f >=0 and operacion_c <= 7 and operacion_c >= 0:
                    if gridd.get_Tablero(operacion_f,operacion_c) != 0:
                        casilla_analizar = gridd.get_Tablero(operacion_f,operacion_c)
                        if casilla_analizar[0] == "B" and casilla_analizar[1] == "C":
                            print("No hay jaque.")
                            final = False

            for t in range(0, len(lista_index)):
                operacion = d - lista_index[t]
                operacion_c = -1
                operacion_f = -1
                if operacion < 10 and operacion >= 0 :

                    operacion = str(0)+str(operacion)
                    operacion_f = int(operacion[0])
                    operacion_c = int(operacion[1])
                elif operacion >= 0:
                    operacion = str(operacion)
                    operacion_f = int(operacion[0]) 
                    operacion_c = int(operacion[1])

                if operacion_f <= 7 and operacion_f >=0 and operacion_c <= 7 and operacion_c >= 0:
                    if gridd.get_Tablero(operacion_f,operacion_c) != 0:
                        casilla_analizar = gridd.get_Tablero(operacion_f,operacion_c)
                        if casilla_analizar[0] == "B" and casilla_analizar[1] == "C":
                            print("No hay jaque.")
                            final = False

        elif self.bando == "N":
            for t in range(0, len(lista_index)):
                operacion = d + lista_index[t]
                operacion_c = -1
                operacion_f = -1
                if operacion < 10 and operacion >= 0 :

                    operacion = str(0)+str(operacion)
                    operacion_f = int(operacion[0]) 
                    operacion_c = int(operacion[1])
                elif operacion >= 0:
                    operacion = str(operacion)
                    operacion_f = int(operacion[0]) 
                    operacion_c = int(operacion[1])
                
                if operacion_f <= 7 and operacion_f >=0 and operacion_c <= 7 and operacion_c >= 0:
                    if gridd.get_Tablero(operacion_f,operacion_c) != 0:
                        casilla_analizar = gridd.get_Tablero(operacion_f,operacion_c)
                        if casilla_analizar[0] == "N" and casilla_analizar[1] == "C":
                            print("No hay jaque.")
                            final = False
                        
            
            for t in range(0, len(lista_index)):
                operacion = d - lista_index[t]
                operacion_c = -1
                operacion_f = -1
                if operacion < 10 and operacion >= 0 :

                    operacion = str(0)+str(operacion)
                    operacion_f = int(operacion[0]) 
                    operacion_c = int(operacion[1])
                elif operacion >= 0:
                    operacion = str(operacion)
                    operacion_f = int(operacion[0]) 
                    operacion_c = int(operacion[1])
                
                if operacion_f <= 7 and operacion_f >=0 and operacion_c <= 7 and operacion_c >= 0:
                    if gridd.get_Tablero(operacion_f,operacion_c) != 0:
                        casilla_analizar = gridd.get_Tablero(operacion_f,operacion_c)
                        if casilla_analizar[0] == "N" and casilla_analizar[1] == "C":
                            print("No hay jaque.")
                            final = False
        
        if final == False:
            return True

    def Checkdiagonals(self,fila_aux,columna_aux,enable_2,final):

        if self.bando == "B":
            if fila_aux >= 0 and columna_aux >= 0 and fila_aux <= 7 and columna_aux <= 7:
                if gridd.get_Tablero(fila_aux,columna_aux) != 0:
                    casilla = gridd.get_Tablero(fila_aux,columna_aux)
                    if casilla[0] == "B" and casilla[1] == "A":
                        print("No hay jaque.")
                        enable_2 = False
                        final = False
                    if casilla[0] == "B" and casilla[1] == "D":
                        print("No hay jaque.")
                        enable_2 = False
                        final = False
                    if casilla[0] == "B" or casilla[0] == "N":
                        enable_2 = False
                else:
                    enable_2 = False
            else:
                enable_2 = False
        
        elif self.bando == "N":
            if fila_aux >= 0 and columna_aux >= 0 and fila_aux <= 7 and columna_aux <= 7:
                if gridd.get_Tablero(fila_aux,columna_aux) != 0:
                    casilla = gridd.get_Tablero(fila_aux,columna_aux)
                    if casilla[0] == "N" and casilla[1] == "A":
                        print("No hay jaque.")
                        enable_2 = False
                        final = False
                    if casilla[0] == "N" and casilla[1] == "D":
                        print("No hay jaque.")
                        enable_2 = False
                        final = False
                    if casilla[0] == "B" or casilla[0] == "N":
                        enable_2 = False
                else:
                    enable_2 = False
            else:
                enable_2 = False

        if enable_2 == False:
            return True
        if final == False:
            return False

    def izquierda(self,cuenta,casilla_actual,casilla_destino,enable_2,final):
        cuenta_permitida = 0
        aux = str(casilla_actual)
        pieza_enemiga = gridd.get_Tablero(int(aux[0]),int(aux[1]))
        for d in range(int(casilla_actual),casilla_destino,cuenta):
            #comprobacion en la pieza enemiga si hay piezas que la pueden atacar.

            
            if cuenta_permitida >= 1:
                #esta seccion es cuando esta en el recorrido de esta.
                #rey blanco
                #peon abajo

                if d-10 >= 0:
                    fila_peon = str(d-10)

                    if int(fila_peon) < 10 and int(fila_peon) >= 0:
                        fila_peon = str(0) + str(fila_peon)                            
                        columan_peon = int(fila_peon[1])
                        fila_peon = int(fila_peon[0])

                    if int(fila_peon) > 9:
                        fila_peon = str(fila_peon)                            
                        columan_peon = int(fila_peon[1])
                        fila_peon = int(fila_peon[0])

                    if self.bando == "B":

                        if fila_peon >= 0 and fila_peon <=7 and columan_peon >= 0  and columan_peon <= 7:
                            if gridd.get_Tablero(fila_peon,columan_peon) != 0:                                 
                                peon = gridd.get_Tablero(fila_peon,columan_peon)
                                if  peon[0] == "B" and peon[1] == "P":
                                    print("No hay jaque")
                                    enable_2 = False
                                    final = False

                fila_peon = str(d+10)
                columan_peon = int(fila_peon[1])
                fila_peon = int(fila_peon[0])
                if self.bando == "N":

                    if fila_peon >= 0 and fila_peon <=7 and columan_peon >= 0  and columan_peon <= 7:
                        if gridd.get_Tablero(fila_peon,columan_peon) != 0:
                            peon  = gridd.get_Tablero(fila_peon,columan_peon)                                    
                            if  peon[0] == "N" and peon[1] == "P":
                                print("No hay jaque")
                                enable_2 = False
                                final = False

                if d-20 >= 0:
                    fila_peon = str(d-20)

                    if int(fila_peon) < 10 and int(fila_peon) >= 0:
                        fila_peon = str(0) + str(fila_peon)                            
                        columan_peon = int(fila_peon[1])
                        fila_peon = int(fila_peon[0])

                    if int(fila_peon) > 9:
                        fila_peon = str(fila_peon)                            
                        columan_peon = int(fila_peon[1])
                        fila_peon = int(fila_peon[0])

                    if self.bando == "B":

                        if fila_peon >= 0 and fila_peon <=7 and columan_peon >= 0  and columan_peon <= 7:
                            
                            if fila_peon == 2:
                                if gridd.get_Tablero(fila_peon,columan_peon) != 0:                                 
                                    peon = gridd.get_Tablero(fila_peon,columan_peon)
                                    
                                    if  peon[0] == "B" and peon[1] == "P":
                                        print("No hay jaque")
                                        enable_2 = False
                                        final = False

                
                fila_peon = str(d+20)
                columan_peon = int(fila_peon[1])
                fila_peon = int(fila_peon[0])

                if self.bando == "N":

                    if fila_peon >= 0 and fila_peon <=7 and columan_peon >= 0  and columan_peon <= 7:
                        
                        if fila_peon == 6:
                            if gridd.get_Tablero(fila_peon,columan_peon) != 0:                                 
                                peon = gridd.get_Tablero(fila_peon,columan_peon)
                                
                                if  peon[0] == "N" and peon[1] == "P":
                                    print("No hay jaque")
                                    enable_2 = False
                                    final = False

                """ if self.checkPawns(self,d,fila_peon,columan_peon,bando):
                    enable_2 = True
                    final = True
                else:
                    enable_2 = False
                    final = False"""


                #rey negro 

            if d < 10:
                fila_aux = str(0) + str(d) 

                columna_aux = int(fila_aux[1])
                fila_aux = int(fila_aux[0])
                
            else:
                fila_aux = str(d) 

                columna_aux = int(fila_aux[1])
                fila_aux = int(fila_aux[0])

            enable_2 = True 
            
            #hacia arriba
            while enable_2:
                
                if self.bando == "B":
                    if fila_aux <= 7 and fila_aux >=0 and columna_aux <= 7 and columna_aux >= 0:
                        if gridd.get_Tablero(fila_aux,columna_aux) != 0:
                            if pieza_enemiga != gridd.get_Tablero(fila_aux,columna_aux):
                                pieza_aliada = gridd.get_Tablero(fila_aux,columna_aux)

                                if pieza_aliada[0] == "B" and pieza_aliada[1] == "T":
                                    enable_2 = False
                                    print("No hay jaque mate.")
                                    final = False
                                elif pieza_aliada[0] == "B" and pieza_aliada[1] == "D":
                                    enable_2 = False
                                    print("No hay jaque mate.")
                                    final = False
                                elif pieza_aliada[0] == "N" or pieza_aliada[0] == "B":
                                    enable_2 = False
                        
           
                    else:
                        enable_2 = False
                        
                elif self.bando == "N":
                    
                    if fila_aux <= 7 and fila_aux >=0 and columna_aux <= 7 and columna_aux >= 0:
                        if pieza_enemiga != gridd.get_Tablero(fila_aux,columna_aux):
                            if gridd.get_Tablero(fila_aux,columna_aux) != 0:

                                pieza_aliada = gridd.get_Tablero(fila_aux,columna_aux)

                                if pieza_aliada[0] == "N" and pieza_aliada[1] == "T":
                                    enable_2 = False
                                    print("No hay jaque mate.")
                                    final = False
                                elif pieza_aliada[0] == "N" and pieza_aliada[1] == "D":
                                    enable_2 = False
                                    print("No hay jaque mate.")
                                    final = False
                                elif pieza_aliada[0] == "N" or pieza_aliada[0] == "B":
                                    enable_2 = False
            
                    else:
                        enable_2 = False
                        
                fila_aux += 1

            enable_2 = True
            if d < 10:
                fila_aux = str(0) + str(d) 

                columna_aux = int(fila_aux[1])
                fila_aux = int(fila_aux[0])
                
            else:
                fila_aux = str(d) 

                columna_aux = int(fila_aux[1])
                fila_aux = int(fila_aux[0])


            #hacia abajo
            while enable_2:
                fila_aux -= 1
                if self.bando == "B":
                    if fila_aux <= 7 and fila_aux >=0 and columna_aux <= 7 and columna_aux >= 0:
                        if pieza_enemiga != gridd.get_Tablero(fila_aux,columna_aux):
                            if gridd.get_Tablero(fila_aux,columna_aux) != 0:
                                pieza_aliada = gridd.get_Tablero(fila_aux,columna_aux)

                                if pieza_aliada[0] == "B" and pieza_aliada[1] == "T":
                                    enable_2 = False
                                    print("No hay jaque mate.")
                                    final = False
                                elif pieza_aliada[0] == "B" and pieza_aliada[1] == "D":
                                    enable_2 = False
                                    print("No hay jaque mate.")
                                    final = False
                                elif pieza_aliada[0] == "N" or pieza_aliada[0] == "B":
                                    enable_2 = False
                        
                            
                    else:
                        enable_2 = False
                    
                elif self.bando == "N":
                    
                    if fila_aux <= 7 and fila_aux >=0 and columna_aux <= 7 and columna_aux >= 0:
                        if pieza_enemiga != gridd.get_Tablero(fila_aux,columna_aux):
                            if gridd.get_Tablero(fila_aux,columna_aux) != 0:
                                pieza_aliada = gridd.get_Tablero(fila_aux,columna_aux)

                                if pieza_aliada[0] == "N" and pieza_aliada[1] == "T":
                                    enable_2 = False
                                    print("No hay jaque mate.")
                                    final = False
                                elif pieza_aliada[0] == "N" and pieza_aliada[1] == "D":
                                    enable_2 = False
                                    print("No hay jaque mate.")
                                    final = False
                                elif pieza_aliada[0] == "N" or pieza_aliada[0] == "B":
                                    enable_2 = False
                         
                                
                    else:
                        enable_2 = False
                        
                

            enable_2 = True
            if d < 10:
                fila_aux = str(0) + str(d) 

                columna_aux = int(fila_aux[1])
                fila_aux = int(fila_aux[0])
                
            else:
                fila_aux = str(d) 

                columna_aux = int(fila_aux[1])
                fila_aux = int(fila_aux[0])
            
            #hacia Derecha
            while enable_2:
                columna_aux += 1
                if self.bando == "B":
                    if fila_aux <= 7 and fila_aux >=0 and columna_aux <= 7 and columna_aux >= 0:
                        if pieza_enemiga != gridd.get_Tablero(fila_aux,columna_aux):
                            if gridd.get_Tablero(fila_aux,columna_aux) != 0:
                                pieza_aliada = gridd.get_Tablero(fila_aux,columna_aux)

                                if pieza_aliada[0] == "B" and pieza_aliada == "T":
                                    enable_2 = False
                                    print("No hay jaque mate.")
                                    final = False
                                elif pieza_aliada[0] == "B" and pieza_aliada == "D":
                                    enable_2 = False
                                    print("No hay jaque mate.")
                                    final = False
                                elif pieza_aliada[0] == "N"or pieza_aliada[0] == "B":
                                    enable_2 = False
           
                    else:
                        enable_2 = False
                    
                        
                elif self.bando == "N":
                    
                    if fila_aux <= 7 and fila_aux >=0 and columna_aux <= 7 and columna_aux >= 0:
                        if pieza_enemiga != gridd.get_Tablero(fila_aux,columna_aux):
                            if gridd.get_Tablero(fila_aux,columna_aux) != 0:
                                pieza_aliada = gridd.get_Tablero(fila_aux,columna_aux)

                                if pieza_aliada[0] == "N" and pieza_aliada == "T":
                                    enable_2 = False
                                    print("No hay jaque mate.")
                                    final = False
                                elif pieza_aliada[0] == "N" and pieza_aliada == "D":
                                    enable_2 = False
                                    print("No hay jaque mate.")
                                    final = False
                                elif pieza_aliada[0] == "N" or pieza_aliada[0] == "B":
                                    enable_2 = False
                  
                            
                    else:
                        enable_2 = False
                    
                
            
            #Seccion de caballo.

            lista_index = [21,19,12,8]
            
            if self.bando == "B":
                for t in range(0, len(lista_index)):
                    operacion = d + lista_index[t]
                    operacion_c = -1
                    operacion_f = -1
                    if operacion < 10 and operacion >= 0 :

                        operacion = str(0)+str(operacion)
                        operacion_f = int(operacion[0]) 
                        operacion_c = int(operacion[1])
                    elif operacion >= 0:
                        operacion = str(operacion)
                        operacion_f = int(operacion[0]) 
                        operacion_c = int(operacion[1])

                    
                    if operacion_f <= 7 and operacion_f >=0 and operacion_c <= 7 and operacion_c >= 0:
                        if gridd.get_Tablero(operacion_f,operacion_c) != 0:
                            casilla_analizar = gridd.get_Tablero(operacion_f,operacion_c)
                            if casilla_analizar[0] == "B" and casilla_analizar[1] == "C":
                                print("No hay jaque.")
                                final = False

                for t in range(0, len(lista_index)):
                    operacion = d - lista_index[t]
                    operacion_c = -1
                    operacion_f = -1
                    if operacion < 10 and operacion >= 0 :

                        operacion = str(0)+str(operacion)
                        operacion_f = int(operacion[0])
                        operacion_c = int(operacion[1])
                    elif operacion >= 0:
                        operacion = str(operacion)
                        operacion_f = int(operacion[0]) 
                        operacion_c = int(operacion[1])

                    if operacion_f <= 7 and operacion_f >=0 and operacion_c <= 7 and operacion_c >= 0:
                        if gridd.get_Tablero(operacion_f,operacion_c) != 0:
                            casilla_analizar = gridd.get_Tablero(operacion_f,operacion_c)
                            if casilla_analizar[0] == "B" and casilla_analizar[1] == "C":
                                print("No hay jaque.")
                                final = False

            elif self.bando == "N":
                for t in range(0, len(lista_index)):
                    operacion = d + lista_index[t]
                    operacion_c = -1
                    operacion_f = -1
                    if operacion < 10 and operacion >= 0 :

                        operacion = str(0)+str(operacion)
                        operacion_f = int(operacion[0]) 
                        operacion_c = int(operacion[1])
                    elif operacion >= 0:
                        operacion = str(operacion)
                        operacion_f = int(operacion[0]) 
                        operacion_c = int(operacion[1])
                    
                    if operacion_f <= 7 and operacion_f >=0 and operacion_c <= 7 and operacion_c >= 0:
                        if gridd.get_Tablero(operacion_f,operacion_c) != 0:
                            casilla_analizar = gridd.get_Tablero(operacion_f,operacion_c)
                            if casilla_analizar[0] == "N" and casilla_analizar[1] == "C":
                                print("No hay jaque.")
                                final = False
                            
                
                for t in range(0, len(lista_index)):
                    operacion = d - lista_index[t]
                    operacion_c = -1
                    operacion_f = -1
                    if operacion < 10 and operacion >= 0 :

                        operacion = str(0)+str(operacion)
                        operacion_f = int(operacion[0]) 
                        operacion_c = int(operacion[1])
                    elif operacion >= 0:
                        operacion = str(operacion)
                        operacion_f = int(operacion[0]) 
                        operacion_c = int(operacion[1])
                    
                    if operacion_f <= 7 and operacion_f >=0 and operacion_c <= 7 and operacion_c >= 0:
                        if gridd.get_Tablero(operacion_f,operacion_c) != 0:
                            casilla_analizar = gridd.get_Tablero(operacion_f,operacion_c)
                            if casilla_analizar[0] == "N" and casilla_analizar[1] == "C":
                                print("No hay jaque.")
                                final = False


            #Seccion Diagonales.

            #Diagonal subiendo izquierda
            enable_2 = True

            if d < 10:
                fila_aux = str(0) + str(d) 

                columna_aux = int(fila_aux[1])
                fila_aux = int(fila_aux[0])
                
            else:
                fila_aux = str(d) 

                columna_aux = int(fila_aux[1])
                fila_aux = int(fila_aux[0])

            while enable_2:
                fila_aux += 1
                columna_aux -= 1
                if self.bando == "B":
                    if fila_aux >= 0 and columna_aux >= 0 and fila_aux <= 7 and columna_aux <= 7:
                        if pieza_enemiga != gridd.get_Tablero(fila_aux,columna_aux):
                            if gridd.get_Tablero(fila_aux,columna_aux) != 0:
                                casilla = gridd.get_Tablero(fila_aux,columna_aux)
                                if casilla[0] == "B" and casilla[1] == "A":
                                    print("No hay jaque.")
                                    enable_2 = False
                                    final = False
                                if casilla[0] == "B" and casilla[1] == "D":
                                    print("No hay jaque.")
                                    enable_2 = False
                                    final = False
                                if casilla[0] == "B" or casilla[0] == "N":
                                    enable_2 = False
                       
                    else:
                        enable_2 = False
                
                elif self.bando == "N":
                    if fila_aux >= 0 and columna_aux >= 0 and fila_aux <= 7 and columna_aux <= 7:
                        if gridd.get_Tablero(fila_aux,columna_aux) != 0:
                            casilla = gridd.get_Tablero(fila_aux,columna_aux)
                            if casilla[0] == "N" and casilla[1] == "A":
                                print("No hay jaque.")
                                enable_2 = False
                                final = False
                            if casilla[0] == "N" and casilla[1] == "D":
                                print("No hay jaque.")
                                enable_2 = False
                                final = False
                            if casilla[0] == "B" or casilla[0] == "N":
                                enable_2 = False
            
                    else:
                        enable_2 = False
                        

            #Diagonal subiendo derecha
            enable_2 = True
            if d < 10:
                fila_aux = str(0) + str(d) 

                columna_aux = int(fila_aux[1])
                fila_aux = int(fila_aux[0])
                
            else:
                fila_aux = str(d) 

                columna_aux = int(fila_aux[1])
                fila_aux = int(fila_aux[0])

            while enable_2:
                fila_aux += 1
                columna_aux += 1
                if self.bando == "B":
                    if fila_aux >= 0 and columna_aux >= 0 and fila_aux <= 7 and columna_aux <= 7:
                        if pieza_enemiga != gridd.get_Tablero(fila_aux,columna_aux):
                            if gridd.get_Tablero(fila_aux,columna_aux) != 0:
                                casilla = gridd.get_Tablero(fila_aux,columna_aux)
                                if casilla[0] == "B" and casilla[1] == "A":
                                    print("No hay jaque.")
                                    enable_2 = False
                                    final = False
                                if casilla[0] == "B" and casilla[1] == "D":
                                    print("No hay jaque.")
                                    enable_2 = False
                                    final = False
                                if casilla[0] == "B" or casilla[0] == "N":
                                    enable_2 = False
 
                    else:
                        enable_2 = False
                           
                elif self.bando == "N":
                    if fila_aux >= 0 and columna_aux >= 0 and fila_aux <= 7 and columna_aux <= 7:
                        if pieza_enemiga != gridd.get_Tablero(fila_aux,columna_aux):
                            if gridd.get_Tablero(fila_aux,columna_aux) != 0:
                                casilla = gridd.get_Tablero(fila_aux,columna_aux)
                                if casilla[0] == "N" and casilla[1] == "A":
                                    print("No hay jaque.")
                                    enable_2 = False
                                    final = False
                                if casilla[0] == "N" and casilla[1] == "D":
                                    print("No hay jaque.")
                                    enable_2 = False
                                    final = False
                                if casilla[0] == "B" or casilla[0] == "N":
                                    enable_2 = False
                            
                    else:
                        enable_2 = False
                        

            #Diagonal bajando izquierda

            enable_2 = True

            if d < 10:
                fila_aux = str(0) + str(d) 

                columna_aux = int(fila_aux[1])
                fila_aux = int(fila_aux[0])
                
            else:
                fila_aux = str(d) 

                columna_aux = int(fila_aux[1])
                fila_aux = int(fila_aux[0])

            while enable_2:
                fila_aux -= 1
                columna_aux -= 1
                if self.bando == "B":
                    if fila_aux >= 0 and columna_aux >= 0 and fila_aux <= 7 and columna_aux <= 7:
                        if pieza_enemiga != gridd.get_Tablero(fila_aux,columna_aux):
                            if gridd.get_Tablero(fila_aux,columna_aux) != 0:
                                casilla = gridd.get_Tablero(fila_aux,columna_aux)
                                if casilla[0] == "B" and casilla[1] == "A":
                                    print("No hay jaque.")
                                    enable_2 = False
                                    final = False
                                if casilla[0] == "B" and casilla[1] == "D":
                                    print("No hay jaque.")
                                    enable_2 = False
                                    final = False
                                if casilla[0] == "B" or casilla[0] == "N":
                                    enable_2 = False
 
                    else:

                        enable_2 = False
                       
                
                elif self.bando == "N":
                    if fila_aux >= 0 and columna_aux >= 0 and fila_aux <= 7 and columna_aux <= 7:
                        if pieza_enemiga != gridd.get_Tablero(fila_aux,columna_aux):
                            if gridd.get_Tablero(fila_aux,columna_aux) != 0:
                                casilla = gridd.get_Tablero(fila_aux,columna_aux)
                                if casilla[0] == "N" and casilla[1] == "A":
                                    print("No hay jaque.")
                                    enable_2 = False
                                    final = False
                                if casilla[0] == "N" and casilla[1] == "D":
                                    print("No hay jaque.")
                                    enable_2 = False
                                    final = False
                                if casilla[0] == "B" or casilla[0] == "N":
                                    enable_2 = False
 
                          
                    else:
                        enable_2 = False
                         

            #Diagonal bajando derecha
            enable_2 = True
            if d < 10:
                fila_aux = str(0) + str(d) 

                columna_aux = int(fila_aux[1])
                fila_aux = int(fila_aux[0])
                
            else:
                fila_aux = str(d) 

                columna_aux = int(fila_aux[1])
                fila_aux = int(fila_aux[0])

            while enable_2:
                fila_aux -= 1
                columna_aux += 1
                if self.bando == "B":
                    if fila_aux >= 0 and columna_aux >= 0 and fila_aux <= 7 and columna_aux <= 7:
                        if pieza_enemiga != gridd.get_Tablero(fila_aux,columna_aux):
                            if gridd.get_Tablero(fila_aux,columna_aux) != 0:
                                casilla = gridd.get_Tablero(fila_aux,columna_aux)
                                if casilla[0] == "B" and casilla[1] == "A":
                                    print("No hay jaque.")
                                    enable_2 = False
                                    final = False
                                if casilla[0] == "B" and casilla[1] == "D":
                                    print("No hay jaque.")
                                    enable_2 = False
                                    final = False
                                if casilla[0] == "B" or casilla[0] == "N":
                                    enable_2 = False
        
                    else:
                        enable_2 = False
                     
                
                elif self.bando == "N":
                    if fila_aux >= 0 and columna_aux >= 0 and fila_aux <= 7 and columna_aux <= 7:
                        if pieza_enemiga != gridd.get_Tablero(fila_aux,columna_aux):
                            if gridd.get_Tablero(fila_aux,columna_aux) != 0:
                                casilla = gridd.get_Tablero(fila_aux,columna_aux)
                                if casilla[0] == "N" and casilla[1] == "A":
                                    print("No hay jaque.")
                                    enable_2 = False
                                    final = False
                                if casilla[0] == "N" and casilla[1] == "D":
                                    print("No hay jaque.")
                                    enable_2 = False
                                    final = False
                                if casilla[0] == "B" or casilla[0] == "N":
                                    enable_2 = False
                       
                    else:
                        enable_2 = False
                        

            cuenta_permitida += 1
        if final == False:
            return True
        return False

    def jaque_mate(self):
        #comprobacion de que su circulo interior no haya mas moviminetos 
        final = True
        enable_2 = True 
        print(Rey.Index_jaque,Rey.Casilla,Rey.Direccion)
        print(self.Index_jaque)

        print(Rey.Direccion)
        if self.Index_jaque >= 1:
            for ii in Rey.Direccion:

                print(ii)
                
                casilla_actual = Rey.Casilla[ii]
                casilla_actual = int(casilla_actual[0][2:4])
                if casilla_actual < 10:
                    casilla_actual = str(0) + str(casilla_actual)
                casilla_destino = int(str(self.posicion_anterior_fila)+str(self.posicion_anterior_columna))
                #seccion de peon.

                #esta seccion comenzara en diagonal con la posicion de la pieza que esta dando jaque, y si resulta que el peon protege no habra jaque
                fila_peon = str(casilla_actual)
                columan_peon = int(fila_peon[1])
                fila_peon = int(fila_peon[0])
                if self.bando == "B":
                    #diagonal izquierda abajo
                    if fila_peon-1 >= 0 and fila_peon-1 <=7 and columan_peon-1 >= 0  and columan_peon-1 <= 7:
                        if gridd.get_Tablero(fila_peon-1,columan_peon-1) != 0:
                            peon = gridd.get_Tablero(fila_peon-1,columan_peon-1)
                            if  peon[0] == "B" and peon[1] == "P":
                                print("No hay jaque")
                                enable_2 = False
                                Final = False
                    #diagonal derecha abajo
                    if fila_peon-1 >= 0 and fila_peon-1 <= 7 and  columan_peon+1 >= 0  and columan_peon+1 <= 7:
                        if gridd.get_Tablero(fila_peon-1,columan_peon+1) != 0:
                            peon = gridd.get_Tablero(fila_peon-1,columan_peon+1)
                            if  peon[0] == "B" and peon[1] == "P":
                                print("No hay jaque")
                                enable_2 = False
                                Final = False

                fila_peon = str(casilla_actual)
                columan_peon = int(fila_peon[1])
                fila_peon = int(fila_peon[0])
                if self.bando == "N":

                    #diagonal izquierda arriba
                    if fila_peon+1 >= 0 and fila_peon+1 <=7 and columan_peon-1 >= 0  and columan_peon-1 <= 7:
                        if gridd.get_Tablero(fila_peon+1,columan_peon-1) != 0:
                            peon = gridd.get_Tablero(fila_peon+1,columan_peon-1)
                            if  peon[0] == "N" and peon[1] == "P":
                                print("No hay jaque")
                                enable_2 = False
                                final = False


                    #diagonal derecha arriba
                    if fila_peon+1 >= 0 and fila_peon+1 <= 7 and  columan_peon+1 >= 0  and columan_peon+1 <= 7:
                        if gridd.get_Tablero(fila_peon+1,columan_peon+1) != 0:
                            peon = gridd.get_Tablero(fila_peon+1,columan_peon+1)
                            if  peon[0] == "N" and peon[1] == "P":
                                print("No hay jaque")
                                enable_2 = False
                                final = False
                    
                if ii == "Izquierda":
                    if self.izquierda(-1,casilla_actual,casilla_destino,enable_2,final):
                        final = False
                    else:
                        pass
 
                if ii == "Derecha":
                    if self.izquierda(1,casilla_actual,casilla_destino,enable_2,final):
                        final = False
                    else:
                        print("no hay jaque mate.")
 
                if ii == "Arriba": 
                    if self.izquierda(10,casilla_actual,casilla_destino,enable_2,final):
                        final = False
                    else:
                        print("no hay jaque mate.")

                if ii == "Abajo": 
                    if self.izquierda(-10,casilla_actual,casilla_destino,enable_2,final):
                        final = False
                    else:
                        print("no hay jaque mate.")
                 
                if ii == "DigIzAb": 
                    if self.izquierda(-11,casilla_actual,casilla_destino,enable_2,final):
                        final = False
                    else:
                        print("no hay jaque mate.")
                
                if ii == "DigIzArr": 
                    if self.izquierda(11,casilla_actual,casilla_destino,enable_2,final):
                        final = False
                    else:
                        print("no hay jaque mate.")

                if ii == "DigDrAb": 
                    if self.izquierda(-11,casilla_actual,casilla_destino,enable_2,final):
                        final = False
                    else:
                        print("no hay jaque mate.")

                if ii == "DigDrArr": 
                    if self.izquierda(11,casilla_actual,casilla_destino,enable_2,final):
                        final = False
                    else:
                        print("no hay jaque mate.")
                #Seccion de caballo
                if ii == "Caballo":
    
                    fila_peon = str(casilla_actual)
                    columan_peon = int(fila_peon[1])
                    fila_peon = int(fila_peon[0])
                    if self.bando == "B":
                    
                        if fila_peon-1 >= 0 and fila_peon-1 <=7 and columan_peon-1 >= 0  and columan_peon-1 <= 7:
                            if gridd.get_Tablero(fila_peon-1,columan_peon-1) != 0:
                                peon = gridd.get_Tablero(fila_peon-1,columan_peon-1)
                                if  peon[0] == "B" and peon[1] == "P":
                                    print("No hay jaque")
                                    enable_2 = False
                                    final = False
                        #diagonal derecha abajo
                        if fila_peon-1 >= 0 and fila_peon-1 <= 7 and  columan_peon+1 >= 0  and columan_peon+1 <= 7:
                            if gridd.get_Tablero(fila_peon-1,columan_peon+1) != 0:
                                peon = gridd.get_Tablero(fila_peon-1,columan_peon+1)
                                if  peon[0] == "B" and peon[1] == "P":
                                    print("No hay jaque")
                                    enable_2 = False
                                    final = False
                        lista_index = [21,19,12,8]
                    
                        enable_2 = True
                        if int(casilla_actual) < 10:
                            fila_aux = str(0) + str(casilla_actual) 

                            columna_aux = int(fila_aux[1])
                            fila_aux = int(fila_aux[0])
                            
                        else:
                            fila_aux = str(casilla_actual) 

                            columna_aux = int(fila_aux[1])
                            fila_aux = int(fila_aux[0])
                       
                        #hacia arriba
                        while enable_2:
                            if self.CheckDirrections(enable_2,final,fila_aux,columna_aux):
                                enable_2 = False
                            else:
                                enable_2 = False
                                final = False
                                        
                            fila_aux += 1
                        
                        

                        #hacia abajo
                        enable_2 = True
                        if int(casilla_actual) < 10:
                            fila_aux = str(0) + str(casilla_actual) 

                            columna_aux = int(fila_aux[1])
                            fila_aux = int(fila_aux[0])
                            
                        else:
                            fila_aux = str(casilla_actual) 

                            columna_aux = int(fila_aux[1])
                            fila_aux = int(fila_aux[0])
                        #hacia abajo
                        while enable_2:
                            if self.CheckDirrections(enable_2,final,fila_aux,columna_aux):
                                enable_2 = False
                            else:
                                enable_2 = False
                                final = False    
                            fila_aux -= 1

             
                        #hacia derecha
                        enable_2 = True
                        if int(casilla_actual) < 10:
                            fila_aux = str(0) + str(casilla_actual) 

                            columna_aux = int(fila_aux[1])
                            fila_aux = int(fila_aux[0])
                            
                        else:
                            fila_aux = str(casilla_actual) 

                            columna_aux = int(fila_aux[1])
                            fila_aux = int(fila_aux[0])

                        while enable_2:
                            if self.CheckDirrections(enable_2,final,fila_aux,columna_aux):
                                enable_2 = False
                            else:
                                enable_2 = False
                                final = False

                            columna_aux += 1

                        #hacia izquierda
                        enable_2 = True
                        if int(casilla_actual) < 10:
                            fila_aux = str(0) + str(casilla_actual) 

                            columna_aux = int(fila_aux[1])
                            fila_aux = int(fila_aux[0])
                            
                        else:
                            fila_aux = str(casilla_actual) 

                            columna_aux = int(fila_aux[1])
                            fila_aux = int(fila_aux[0])

                        while enable_2:
                            if self.CheckDirrections(enable_2,final,fila_aux,columna_aux):
                                enable_2 = False
                            else:
                                enable_2 = False
                                final = False

                            columna_aux -= 1

                        #digarribaderecha
                        enable_2 = True
                        if int(casilla_actual) < 10:
                            fila_aux = str(0) + str(casilla_actual) 

                            columna_aux = int(fila_aux[1])
                            fila_aux = int(fila_aux[0])
                            
                        else:
                            fila_aux = str(casilla_actual) 

                            columna_aux = int(fila_aux[1])
                            fila_aux = int(fila_aux[0])
                        while enable_2:
                            fila_aux += 1
                            columna_aux += 1
                            if self.Checkdiagonals(fila_aux,columna_aux,enable_2,final):
                                enable_2 =False
                            else:
                                final = False

                        #digarribaizquierda
                        enable_2 = True
                        if int(casilla_actual) < 10:
                            fila_aux = str(0) + str(casilla_actual) 

                            columna_aux = int(fila_aux[1])
                            fila_aux = int(fila_aux[0])
                            
                        else:
                            fila_aux = str(casilla_actual) 

                            columna_aux = int(fila_aux[1])
                            fila_aux = int(fila_aux[0])
                        while enable_2:
                            fila_aux += 1
                            columna_aux -= 1
                            if self.Checkdiagonals(fila_aux,columna_aux,enable_2,final):
                                enable_2 =False
                            else:
                                final = False
                            
                        #digabajoderecha
                        enable_2 = True
                        if int(casilla_actual) < 10:
                            fila_aux = str(0) + str(casilla_actual) 

                            columna_aux = int(fila_aux[1])
                            fila_aux = int(fila_aux[0])
                            
                        else:
                            fila_aux = str(casilla_actual) 

                            columna_aux = int(fila_aux[1])
                            fila_aux = int(fila_aux[0])
                        while enable_2:
                            fila_aux -= 1
                            columna_aux += 1
                            if self.Checkdiagonals(fila_aux,columna_aux,enable_2,final):
                                enable_2 =False
                            else:
                                final = False


                        #digabajoizquierda
                        enable_2 = True
                        if int(casilla_actual) < 10:
                            fila_aux = str(0) + str(casilla_actual) 

                            columna_aux = int(fila_aux[1])
                            fila_aux = int(fila_aux[0])
                            
                        else:
                            fila_aux = str(casilla_actual) 

                            columna_aux = int(fila_aux[1])
                            fila_aux = int(fila_aux[0])
                        while enable_2:
                            fila_aux -= 1
                            columna_aux -= 1
                            if self.Checkdiagonals(fila_aux,columna_aux,enable_2,final):
                                enable_2 =False
                            else:
                                final = False
                            
                            
                        if self.bando == "B":   
                            for t in range(0, len(lista_index)):
                                operacion = int(casilla_actual) + lista_index[t]
                                operacion_c = -1
                                operacion_f = -1
                                if operacion < 10 and operacion >= 0 :

                                    operacion = str(0)+str(operacion)
                                    operacion_f = int(operacion[0]) 
                                    operacion_c = int(operacion[1])
                                elif operacion >= 0:
                                    operacion = str(operacion)
                                    operacion_f = int(operacion[0]) 
                                    operacion_c = int(operacion[1])

                                
                                if operacion_f <= 7 and operacion_f >=0 and operacion_c <= 7 and operacion_c >= 0:
                                    if gridd.get_Tablero(operacion_f,operacion_c) != 0:
                                        casilla_analizar = gridd.get_Tablero(operacion_f,operacion_c)
                                        if casilla_analizar[0] == "B" and casilla_analizar[1] == "C":
                                            print("No hay jaque.")
                                            final = False
                                        
                                            final = False
                        
                            for t in range(0, len(lista_index)):
                                operacion = int(casilla_actual) - lista_index[t]
                                operacion_c = -1
                                operacion_f = -1
                                if operacion < 10 and operacion >= 0 :

                                    operacion = str(0)+str(operacion)
                                    operacion_f = int(operacion[0])
                                    operacion_c = int(operacion[1])
                                elif operacion >= 0:
                                    operacion = str(operacion)
                                    operacion_f = int(operacion[0]) 
                                    operacion_c = int(operacion[1])

                                if operacion_f <= 7 and operacion_f >=0 and operacion_c <= 7 and operacion_c >= 0:
                                    if gridd.get_Tablero(operacion_f,operacion_c) != 0:
                                        casilla_analizar = gridd.get_Tablero(operacion_f,operacion_c)
                                        if casilla_analizar[0] == "B" and casilla_analizar[1] == "C":
                                            print("No hay jaque.")
                                            final = False

                        elif self.bando == "N":
                                for t in range(0, len(lista_index)):
                                    operacion = int(casilla_actual) + lista_index[t]
                                    operacion_c = -1
                                    operacion_f = -1
                                    if operacion < 10 and operacion >= 0 :

                                        operacion = str(0)+str(operacion)
                                        operacion_f = int(operacion[0]) 
                                        operacion_c = int(operacion[1])
                                    elif operacion >= 0:
                                        operacion = str(operacion)
                                        operacion_f = int(operacion[0]) 
                                        operacion_c = int(operacion[1])
                                    
                                    if operacion_f <= 7 and operacion_f >=0 and operacion_c <= 7 and operacion_c >= 0:
                                        if gridd.get_Tablero(operacion_f,operacion_c) != 0:
                                            casilla_analizar = gridd.get_Tablero(operacion_f,operacion_c)
                                            if casilla_analizar[0] == "N" and casilla_analizar[1] == "C":
                                                print("No hay jaque.")
                                                final = False
                                                
                                
                                for t in range(0, len(lista_index)):
                                    operacion = int(casilla_actual) - lista_index[t]
                                    operacion_c = -1
                                    operacion_f = -1
                                    if operacion < 10 and operacion >= 0 :

                                        operacion = str(0)+str(operacion)
                                        operacion_f = int(operacion[0]) 
                                        operacion_c = int(operacion[1])
                                    elif operacion >= 0:
                                        operacion = str(operacion)
                                        operacion_f = int(operacion[0]) 
                                        operacion_c = int(operacion[1])
                                    
                                    if operacion_f <= 7 and operacion_f >=0 and operacion_c <= 7 and operacion_c >= 0:
                                        if gridd.get_Tablero(operacion_f,operacion_c) != 0:
                                            casilla_analizar = gridd.get_Tablero(operacion_f,operacion_c)
                                            if casilla_analizar[0] == "N" and casilla_analizar[1] == "C":
                                                print("No hay jaque.")
                                                final = False

                    fila_peon = str(casilla_actual)
                    columan_peon = int(fila_peon[1])
                    fila_peon = int(fila_peon[0])
                    if self.bando == "N":

                        #diagonal izquierda arriba
                        if fila_peon+1 >= 0 and fila_peon+1 <=7 and columan_peon-1 >= 0  and columan_peon-1 <= 7:
                            if gridd.get_Tablero(fila_peon+1,columan_peon-1) != 0:
                                peon = gridd.get_Tablero(fila_peon+1,columan_peon-1)
                                if  peon[0] == "N" and peon[1] == "P":
                                    print("No hay jaque")
                                    enable_2 = False
                                    final = False

                        #diagonal derecha arriba
                        if fila_peon+1 >= 0 and fila_peon+1 <= 7 and  columan_peon+1 >= 0  and columan_peon+1 <= 7:
                            if gridd.get_Tablero(fila_peon+1,columan_peon+1) != 0:
                                peon = gridd.get_Tablero(fila_peon+1,columan_peon+1)
                                if  peon[0] == "N" and peon[1] == "P":
                                    print("No hay jaque")
                                    enable_2 = False
                                    final = False
                    

                        lista_index = [21,19,12,8]
                    
                        enable_2 = True
                        if int(casilla_actual) < 10:
                            fila_aux = str(0) + str(casilla_actual) 

                            columna_aux = int(fila_aux[1])
                            fila_aux = int(fila_aux[0])
                            
                        else:
                            fila_aux = str(casilla_actual) 

                            columna_aux = int(fila_aux[1])
                            fila_aux = int(fila_aux[0])
                        #hacia arriba
                        while enable_2:
                            if self.CheckDirrections(enable_2,final,fila_aux,columna_aux):
                                enable_2 = False
                            else:
                                enable_2 = False
                                final = False
                                        
                            fila_aux += 1

                        #hacia abajo
                        enable_2 = True
                        if int(casilla_actual) < 10:
                            fila_aux = str(0) + str(casilla_actual) 

                            columna_aux = int(fila_aux[1])
                            fila_aux = int(fila_aux[0])
                            
                        else:
                            fila_aux = str(casilla_actual) 

                            columna_aux = int(fila_aux[1])
                            fila_aux = int(fila_aux[0])
                        #hacia abajo
                        while enable_2:
                            if self.CheckDirrections(enable_2,final,fila_aux,columna_aux):
                                enable_2 = False
                            else:
                                enable_2 = False
                                final = False    
                            fila_aux -= 1
                        

                        #hacia derecha
                        enable_2 = True
                        if int(casilla_actual) < 10:
                            fila_aux = str(0) + str(casilla_actual) 

                            columna_aux = int(fila_aux[1])
                            fila_aux = int(fila_aux[0])
                            
                        else:
                            fila_aux = str(casilla_actual) 

                            columna_aux = int(fila_aux[1])
                            fila_aux = int(fila_aux[0])

                        while enable_2:
                            if self.CheckDirrections(enable_2,final,fila_aux,columna_aux):
                                enable_2 = False
                            else:
                                enable_2 = False
                                final = False

                            columna_aux += 1

                        #hacia izquierda
                        enable_2 = True
                        if int(casilla_actual) < 10:
                            fila_aux = str(0) + str(casilla_actual) 

                            columna_aux = int(fila_aux[1])
                            fila_aux = int(fila_aux[0])
                            
                        else:
                            fila_aux = str(casilla_actual) 

                            columna_aux = int(fila_aux[1])
                            fila_aux = int(fila_aux[0])

                        while enable_2:
                            if self.CheckDirrections(enable_2,final,fila_aux,columna_aux):
                                enable_2 = False
                            else:
                                enable_2 = False
                                final = False

                            columna_aux -= 1

                        
                        #digarribaderecha
                        enable_2 = True
                        if int(casilla_actual) < 10:
                            fila_aux = str(0) + str(casilla_actual) 

                            columna_aux = int(fila_aux[1])
                            fila_aux = int(fila_aux[0])
                            
                        else:
                            fila_aux = str(casilla_actual) 

                            columna_aux = int(fila_aux[1])
                            fila_aux = int(fila_aux[0])
                        while enable_2:
                            fila_aux += 1
                            columna_aux += 1
                            if self.Checkdiagonals(fila_aux,columna_aux,enable_2,final):
                                enable_2 =False
                            else:
                                final = False

                        #digarribaizquierda
                        enable_2 = True
                        if int(casilla_actual) < 10:
                            fila_aux = str(0) + str(casilla_actual) 

                            columna_aux = int(fila_aux[1])
                            fila_aux = int(fila_aux[0])
                            
                        else:
                            fila_aux = str(casilla_actual) 

                            columna_aux = int(fila_aux[1])
                            fila_aux = int(fila_aux[0])
                        while enable_2:
                            fila_aux += 1
                            columna_aux -= 1
                            if self.Checkdiagonals(fila_aux,columna_aux,enable_2,final):
                                enable_2 =False
                            else:
                                final = False

                        #digabajoderecha
                        enable_2 = True
                        if int(casilla_actual) < 10:
                            fila_aux = str(0) + str(casilla_actual) 

                            columna_aux = int(fila_aux[1])
                            fila_aux = int(fila_aux[0])
                            
                        else:
                            fila_aux = str(casilla_actual) 

                            columna_aux = int(fila_aux[1])
                            fila_aux = int(fila_aux[0])
                        
                        while enable_2:
                            fila_aux -= 1
                            columna_aux += 1
                            if self.Checkdiagonals(fila_aux,columna_aux,enable_2,final):
                                enable_2 =False
                            else:
                                final = False

                        #digabajoizquierda
                        enable_2 = True
                        if int(casilla_actual) < 10:
                            fila_aux = str(0) + str(casilla_actual) 

                            columna_aux = int(fila_aux[1])
                            fila_aux = int(fila_aux[0])
                            
                        else:
                            fila_aux = str(casilla_actual) 

                            columna_aux = int(fila_aux[1])
                            fila_aux = int(fila_aux[0])
                        while enable_2:
                            fila_aux -= 1
                            columna_aux -= 1
                            if self.Checkdiagonals(fila_aux,columna_aux,enable_2,final):
                                enable_2 =False
                            else:
                                final = False
                            
                            
                        if self.bando == "B":   
                            for t in range(0, len(lista_index)):
                                operacion = int(casilla_actual) + lista_index[t]
                                operacion_c = -1
                                operacion_f = -1
                                if operacion < 10 and operacion >= 0 :

                                    operacion = str(0)+str(operacion)
                                    operacion_f = int(operacion[0]) 
                                    operacion_c = int(operacion[1])
                                elif operacion >= 0:
                                    operacion = str(operacion)
                                    operacion_f = int(operacion[0]) 
                                    operacion_c = int(operacion[1])

                                
                                if operacion_f <= 7 and operacion_f >=0 and operacion_c <= 7 and operacion_c >= 0:
                                    if gridd.get_Tablero(operacion_f,operacion_c) != 0:
                                        if casilla_analizar[0] == "B" and casilla_analizar[1] == "C":
                                            print("No hay jaque.")
                                            final = False
                                        
                                            final = False
                        
                            for t in range(0, len(lista_index)):
                                operacion = int(casilla_actual) - lista_index[t]
                                operacion_c = -1
                                operacion_f = -1
                                if operacion < 10 and operacion >= 0 :

                                    operacion = str(0)+str(operacion)
                                    operacion_f = int(operacion[0])
                                    operacion_c = int(operacion[1])
                                elif operacion >= 0:
                                    operacion = str(operacion)
                                    operacion_f = int(operacion[0]) 
                                    operacion_c = int(operacion[1])

                                if operacion_f <= 7 and operacion_f >=0 and operacion_c <= 7 and operacion_c >= 0:
                                    if gridd.get_Tablero(operacion_f,operacion_c) != 0:
                                        casilla_analizar = gridd.get_Tablero(operacion_f,operacion_c)
                                        if casilla_analizar[0] == "B" and casilla_analizar[1] == "C":
                                            print("No hay jaque.")
                                            final = False

                        elif self.bando == "N":
                                for t in range(0, len(lista_index)):
                                    operacion = int(casilla_actual) + lista_index[t]
                                    operacion_c = -1
                                    operacion_f = -1
                                    if operacion < 10 and operacion >= 0 :

                                        operacion = str(0)+str(operacion)
                                        operacion_f = int(operacion[0]) 
                                        operacion_c = int(operacion[1])
                                    elif operacion >= 0:
                                        operacion = str(operacion)
                                        operacion_f = int(operacion[0]) 
                                        operacion_c = int(operacion[1])
                                    
                                    if operacion_f <= 7 and operacion_f >=0 and operacion_c <= 7 and operacion_c >= 0:
                                        if gridd.get_Tablero(operacion_f,operacion_c) != 0:
                                            casilla_analizar = gridd.get_Tablero(operacion_f,operacion_c)
                                            if casilla_analizar[0] == "N" and casilla_analizar[1] == "C":
                                                print("No hay jaque.")
                                                final = False
                                                
                                
                                for t in range(0, len(lista_index)):
                                    operacion = int(casilla_actual) - lista_index[t]
                                    operacion_c = -1
                                    operacion_f = -1
                                    if operacion < 10 and operacion >= 0 :

                                        operacion = str(0)+str(operacion)
                                        operacion_f = int(operacion[0]) 
                                        operacion_c = int(operacion[1])
                                    elif operacion >= 0:
                                        operacion = str(operacion)
                                        operacion_f = int(operacion[0]) 
                                        operacion_c = int(operacion[1])
                                    
                                    if operacion_f <= 7 and operacion_f >=0 and operacion_c <= 7 and operacion_c >= 0:
                                        if gridd.get_Tablero(operacion_f,operacion_c) != 0:
                                            casilla_analizar = gridd.get_Tablero(operacion_f,operacion_c)
                                            if casilla_analizar[0] == "N" and casilla_analizar[1] == "C":
                                                print("No hay jaque.")
                                                final = False


            if  final == True:
                #Comprobacion de los espacios.
                fila = self.posicion_anterior_fila
                columna = self.posicion_anterior_columna  
                casilla_a_comparar = int(str(fila) + str(columna))
                limite = 0
                for x in range(fila-1,fila+2):
                    for y in range(columna-1,columna+2):
                                
                        if x >= 0 and x <= 7:
                            if y >= 0 and y <= 7:
                                combinacion = int(str(x)+str(y))
                                if casilla_a_comparar != combinacion:
                                    if self.bando == "B":
                                        p = gridd.get_Tablero(x,y)
                                        if gridd.get_Tablero(x,y) != 0 and p[0] == "B":
                                            limite += 1
                                        if gridd.get_Tablero(x,y) != 0:
                                            if p[0] == "N":
                                                rey_aux = Rey(self.bando,self.pieza,self.posicion_anterior_fila,self.posicion_anterior_columna,x,y)
                                              
                                                rey_aux.restricciones(x,y)
                                                if rey_aux.Index_jaque >= 1:
                                                    limite += 1
                                                
                                        elif gridd.get_Tablero(x,y) == 0:
                                            rey_aux = Rey(self.bando,self.pieza,self.posicion_anterior_fila,self.posicion_anterior_columna,x,y)
                                      
                                            rey_aux.restricciones(x,y)
                                            
                                                                        
                                            if rey_aux.Index_jaque >= 1:
                                                limite += 1
                                                
                                    if self.bando == "N":
                                        p = gridd.get_Tablero(x,y)
                                        
                                        if gridd.get_Tablero(x,y) != 0 and p[0] == "N":
                                     
                                            limite += 1
                                            
                                        if gridd.get_Tablero(x,y) != 0:
                                            if p[0] == "B":
                                                rey_aux = Rey(self.bando,self.pieza,self.posicion_anterior_fila,self.posicion_anterior_columna,x,y)
                                                rey_aux.restricciones(x,y)
                                                if rey_aux.Index_jaque >= 1:
                                               
                                                    limite += 1

                                        elif gridd.get_Tablero(x,y) == 0:
                                            rey_aux = Rey(self.bando,self.pieza,self.posicion_anterior_fila,self.posicion_anterior_columna,x,y)
                                            
                                            rey_aux.restricciones(x,y)
                                                                        
                                            if rey_aux.Index_jaque >= 1:
                                            
                                                limite += 1
                            else: 
                                limite += 1
                        else: 
                            limite += 1
                if limite == 8:
                    print("Jaque mate.")
                    return True
            
                
        if self.Index_jaque == 2:

            if  final == True:
                #Comprobacion de los espacios.
                fila = self.posicion_anterior_fila
                columna = self.posicion_anterior_columna  
                casilla_a_comparar = int(str(fila) + str(columna))
                limite = 0
                for x in range(fila-1,fila+2):
                    for y in range(columna-1,columna+2):
                                
                        if x >= 0 and x <= 7:
                            if y >= 0 and y <= 7:
                                combinacion = int(str(x)+str(y))
                                if casilla_a_comparar != combinacion:
                                    if self.bando == "B":
                                        p = gridd.get_Tablero(x,y) 
                                        if gridd.get_Tablero(x,y) != 0 and p[0] == "B":
                                        
                                            limite += 1
                                        if gridd.get_Tablero(x,y) != 0:
                                        
                                            if p[0] == "N":
                                                rey_aux = Rey(self.bando,self.pieza,self.posicion_anterior_fila,self.posicion_anterior_columna,x,y)
                                                rey_aux.restricciones(x,y)
                                                                            
                                                if rey_aux.Index_jaque >= 1:
                                               
                                                    limite += 1
                                            
                                        elif gridd.get_Tablero(x,y) == 0:
                                            rey_aux = Rey(self.bando,self.pieza,self.posicion_anterior_fila,self.posicion_anterior_columna,x,y)           
                                            rey_aux.restricciones(x,y)
                                            
                                                                        
                                            if rey_aux.Index_jaque >= 1:
                                  
                                                limite += 1
                                                
                                    if self.bando == "N":
                                        p = gridd.get_Tablero(x,y) 
                                        if gridd.get_Tablero(x,y) != 0 and p[0] == "N":
                                    
                                            limite += 1

                                        if gridd.get_Tablero(x,y) != 0:
                                            if p[0] == "B":
                                                rey_aux = Rey(self.bando,self.pieza,self.posicion_anterior_fila,self.posicion_anterior_columna,x,y)
                                                rey_aux.restricciones(x,y)
                                                                            
                                                if rey_aux.Index_jaque >= 1:
                                         
                                                    limite += 1

                                        elif gridd.get_Tablero(x,y) == 0:
                                            rey_aux = Rey(self.bando,self.pieza,self.posicion_anterior_fila,self.posicion_anterior_columna,x,y)
                                            rey_aux.restricciones(x,y)
                                                                      
                                            if Rey.Index_jaque >= 1:
                              
                                                limite += 1
                            else: 
                                limite += 1
                        else: 
                            limite += 1

                if limite == 8:
                    print("Jaque mate.")
                    return True
      
   
