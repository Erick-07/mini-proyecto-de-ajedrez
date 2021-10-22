"""
Una comprobación que descubri con el caballo para comprobar si su movimiento es valido o no, es que si restas la 
coordenada en que esta el caballo posicionado menos la casilla que quisiera ocupar y esa resta la haremos tomando el valor absoluto de la misma, da como resultado 
la constantes de 4 numeros. Las cuales son 21, 19, 12, 8, lo cual lo he almacenado en una lista para comprobarlos ej:

Si el caballo estuviera en la casilla 3,3 si restas ese valor a la casilla destino que quieres colocar ese caballo por ejemplo, la 
casilla 5,2 y hacemos la operacion: 52 - 33 = 19 tal y como el de la lista. Si colocamos casillas invalidas o movimientos erroneos
saldra un resultado fuera de estos 4 numeros, ejemplo: 53 (La casilla destino) - 33 (Casilla del caballo) = 20 

Otros ejemplos con las otras casillas disponibles con la 33:

|54-33|= 21
|52-33|= 19
|41-33|= 8
|21-33|= 12
|12-33|= 21
|14-33|= 19
|25-33|= 8
"""

import grig_general

gridd = grig_general.gridd

class caballo():

    lista_index = [21,19,12,8]

    #esas posiciones deben de ser en enteros
    def __init__(self, bando,pieza,posicion_anterior_fila, posicion_anterior_columna, posicion_destino_fila, posicion_destino_columna):
        self.bando = bando #str
        self.pieza = pieza #str
        self.posicion_anterior_fila = posicion_anterior_fila #int
        self.posicion_anterior_columna = posicion_anterior_columna  #int
        self.posicion_destino_fila = posicion_destino_fila #int 
        self.posicion_destino_columna = posicion_destino_columna #int
        

    def movimiento(self,rey):
        if self.bando == "B" and self.pieza == "C":
            
            casilla_actual = str(self.posicion_anterior_fila) + str(self.posicion_anterior_columna)
            casilla_destino = str(self.posicion_destino_fila) + str(self.posicion_destino_columna)
            casilla_actual = int(casilla_actual)
            casilla_destino = int(casilla_destino)
            resultado = abs(casilla_actual-casilla_destino)
            casilla_a_ocupar = gridd.get_Tablero(self.posicion_destino_fila,self.posicion_destino_columna)

            aux = str(casilla_a_ocupar)
            if casilla_a_ocupar != 0 and aux[0] == "B":
                print("Casilla ocupada para el caballo.") 

            else:
                for i in  range(0,len(caballo.lista_index)):
                    if resultado == caballo.lista_index[i]:
                        print(gridd.printeo())
                        pieza_a_guardar = gridd.get_Tablero(self.posicion_destino_fila,self.posicion_destino_columna)
                        grig_general.gridd = gridd.set_Tablero(self.posicion_destino_fila,self.posicion_destino_columna,str(self.bando)+str(self.pieza)+str(self.posicion_destino_fila)+str(self.posicion_destino_columna))
                        grig_general.gridd = gridd.set_Tablero(self.posicion_anterior_fila,self.posicion_anterior_columna,0)

                        rey.restricciones(rey.posicion_destino_fila,rey.posicion_destino_columna)
                        if rey.Index_jaque >= 1:
                            grig_general.gridd = gridd.set_Tablero(self.posicion_destino_fila,self.posicion_destino_columna,pieza_a_guardar)
                            grig_general.gridd = gridd.set_Tablero(self.posicion_anterior_fila,self.posicion_anterior_columna,self.bando+self.pieza+str(self.posicion_anterior_fila)+str(self.posicion_anterior_columna))
                            print("Rey en jaque.")
                            return False
                        else:
                            print("Moviemiento valido.")
                            return True
            


        elif self.bando == "N" and self.pieza == "C":
            casilla_actual = str(self.posicion_anterior_fila) + str(self.posicion_anterior_columna)
            casilla_destino = str(self.posicion_destino_fila) + str(self.posicion_destino_columna)
            casilla_actual = int(casilla_actual)
            casilla_destino = int(casilla_destino)
            resultado = abs(casilla_actual-casilla_destino)
            casilla_a_ocupar = gridd.get_Tablero(self.posicion_destino_fila,self.posicion_destino_columna)
            
            aux = str(casilla_a_ocupar)
            if casilla_a_ocupar != 0 and aux[0] == "N":
                print("Casilla ocupada para el caballo.") 
                
            else:
                for i in  range(0,len(caballo.lista_index)):
                    if resultado == caballo.lista_index[i]:
                        print("encontrado")
 
                        print(gridd.printeo())
                        pieza_a_guardar = gridd.get_Tablero(self.posicion_destino_fila,self.posicion_destino_columna)
                        grig_general.gridd = gridd.set_Tablero(self.posicion_destino_fila,self.posicion_destino_columna,str(self.bando)+str(self.pieza)+str(self.posicion_destino_fila)+str(self.posicion_destino_columna))
                        grig_general.gridd = gridd.set_Tablero(self.posicion_anterior_fila,self.posicion_anterior_columna,0)

                        rey.restricciones(rey.posicion_destino_fila,rey.posicion_destino_columna)
                        if rey.Index_jaque >= 1:
                            grig_general.gridd = gridd.set_Tablero(self.posicion_destino_fila,self.posicion_destino_columna,pieza_a_guardar)
                            grig_general.gridd = gridd.set_Tablero(self.posicion_anterior_fila,self.posicion_anterior_columna,self.bando+self.pieza+str(self.posicion_anterior_fila)+str(self.posicion_anterior_columna))
                            print("Rey en jaque.")
                            return False
                        else:
                            print("Moviemiento valido.")
                            return True
                        


