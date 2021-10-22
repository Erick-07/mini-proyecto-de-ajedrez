
"""
Derecha

43 + (1*x)

if fila_actual ==  fila_destino y la columna actual es menor que la columna destino


Abajo

43 - (10*x)

if fila_actual !=  fila_destino(arriba la fila actual es mayor que la fila destino) y las columnas son iguales

izquierda

43 - (1*x)

if fila_actual ==  fila_destino y la columna actual es mayor que la columna destino


Arriba

43 + (10*x)

if fila_actual !=  fila_destino(arriba la fila actual es menor que la fila destino) y las columnas son iguales

"""



import grig_general
import Rey

gridd = grig_general.gridd


class torre():
    #esas posiciones deben de ser en enteros
    def __init__(self, bando,pieza,posicion_anterior_fila, posicion_anterior_columna, posicion_destino_fila, posicion_destino_columna):
        self.bando = bando #str
        self.pieza = pieza #str
        self.posicion_anterior_fila = posicion_anterior_fila #int
        self.posicion_anterior_columna = posicion_anterior_columna  #int
        self.posicion_destino_fila = posicion_destino_fila #int 
        self.posicion_destino_columna = posicion_destino_columna #int
 
    def movimiento(self,rey):
        if self.bando == "B":
            casilla_actual = str(self.posicion_anterior_fila)+str(self.posicion_anterior_columna)
            casilla_destino = str(self.posicion_destino_fila)+str(self.posicion_destino_columna)
            cuenta = 0
            enable = True
            x = abs(int(casilla_actual) - int(casilla_destino))
            print(x)

            #Derecha
            if casilla_actual[0] == casilla_destino[0] and casilla_actual[1] < casilla_destino[1]:
                print("Torre moviendose a la derecha, TEST.")
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
                        enable_aux = True
                        while enable_aux:
                            

                            print(gridd.printeo())
                            pieza_a_guardar = gridd.get_Tablero(self.posicion_destino_fila,self.posicion_destino_columna)
                            grig_general.gridd = gridd.set_Tablero(self.posicion_destino_fila,self.posicion_destino_columna,self.bando+self.pieza+str(self.posicion_destino_fila)+str(self.posicion_destino_columna))
                            grig_general.gridd = gridd.set_Tablero(self.posicion_anterior_fila,self.posicion_anterior_columna,0)
                            rey.restricciones(rey.posicion_destino_fila,rey.posicion_destino_columna)
                            
                            if rey.Index_jaque >= 1:
                                grig_general.gridd = gridd.set_Tablero(self.posicion_destino_fila,self.posicion_destino_columna,pieza_a_guardar)
                                grig_general.gridd = gridd.set_Tablero(self.posicion_anterior_fila,self.posicion_anterior_columna,self.bando+self.pieza+str(self.posicion_anterior_fila)+str(self.posicion_anterior_columna))
                                print("Rey en jaque.")
                                enable_aux = False
                                return False
                            else:
                                enable_aux = False
                                print(gridd.printeo())
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
                    print(gridd.get_Tablero(fila,columna))
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
                        enable_aux = True
                        while enable_aux:
                            

                            print(gridd.printeo())
                            pieza_a_guardar = gridd.get_Tablero(self.posicion_destino_fila,self.posicion_destino_columna)
                            grig_general.gridd = gridd.set_Tablero(self.posicion_destino_fila,self.posicion_destino_columna,self.bando+self.pieza+str(self.posicion_destino_fila)+str(self.posicion_destino_columna))
                            grig_general.gridd = gridd.set_Tablero(self.posicion_anterior_fila,self.posicion_anterior_columna,0)
                            rey.restricciones(rey.posicion_destino_fila,rey.posicion_destino_columna)
                            if rey.Index_jaque >= 1:
                                grig_general.gridd = gridd.set_Tablero(self.posicion_destino_fila,self.posicion_destino_columna,pieza_a_guardar)
                                grig_general.gridd = gridd.set_Tablero(self.posicion_anterior_fila,self.posicion_anterior_columna,self.bando+self.pieza+str(self.posicion_anterior_fila)+str(self.posicion_anterior_columna))
                                print("Rey en jaque.")
                                enable_aux = False
                                return False
                            else:
                                enable_aux = False
                                print(gridd.printeo())
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
                        enable_aux = True
                        while enable_aux:
                            

                            print(gridd.printeo())
                            pieza_a_guardar = gridd.get_Tablero(self.posicion_destino_fila,self.posicion_destino_columna)
                            grig_general.gridd = gridd.set_Tablero(self.posicion_destino_fila,self.posicion_destino_columna,self.bando+self.pieza+str(self.posicion_destino_fila)+str(self.posicion_destino_columna))
                            grig_general.gridd = gridd.set_Tablero(self.posicion_anterior_fila,self.posicion_anterior_columna,0)
                            rey.restricciones(rey.posicion_destino_fila,rey.posicion_destino_columna)
                            if rey.Index_jaque >= 1:
                                grig_general.gridd = gridd.set_Tablero(self.posicion_destino_fila,self.posicion_destino_columna,pieza_a_guardar)
                                grig_general.gridd = gridd.set_Tablero(self.posicion_anterior_fila,self.posicion_anterior_columna,self.bando+self.pieza+str(self.posicion_anterior_fila)+str(self.posicion_anterior_columna))
                                print("Rey en jaque.")
                                enable_aux = False
                                return False
                            else:
                                enable_aux = False
                                print(gridd.printeo())
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
                        enable_aux = True
                        while enable_aux:
                            

                            print(gridd.printeo())
                            pieza_a_guardar = gridd.get_Tablero(self.posicion_destino_fila,self.posicion_destino_columna)
                            grig_general.gridd = gridd.set_Tablero(self.posicion_destino_fila,self.posicion_destino_columna,self.bando+self.pieza+str(self.posicion_destino_fila)+str(self.posicion_destino_columna))
                            grig_general.gridd = gridd.set_Tablero(self.posicion_anterior_fila,self.posicion_anterior_columna,0)
                            rey.restricciones(rey.posicion_destino_fila,rey.posicion_destino_columna)
                            if rey.Index_jaque >= 1:
                                grig_general.gridd = gridd.set_Tablero(self.posicion_destino_fila,self.posicion_destino_columna,pieza_a_guardar)
                                grig_general.gridd = gridd.set_Tablero(self.posicion_anterior_fila,self.posicion_anterior_columna,self.bando+self.pieza+str(self.posicion_anterior_fila)+str(self.posicion_anterior_columna))
                                print("Rey en jaque.")
                                enable_aux = False
                                return False
                            else:
                                enable_aux = False
                                print(gridd.printeo())
                                print("Moviemiento valido.")
                                return True

        elif self.bando == "N":
            casilla_actual = str(self.posicion_anterior_fila)+str(self.posicion_anterior_columna)
            casilla_destino = str(self.posicion_destino_fila)+str(self.posicion_destino_columna)
            cuenta = 0
            enable = True
            x = abs(int(casilla_actual) - int(casilla_destino))
            print(x)

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
                        enable_aux = True
                        while enable_aux:
                            

                            print(gridd.printeo())
                            pieza_a_guardar = gridd.get_Tablero(self.posicion_destino_fila,self.posicion_destino_columna)
                            grig_general.gridd = gridd.set_Tablero(self.posicion_destino_fila,self.posicion_destino_columna,self.bando+self.pieza+str(self.posicion_destino_fila)+str(self.posicion_destino_columna))
                            grig_general.gridd = gridd.set_Tablero(self.posicion_anterior_fila,self.posicion_anterior_columna,0)
                            rey.restricciones(rey.posicion_destino_fila,rey.posicion_destino_columna)
                            if rey.Index_jaque >= 1:
                                grig_general.gridd = gridd.set_Tablero(self.posicion_destino_fila,self.posicion_destino_columna,pieza_a_guardar)
                                grig_general.gridd = gridd.set_Tablero(self.posicion_anterior_fila,self.posicion_anterior_columna,self.bando+self.pieza+str(self.posicion_anterior_fila)+str(self.posicion_anterior_columna))
                                print("Rey en jaque.")
                                enable_aux = False
                                return False
                            else:
                                enable_aux = False
                                print(gridd.printeo())
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
                        enable_aux = True
                        while enable_aux:
                            

                            print(gridd.printeo())
                            pieza_a_guardar = gridd.get_Tablero(self.posicion_destino_fila,self.posicion_destino_columna)
                            grig_general.gridd = gridd.set_Tablero(self.posicion_destino_fila,self.posicion_destino_columna,self.bando+self.pieza+str(self.posicion_destino_fila)+str(self.posicion_destino_columna))
                            grig_general.gridd = gridd.set_Tablero(self.posicion_anterior_fila,self.posicion_anterior_columna,0)
                            
                            rey.restricciones(rey.posicion_destino_fila,rey.posicion_destino_columna)
                            if rey.Index_jaque >= 1:
                                grig_general.gridd = gridd.set_Tablero(self.posicion_destino_fila,self.posicion_destino_columna,pieza_a_guardar)
                                grig_general.gridd = gridd.set_Tablero(self.posicion_anterior_fila,self.posicion_anterior_columna,self.bando+self.pieza+str(self.posicion_anterior_fila)+str(self.posicion_anterior_columna))
                                print("Rey en jaque.")
                                enable_aux = False
                                return False
                            else:
                                enable_aux = False
                                print(gridd.printeo())
                                print("Moviemiento valido.")
                                return True

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
                        enable_aux = True
                        while enable_aux:
                            

                            print(gridd.printeo())
                            pieza_a_guardar = gridd.get_Tablero(self.posicion_destino_fila,self.posicion_destino_columna)
                            grig_general.gridd = gridd.set_Tablero(self.posicion_destino_fila,self.posicion_destino_columna,self.bando+self.pieza+str(self.posicion_destino_fila)+str(self.posicion_destino_columna))
                            grig_general.gridd = gridd.set_Tablero(self.posicion_anterior_fila,self.posicion_anterior_columna,0)
                            
                            rey.restricciones(rey.posicion_destino_fila,rey.posicion_destino_columna)
                            if rey.Index_jaque >= 1:
                                grig_general.gridd = gridd.set_Tablero(self.posicion_destino_fila,self.posicion_destino_columna,pieza_a_guardar)
                                grig_general.gridd = gridd.set_Tablero(self.posicion_anterior_fila,self.posicion_anterior_columna,self.bando+self.pieza+str(self.posicion_anterior_fila)+str(self.posicion_anterior_columna))
                                print("Rey en jaque.")
                                enable_aux = False
                                return False
                            else:
                                enable_aux = False
                                print(gridd.printeo())
                                print("Moviemiento valido.")
                                return True

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
                        enable_aux = True
                        while enable_aux:
                            

                            print(gridd.printeo())
                            pieza_a_guardar = gridd.get_Tablero(self.posicion_destino_fila,self.posicion_destino_columna)
                            grig_general.gridd = gridd.set_Tablero(self.posicion_destino_fila,self.posicion_destino_columna,self.bando+self.pieza+str(self.posicion_destino_fila)+str(self.posicion_destino_columna))
                            grig_general.gridd = gridd.set_Tablero(self.posicion_anterior_fila,self.posicion_anterior_columna,0)
                            
                            rey.restricciones(rey.posicion_destino_fila,rey.posicion_destino_columna)
                            if rey.Index_jaque >= 1:
                                grig_general.gridd = gridd.set_Tablero(self.posicion_destino_fila,self.posicion_destino_columna,pieza_a_guardar)
                                grig_general.gridd = gridd.set_Tablero(self.posicion_anterior_fila,self.posicion_anterior_columna,self.bando+self.pieza+str(self.posicion_anterior_fila)+str(self.posicion_anterior_columna))
                                print("Rey en jaque.")
                                enable_aux = False
                                return False
                            else:
                                enable_aux = False
                                print(gridd.printeo())
                                print("Moviemiento valido.")
                                return True
                                
