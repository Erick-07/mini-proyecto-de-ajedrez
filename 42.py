#Esta logica  no logra evitar errores como cual pieza analizo 
#esa logica va antes

import grig_general

gridd = grig_general.gridd

#gridd.set_Tablero(1,0,"BP10")


#Antes de salir De esta clase se debera de asegurar si el rey no se encuentre en jaque 
#si esta en jaque invalid move 
#try again

#Antes de esta clase se debera de comprabar si una pieza esta en su casilla

class peon():
    #esas posiciones deben de ser en enteros
    listaN = ["20","21","22","23","24","25","26","27"]
    listaB = ["50","51","52","53","54","55","56","57"]
    registro = {"20":[],"21":[],"22":[],"23":[],"24":[],"25":[],"26":[],"27":[],"50":[],"51":[],"52":[],"53":[],"54":[],"55":[],"56":[],"57":[]}

    def __init__(self, bando,color,posicion_anterior_fila, posicion_anterior_columna, posicion_destino_fila, posicion_destino_columna):
        self.bando = bando #str
        self.color = color #str
        self.posicion_anterior_fila = posicion_anterior_fila #int
        self.posicion_anterior_columna = posicion_anterior_columna  #int
        self.posicion_destino_fila = posicion_destino_fila #int 
        self.posicion_destino_columna = posicion_destino_columna #int
        

    #movimiento 
    
    def movimiento(self,rey):
        enable = False
        
        #Codigo para pieza peon blanca.
        #####################################
        if self.bando == "N":  
        #####################################
            cuenta = 0 
            #enable to move 2 row with move natural. 
            if self.posicion_anterior_fila == 1: 
                
                Pieza = gridd.get_Tablero(self.posicion_anterior_fila,self.posicion_anterior_columna)
                print(Pieza)
                Pieza= list(Pieza)
                Pieza[2] = str(self.posicion_destino_fila)
                Pieza[3] = str(self.posicion_destino_columna)
                Pieza = "".join(Pieza)
                print(Pieza)
                
                if self.posicion_anterior_fila - self.posicion_destino_fila == -2:
                    if self.posicion_destino_columna == self.posicion_anterior_columna:
                        for i in range(self.posicion_anterior_fila,self.posicion_destino_fila):
                     
                            if gridd.get_Tablero(i+1,self.posicion_anterior_columna) == 0:    
                                cuenta +=1

                        if cuenta == 2:
                            pieza_a_guardar = gridd.get_Tablero(self.posicion_destino_fila,self.posicion_destino_columna)
                            gridd.set_Tablero(self.posicion_destino_fila,self.posicion_destino_columna,str(Pieza[0])+str(Pieza[1])+str(Pieza[2])+str(Pieza[3])) 
                            gridd.set_Tablero(self.posicion_anterior_fila,self.posicion_anterior_columna,0)

                            rey.restricciones(rey.posicion_destino_fila,rey.posicion_destino_columna)
                            if rey.Index_jaque >= 1:
                                grig_general.gridd = gridd.set_Tablero(self.posicion_destino_fila,self.posicion_destino_columna,pieza_a_guardar)
                                grig_general.gridd = gridd.set_Tablero(self.posicion_anterior_fila,self.posicion_anterior_columna,self.bando+self.color+str(self.posicion_anterior_fila)+str(self.posicion_anterior_columna))
                                print("Movimiento invalido.")
                                return False
                             
                            if self.posicion_anterior_columna > 0 :
                                pieza_enemiga_izquierda = gridd.get_Tablero(self.posicion_destino_fila,self.posicion_destino_columna-1)
                     
                                if pieza_enemiga_izquierda is not -1 and pieza_enemiga_izquierda != 0:
                                    if pieza_enemiga_izquierda[0] == "N" and pieza_enemiga_izquierda[1] == "P":
                                        pieza_amiga = str(self.posicion_destino_fila-1)+str(self.posicion_destino_columna)
                                        peon.registro[pieza_amiga].append(pieza_enemiga_izquierda)
                                        print(peon.registro)
                                        

                            print(gridd.printeo())
                            
                            if self.posicion_anterior_columna < 7 :

                                pieza_enemiga_derecha = gridd.get_Tablero(self.posicion_destino_fila,self.posicion_destino_columna+1)
                                print(pieza_enemiga_derecha,"pieza derecha")
                                
                            
                                if pieza_enemiga_derecha is not -1 and pieza_enemiga_derecha != 0 and pieza_enemiga_derecha != 0:

                                    if  pieza_enemiga_derecha[0] == "N" and pieza_enemiga_derecha[1] == "P":
                                        pieza_amiga = str(self.posicion_destino_fila-1)+str(self.posicion_destino_columna)
                                        peon.registro[pieza_amiga].append(pieza_enemiga_derecha)
                                        print(peon.registro,"pieza")
                            return True

                        else:
                            print("Casilla ocupada")
                            return False

            #enable to move one row.

            if self.posicion_anterior_fila - self.posicion_destino_fila == -1 and self.posicion_anterior_columna == self.posicion_destino_columna:
                
                if gridd.get_Tablero(self.posicion_destino_fila,self.posicion_destino_columna) == 0:      
                    Pieza = gridd.get_Tablero(self.posicion_anterior_fila,self.posicion_anterior_columna)
                    Pieza= list(Pieza)
                    Pieza[2] = str(self.posicion_destino_fila)
                    Pieza[3] = str(self.posicion_destino_columna)
                    Pieza = "".join(Pieza)
                    print(Pieza)
                    
                    pieza_a_guardar = gridd.get_Tablero(self.posicion_destino_fila,self.posicion_destino_columna)
                    gridd.set_Tablero(self.posicion_destino_fila,self.posicion_destino_columna,str(Pieza[0])+str(Pieza[1])+str(Pieza[2])+str(Pieza[3])) 
                    gridd.set_Tablero(self.posicion_anterior_fila,self.posicion_anterior_columna,0)

                    rey.restricciones(rey.posicion_destino_fila,rey.posicion_destino_columna)
                    if rey.Index_jaque >= 1:
                            grig_general.gridd = gridd.set_Tablero(self.posicion_destino_fila,self.posicion_destino_columna,pieza_a_guardar)
                            grig_general.gridd = gridd.set_Tablero(self.posicion_anterior_fila,self.posicion_anterior_columna,self.bando+self.color+str(self.posicion_anterior_fila)+str(self.posicion_anterior_columna))
                            print("Rey en jaque.")
                             
                            return False
                    
                    else:
                        enable = True
                        print(enable, "Movimiento Valido mml.")
                        


                #este debe ser > 6 cuando se añadan mas filas
                #esto es para la coronacion
                if self.posicion_destino_fila > 6 :

                    Pieza = gridd.get_Tablero(self.posicion_destino_fila,self.posicion_destino_columna)
                    Pieza= list(Pieza)
                    cierre = True
                    items = ["D","C","A","T"]

                    while(cierre):
                        Pieza[1] = str(input("Seleccione D, C, A, T: "))
                        for i in range(0,len(items)):
                            if Pieza[1] is items[i]:
                                cierre = False
                        else:
                            print("Seleccione de nuevo y escribalo en mayúsculas.")     

                    Pieza = "".join(Pieza)
                    print(Pieza)
                    gridd.set_Tablero(self.posicion_destino_fila,self.posicion_destino_columna,str(Pieza[0])+str(Pieza[1])+str(Pieza[2])+str(Pieza[3])) 

                return enable

            #region //metodo para la capturacion al paso.   
            aux = True
            if peon.verificacion_captura_al_paso(self,rey):
                print("pieza capturada")
                print("hola")
                aux = False
                return True
            
            #endRegion

            #enable to kill someone.
            aux = True
            if peon.verificacion_peon(self,rey):
                print("Capturacion de peon")
                aux = False
                return True
  
            elif aux == True:
                print("Movimiento de captura no permitido.")
                return False

            

        #Codigo para pieza peon negro.
        if self.bando == "B":
                    
            cuenta = 0 
            # Region enable to move 2 row with move natural. 
            if self.posicion_anterior_fila == 6: 
                
                Pieza = gridd.get_Tablero(self.posicion_anterior_fila,self.posicion_anterior_columna)
                print(Pieza)
                Pieza= list(Pieza)
                Pieza[2] = str(self.posicion_destino_fila)
                Pieza[3] = str(self.posicion_destino_columna)
                Pieza = "".join(Pieza)
                print(Pieza)
                if self.posicion_anterior_fila - self.posicion_destino_fila == 2:
                    if self.posicion_destino_columna == self.posicion_anterior_columna:
                        for i in range(self.posicion_destino_fila,self.posicion_anterior_fila):
                            print(i)
                            if gridd.get_Tablero(i,self.posicion_anterior_columna) == 0:    
                                cuenta +=1
                            print(i)

                        if cuenta == 2:
                            
                            pieza_a_guardar = gridd.get_Tablero(self.posicion_destino_fila,self.posicion_destino_columna)
                            gridd.set_Tablero(self.posicion_destino_fila,self.posicion_destino_columna,str(Pieza[0])+str(Pieza[1])+str(Pieza[2])+str(Pieza[3])) 
                            gridd.set_Tablero(self.posicion_anterior_fila,self.posicion_anterior_columna,0)

                            rey.restricciones(rey.posicion_destino_fila,rey.posicion_destino_columna)
                            if rey.Index_jaque >= 1:
                                grig_general.gridd = gridd.set_Tablero(self.posicion_destino_fila,self.posicion_destino_columna,pieza_a_guardar)
                                grig_general.gridd = gridd.set_Tablero(self.posicion_anterior_fila,self.posicion_anterior_columna,self.bando+self.color+str(self.posicion_anterior_fila)+str(self.posicion_anterior_columna))
                                print("Movimiento invalido.")
                                return False

                            if self.posicion_anterior_columna > 0 :
                                pieza_enemiga_izquierda = gridd.get_Tablero(self.posicion_destino_fila,self.posicion_destino_columna-1)
                                print(pieza_enemiga_izquierda,"pieza izquierda")
                                if pieza_enemiga_izquierda is not -1 and pieza_enemiga_izquierda != 0:
                                    if pieza_enemiga_izquierda[1] == "P" and  pieza_enemiga_izquierda[0] == "B":
                                        pieza_amiga = str(self.posicion_destino_fila+1)+str(self.posicion_destino_columna)
                                        peon.registro[pieza_amiga].append(pieza_enemiga_izquierda)
                                        print(peon.registro)
                                 
                            print(enable,"Peon iniciando se movio dos casilla.")

                            if self.posicion_anterior_columna < 7 :

                                pieza_enemiga_derecha = gridd.get_Tablero(self.posicion_destino_fila,self.posicion_destino_columna+1)
                                print(pieza_enemiga_derecha,"pieza derecha")
                                
                            
                                if pieza_enemiga_derecha is not -1 and pieza_enemiga_derecha != 0 and pieza_enemiga_derecha != 0:

                                    if  pieza_enemiga_derecha[1] == "P" and pieza_enemiga_derecha[0] == "B":
                                        pieza_amiga = str(self.posicion_destino_fila+1)+str(self.posicion_destino_columna)
                                        peon.registro[pieza_amiga].append(pieza_enemiga_derecha)
                                        print(peon.registro,"Pieza,Pieza,Pieza,Pieza,Pieza,Pieza,")

          
                            return True

                        else:
                            print("Casilla ocupada")
                            return False
                #endRegion 

            if self.posicion_anterior_fila - self.posicion_destino_fila == 1 and self.posicion_anterior_columna == self.posicion_destino_columna:
                
                if gridd.get_Tablero(self.posicion_destino_fila,self.posicion_destino_columna) == 0:      
                    Pieza = gridd.get_Tablero(self.posicion_anterior_fila,self.posicion_anterior_columna)
                    Pieza= list(Pieza)
                    Pieza[2] = str(self.posicion_destino_fila)
                    Pieza[3] = str(self.posicion_destino_columna)
                    Pieza = "".join(Pieza)
                    print(Pieza)

                    pieza_a_guardar = gridd.get_Tablero(self.posicion_destino_fila,self.posicion_destino_columna)
                    gridd.set_Tablero(self.posicion_destino_fila,self.posicion_destino_columna,str(Pieza[0])+str(Pieza[1])+str(Pieza[2])+str(Pieza[3])) 
                    gridd.set_Tablero(self.posicion_anterior_fila,self.posicion_anterior_columna,0)

                    rey.restricciones(rey.posicion_destino_fila,rey.posicion_destino_columna)
                    if rey.Index_jaque >= 1:
                            grig_general.gridd = gridd.set_Tablero(self.posicion_destino_fila,self.posicion_destino_columna,pieza_a_guardar)
                            grig_general.gridd = gridd.set_Tablero(self.posicion_anterior_fila,self.posicion_anterior_columna,self.bando+self.color+str(self.posicion_anterior_fila)+str(self.posicion_anterior_columna))
                            print("Rey en jaque.")
                            enable = False
                            return False

                    enable = True
                    print(enable, "Movimiento Valido mml.")

                if self.posicion_destino_fila < 1:

                    Pieza = gridd.get_Tablero(self.posicion_destino_fila,self.posicion_destino_columna)
                    Pieza= list(Pieza)
                    cierre = True
                    items = ["D","C","A","T"]

                    while(cierre):
                        Pieza[1] = str(input("Seleccione D, C, A, T: "))
                        for i in range(0,len(items)):
                            if Pieza[1] is items[i]:
                                cierre = False
                        else:
                            print("Seleccione de nuevo y escribalo es mayusculas.")     

                    Pieza = "".join(Pieza)
                    print(Pieza)
                    gridd.set_Tablero(self.posicion_destino_fila,self.posicion_destino_columna,str(Pieza[0])+str(Pieza[1])+str(Pieza[2])+str(Pieza[3])) 


                return enable
            
            #enable to kill someone.
            aux = True
            if peon.verificacion_peon(self,rey):
                print("Capturacion de peon")
                aux = False
                return True
            """
                elif aux == True:
                    print("Movimiento de captura no permitido.")
                    return enable
            """        
            

            #region //metodo para la capturacion al paso.   
            if peon.verificacion_captura_al_paso(self,rey):
                print("pieza capturada")
                print("hola")
                return True
            else:
                print("Pieza noooooooooooooo encontrada")
                return False
            
            #endRegion


    #Esta clase verificara si las diagonales seleccionadas estan correcta, si hay un peon para capturar, o si no, no se movera.
    def verificacion_peon(self,rey):
       
        if self.bando == "N":
            
            #Verificacion de las diagonales, y direccion, pendiente de que no se mueva hacia atras.
                if (self.posicion_anterior_fila - self.posicion_destino_fila) == -1 and abs(self.posicion_anterior_columna - self.posicion_destino_columna) == 1:
                
                    if gridd.get_Tablero(self.posicion_destino_fila,self.posicion_destino_columna) != 0:
                        
                        Pieza = gridd.get_Tablero(self.posicion_destino_fila,self.posicion_destino_columna)
                        "Pieza 0, será El bando."
                        Bando = Pieza[0] 
                        "Indicar que seá peon."
                        Pieza_P = Pieza[1]     
                        Pieza_a_colocar = str(self.bando) + str(self.color) + str(self.posicion_destino_fila) + str(self.posicion_destino_columna)
                        #esto es para verificar si enverdad haya peon negro
                        if Bando == "N":
                            print("Capturado")

                            gridd.set_Tablero(self.posicion_anterior_fila,self.posicion_anterior_columna,0)
                            gridd.set_Tablero(self.posicion_destino_fila,self.posicion_destino_columna, Pieza_a_colocar[0]+Pieza_a_colocar[1]+Pieza_a_colocar[2]+Pieza_a_colocar[3])
                            print(gridd.printeo())
                            
                            return True
        #Verificacion de la comprobacion es desde N a B. 
        elif self.bando == "B":
             if (self.posicion_anterior_fila - self.posicion_destino_fila) == 1 and abs(self.posicion_anterior_columna - self.posicion_destino_columna) == 1:
               
                if gridd.get_Tablero(self.posicion_destino_fila,self.posicion_destino_columna) != 0:
                    
                    Pieza = gridd.get_Tablero(self.posicion_destino_fila,self.posicion_destino_columna)
                    "Pieza 0, será El bando."
                    Bando = Pieza[0] 
                    "Indicar que seá peon."
                    Pieza_P = Pieza[1]     
                    Pieza_a_colocar = str(self.bando) + str(self.color) + str(self.posicion_destino_fila) + str(self.posicion_destino_columna)
                    #esto es para verificar si enverdad haya peon negro
                    if Bando == "B":
                        print("Capturado")
                        gridd.set_Tablero(self.posicion_anterior_fila,self.posicion_anterior_columna,0)
                        gridd.set_Tablero(self.posicion_destino_fila,self.posicion_destino_columna, Pieza_a_colocar[0]+Pieza_a_colocar[1]+Pieza_a_colocar[2]+Pieza_a_colocar[3])
                        print(gridd.printeo())
                        
                        return True
            
        return False

    #Añadido
    def Borrado_de_registro(self):
        if self.bando == "B":

            for i in range(0,len(peon.registro)):
                for s in range(0, len(peon.listaB)):
                  
                    if peon.listaB[s] in peon.registro.keys():
                        if peon.registro[peon.listaB[s]] != []:
                            peon.registro.pop(peon.listaB[s])
                            print(peon.registro)
        elif self.bando == "N":
            for i in range(0,len(peon.registro)):
                for s in range(0, len(peon.listaN)):
               
                    if peon.listaN[s] in peon.registro.keys():
                        if peon.registro[peon.listaN[s]] != []:
                            peon.registro.pop(peon.listaN[s])
                            print(peon.registro)

    #Añadido
    def verificacion_captura_al_paso(self,rey):
        #primero como la clase no se rompe al tomar una pieza y ponerlo en un valor cero
        casilla = str(self.posicion_destino_fila) + str(self.posicion_destino_columna)
        Pieza_enemiga = str(self.bando) + str(self.color) + str(self.posicion_anterior_fila) + str(self.posicion_anterior_columna) 
        Pieza = gridd.get_Tablero(self.posicion_anterior_fila,self.posicion_anterior_columna)
        Pieza= list(Pieza)
        Pieza[2] = str(self.posicion_destino_fila)
        Pieza[3] = str(self.posicion_destino_columna)
        Pieza = "".join(Pieza)
        print(Pieza)
        if casilla in peon.registro:
            if Pieza_enemiga in peon.registro.get(casilla):
              
                if self.bando == "N":
                    print(gridd.printeo())
               
                    rey.restricciones(rey.posicion_destino_fila,rey.posicion_destino_columna)
                    if rey.Index_jaque >= 1:
                        print("Rey en jaque.")
                        return False
                    else:
                        print("Moviemiento valido.")
                        gridd.set_Tablero(self.posicion_destino_fila,self.posicion_destino_columna, str(Pieza))
                        #esto es en caso blanco 
                        gridd.set_Tablero(self.posicion_destino_fila-1,self.posicion_destino_columna,0)
                        gridd.set_Tablero(self.posicion_anterior_fila,self.posicion_anterior_columna,0)
                        print("Pieza capturada al paso")
                        return True


                if self.bando == "B":
                    
                    print(gridd.printeo())
               
                    rey.restricciones(rey.posicion_destino_fila,rey.posicion_destino_columna)
                    if rey.Index_jaque >= 1:
                        print("Rey en jaque.")
                        return False
                    else:
                        print("Moviemiento valido.")
                        gridd.set_Tablero(self.posicion_destino_fila,self.posicion_destino_columna, str(Pieza))
                        #esto es en caso blanco 
                        gridd.set_Tablero(self.posicion_destino_fila-1,self.posicion_destino_columna,0)
                        gridd.set_Tablero(self.posicion_anterior_fila,self.posicion_anterior_columna,0)
                        print("Pieza capturada al paso")
                        return True

                    

                return True
            else:
                print("Pieza no encontrada")
                return False
        else:
            print("Casilla no existente.")
            return False
 