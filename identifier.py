import Alfil
import Peon
import grig_general
import caballo
import Torre
import Dama
import Rey
 

grid = grig_general.gridd

p0 = Peon.peon("B","P",1,0,None,None)
p1 = Peon.peon("B","P",1,1,None,None)
p2 = Peon.peon("B","P",1,2,None,None)
p3 = Peon.peon("B","P",1,3,None,None)
p4 = Peon.peon("B","P",1,4,None,None)
p5 = Peon.peon("B","P",1,5,None,None)
p6 = Peon.peon("B","P",1,6,None,None)
p7 = Peon.peon("B","P",1,7,None,None)

t0 = Torre.torre("B","T",0,0,None,None)
t1 = Torre.torre("B","T",0,7,None,None)

c0 = caballo.caballo("B","C",0,1,None,None)
c1 = caballo.caballo("B","C",0,6,None,None)

a0 = Alfil.alfill("B","A",0,2,None,None)
a1 = Alfil.alfill("B","A",0,5,None,None)

d0 = Dama.Dama("B","D",0,3,None,None)

r0 = Rey.Rey("B","R",0,4,0,4)

p8 = Peon.peon("N","P",6,0,None,None)
p9 = Peon.peon("N","P",6,1,None,None)
p10 = Peon.peon("N","P",6,2,None,None)
p11 = Peon.peon("N","P",6,3,None,None)
p12 = Peon.peon("N","P",6,4,None,None)
p13 = Peon.peon("N","P",6,5,None,None)
p14 = Peon.peon("N","P",6,6,None,None)
p15 = Peon.peon("N","P",6,7,None,None)

t2 = Torre.torre("N","T",7,0,None,None)
t3 = Torre.torre("N","T",7,7,None,None)

c2 = caballo.caballo("N","C",7,1,None,None)
c3 = caballo.caballo("N","C",7,6,None,None)

a2 = Alfil.alfill("N","A",7,2,None,None)
a3 = Alfil.alfill("N","A",7,5,None,None)

d1 = Dama.Dama("N","D",7,3,None,None)

r1 = Rey.Rey("N","R",7,4,7,4)


Lista = [p0,p1,p2,p3,p4,p5,p6,p7,
         p8,p9,p10,p11,p12,p13,p14,p15,
         c0,c1,c2,c3,
         t0,t1,t2,t3,
         a0,a1,a2,a3,
         d0,d1,
         r0,r1
         ]

 


class ID:
 
    def verification(turn,start,target): 
    
        variable = ID.modify(target[0],target[1],start[0],start[1])
        
        if variable:
            if turn == "B" and variable.bando == "B":
                if variable.pieza != "R" :    
                    if variable.movimiento(r0):
                        if variable.pieza == "P" and Peon.peon.change_role != "P":

                            if Peon.peon.change_role == "D":
                                Lista.append(Dama.Dama("B","D",target[0],target[1],None,None))
                            elif Peon.peon.change_role == "A":
                                Lista.append(Alfil.alfill("B","A",target[0],target[1],None,None))
                            elif Peon.peon.change_role == "C":
                                Lista.append(caballo.caballo("B","C",target[0],target[1],None,None))
                            elif Peon.peon.change_role == "T":
                                Lista.append(Torre.torre("B","T",target[0],target[1],None,None))
                                
                            Peon.peon.change_role = "P"
                        variable.posicion_anterior_fila = target[0]
                        variable.posicion_anterior_columna = target[1]
                        enemy_piece = grid.get_Tablero(target[0],target[1])
                        if enemy_piece != 0 and enemy_piece[0] == "N":
                            ID.remove(enemy_piece)
                        return True
                    else:
                        return False
                else:
                    if variable.movimiento(target[0],target[1]):
                        variable.posicion_anterior_fila = target[0]
                        variable.posicion_anterior_columna = target[1]
                        enemy_piece = grid.get_Tablero(target[0],target[1])
                        if enemy_piece != 0 and enemy_piece[0] == "N":
                            ID.remove(enemy_piece)
                        return True
                    
            elif turn == "N" and variable.bando == "N":
                if variable.pieza != "R":    
                    if variable.movimiento(r1):
                        if variable.pieza == "P" and Peon.peon.change_role != "P":
                            
                            if Peon.peon.change_role == "D":
                                Lista.append(Dama.Dama("N","D",target[0],target[1],None,None))
                            elif Peon.peon.change_role == "A":
                                Lista.append(Alfil.alfill("N","A",target[0],target[1],None,None))
                            elif Peon.peon.change_role == "C":
                                Lista.append(caballo.caballo("N","C",target[0],target[1],None,None))
                            elif Peon.peon.change_role == "T":
                                Lista.append(Torre.torre("N","T",target[0],target[1],None,None))
                            Peon.peon.change_role = "P"

                        variable.posicion_anterior_fila = target[0]
                        variable.posicion_anterior_columna = target[1]
                        enemy_piece = grid.get_Tablero(target[0],target[1])
                        if enemy_piece != 0 and enemy_piece[0] == "B":
                            ID.remove(enemy_piece)
                        return True
                    else:
                        return False    
                if variable.movimiento(target[0],target[1]):
                        variable.posicion_anterior_fila = target[0]
                        variable.posicion_anterior_columna = target[1]
                        enemy_piece = grid.get_Tablero(target[0],target[1])
                        if enemy_piece != 0 and enemy_piece[0] == "B":
                            ID.remove(enemy_piece)
                        return True       
              
            return False

    def select_the_object(x,y):
        piece = grid.get_Tablero(x,y)
        
        for i in range(0,len(Lista)):
            E_P = Lista[i]
            if piece == E_P.bando+E_P.pieza+str(E_P.posicion_anterior_fila)+str(E_P.posicion_anterior_columna):  
                return Lista[i]

    def remove(object):
        for i in range(0,len(Lista)):
            E_P = Lista[i]
            if object == E_P.bando+E_P.pieza+str(E_P.posicion_destino_fila)+str(E_P.posicion_destino_columna):
                Lista.pop(i)
                break

    def modify(x,y,x_b,y_b):
        variable = ID.select_the_object(x_b,y_b)
        if variable:
            variable.posicion_destino_fila = x
            variable.posicion_destino_columna = y
            return variable
        else:
            return False 
    def verify_checks(turn):

        if turn == "B":
            if r0.restricciones(r0.posicion_anterior_fila,r0.posicion_anterior_columna):
                if r0.Index_jaque >= 1:
                    if r0.jaque_mate():
                        return 2   
                    else:
                        return 1
            else:
                return False
        else:
            if r1.restricciones(r1.posicion_anterior_fila,r1.posicion_anterior_columna):
                if r1.Index_jaque >= 1:
                    if r1.jaque_mate():
                        return 2   
                    else:
                        return 1
            else:
                return False
                
    
    

    





