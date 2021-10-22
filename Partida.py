
import Alfil
import Peon
import grig_general
import caballo
import Torre
import Dama
import Rey

grid = grig_general.gridd
pieza = grid
disponibilildad = True

fila_ant_reyB = 0
columna_ant_reyB = 4
fila_reyB = 0
columna_reyB = 4

fila_ant_reyN = 7
columan_ant_reyN = 4
fila_reyN = 7
columan_reyN = 4

print((grig_general.gridd),"this")
 
 

while disponibilildad:
    print(grid.g())
    turno = "B"
    #turno blanco
    while turno == "B":
        reyB = Rey.Rey("B","R",fila_reyB,columna_reyB,fila_reyB,columna_reyB)
        if reyB.restricciones(fila_reyB,columna_reyB):
            if reyB.Index_jaque >= 1:
                if reyB.jaque_mate():
                    turno = "NO"
                    disponibilildad = False
                    print("Game over, ganan las negras.")
                    break
        else:
            print("No hay jaque")            
 
        repeat = True
        while repeat:
            try:
                fila = int(input("Elija su pieza en filaB: "))
                columna = int(input("Elija su pieza en columnaB: "))
                if (fila <= 7 and fila >= 0) and (columna <= 7 and columna >= 0):

                    repeat = False
            except:
                print("El caracter no es numerico.")
                
 
        
        
        pieza = grid.get_Tablero(fila,columna)
       
        
        if pieza != 0:  
            if pieza[0] == "B":
                peon = Peon.peon("B","P",None,None,None,None)
                peon.Borrado_de_registro()
                    
                if pieza[1] == "P":
                    print(pieza)
                    repeat = True
                    while repeat:
                        try:
                            fila_destino = int(input("Elija su movimiento en fila: "))
                            columna_destino = int(input("Elija su movimiento en columna: "))
                            if (fila <= 7 and fila >= 0) and (columna <= 7 and columna >= 0):

                                repeat = False
                        except:
                            print("El caracter no es numerico.")

                    
                    peon = Peon.peon("B","P",fila,columna,fila_destino,columna_destino)
                    if peon.movimiento(reyB):
                        print()
                        print()
                        print("Turno De las negras")
                        print(grid.g())
                        turno = "N"
                    else:
                        print("Elija bien la fila y la columna nuevamente.")

                elif pieza[1] == "T":
                    print(pieza)
                    repeat = True
                    while repeat:
                        try:
                            fila_destino = int(input("Elija su movimiento en fila: "))
                            columan_destino = int(input("Elija su movimiento en columna: "))
                            if (fila_destino <= 7 and fila_destino >= 0) and (columan_destino <= 7 and columan_destino >= 0):

                                repeat = False
                        except:
                            print("El caracter no es numerico.")
                    Tower = Torre.torre("B","T",fila,columna,fila_destino,columan_destino)
                    if Tower.movimiento(reyB):
                        print()
                        print()
                        print("Movimiento Valido")
                        turno = "N"
                        print(grid.printeo())
                    else:
                        print()
                        print()
                        print("Verifique su movimiento o si su rey esta en jaque")
                        print(grid.printeo())
                        
                elif pieza[1] == "C":
                    print(pieza)
                    repeat = True
                    while repeat:

                        try:
                            fila_destino = int(input("Elija su movimiento en fila: "))
                            columan_destino = int(input("Elija su movimiento en columna: "))
                            if (fila_destino <= 7 and fila_destino >= 0) and (columan_destino <= 7 and columan_destino >= 0):

                                repeat = False
                        except:
                            print("El caracter no es numerico.")

                    Caballo = caballo.caballo("B","C",fila,columna,fila_destino,columan_destino)
                    if Caballo.movimiento(reyB):
                        print()
                        print()
                        print("Movimiento valido")
                        turno = "N"
                        print(grid.printeo())
                    else:
                        print()
                        print()
                        print("Elija bien la fila y la columna nuevamente.")                        
                        print(grid.printeo())

                elif pieza[1] == "A":
                    print(pieza)
                    repeat = True
                    while repeat:
                        try:
                            fila_destino = int(input("Elija su movimiento en fila: "))
                            columan_destino = int(input("Elija su movimiento en columna: "))
                            if (fila_destino <= 7 and fila_destino >= 0) and (columan_destino <= 7 and columan_destino >= 0):

                                repeat = False
                        except:
                            print("El caracter no es numerico.")

                    Bishop = Alfil.alfill("B","A",fila,columna,fila_destino,columan_destino)
                    if Bishop.movimiento(reyB):
                        print()
                        print()
                        print("Movimiento valido")
                        turno = "N"
                        print(grid.g())
                    else:
                        print()
                        print()
                        print("Elija bien la fila y la columna nuevamente.")
                        print(grid.g())

                elif pieza[1] == "D":
                    print(pieza)
                    repeat = True
                    while repeat:
                        try:
                            fila_destino = int(input("Elija su movimiento en fila: "))
                            columan_destino = int(input("Elija su movimiento en columna: "))
                            if (fila_destino <= 7 and fila_destino >= 0) and (columan_destino <= 7 and columan_destino >= 0):

                                repeat = False
                        except:
                            print("El caracter no es numerico.")

                    Queen = Dama.Dama("B","D",fila,columna,fila_destino,columan_destino)
                    if Queen.movimiento(reyB):
                        print()
                        print()
                        print("Movimiento valido")
                        turno = "N"
                        print(grid.g())
                    else:
                        print()
                        print()
                        print("Elija bien la fila y la columna nuevamente Queen.")
                        print(grid.g())
                
                elif pieza[1] == "R":
                    print(pieza)
                    repeat = True
                    while repeat:
                        try:
                            fila_destino = int(input("Elija su movimiento en fila: "))
                            columan_destino = int(input("Elija su movimiento en columna: "))
                            if (fila_destino <= 7 and fila_destino >= 0) and (columan_destino <= 7 and columan_destino >= 0):

                                repeat = False
                        except:
                            print("El caracter no es numerico.")

                    """Hacer esto tambien para el bando negro"""
                    if reyB.movimiento(fila_destino,columan_destino):
                        print("Movimiento es valido.")
                        fila_reyB = fila_destino
                        columna_reyB = columan_destino
                        turno = "N"

                    else:
                        print("Movimiento invalido por causa de jaque, o seleccion de movimiento incorrecto.")
                        turno = "B"


                    """
                    if reyB.restricciones(fila_destino,columan_destino):
                        if reyB.Index_jaque >= 1:
                            print()
                            print()
                            print("Verifique su movimiento o si su rey esta en jaque.")
                            turno = "N"
                    else:
                        print()
                        print()
                        print("Movimiento valido.")
                        print(pieza)
                        fila_destino = int(input("Elija su movimiento en fila: "))
                        columan_destino = int(input("Elija su movimiento en columna: "))
                        reyB = Rey.Rey("B","R",fila,columna,fila_destino,columan_destino)
                        reyB.movimiento(fila_destino,columan_destino)   
                        fila_ant_reyB = fila
                        columna_ant_reyB = columna         
                        fila_reyB = fila_destino
                        columna_reyB = columan_destino
                        print(grid.printeo())
                    """


            else:
                print()
                print()
                turno = "B"
        else:
            print()
            print()
            print("Elije bien la pieza!")
            print(pieza)
            turno = "B"

    while turno == "N":
        reyN = Rey.Rey("N","R",fila_reyN,columan_reyN,fila_reyN,columan_reyN)
        if reyN.restricciones(fila_reyN,columan_reyN):
            if reyN.Index_jaque >= 1:
                if reyN.jaque_mate():
                    turno = "NO"
                    disponibilildad = False
                    print("Game over, ganas las blancas.")
                    break

        repeat = True
        while repeat:
            try:
                fila = int(input("Elija su pieza en filaN: "))
                columna = int(input("Elija su pieza en columnaN: "))
                if (fila <= 7 and fila >= 0) and (columna <= 7 and columna >= 0):

                    repeat = False
            except:
                print("El caracter no es numerico.")

        pieza = grid.get_Tablero(fila,columna)
       
        
        if pieza != 0:  
            if pieza[0] == "N":
                peon = Peon.peon("N","P",None,None,None,None)
                peon.Borrado_de_registro()     
                print(peon.registro)    
                
                if pieza[1] == "P":
                    print(pieza)
                    repeat = True
                    while repeat:
                        try:
                            fila_destino = int(input("Elija su movimiento en fila: "))
                            columna_destino = int(input("Elija su movimiento en columna: "))
                            if (fila <= 7 and fila >= 0) and (columna <= 7 and columna >= 0):

                                repeat = False
                        except:
                            print("El caracter no es numerico.")

                    peon = Peon.peon("N","P",fila,columna,fila_destino,columna_destino)
                    if peon.movimiento(reyN):
                        print("Turno de las blancas")
                        turno = "B"
                        print(grid.g())
                    else:
                        print("Elija bien la fila y la columna nuevamente.")
                        turno = "N"

                elif pieza[1] == "T":
                    print(pieza)
                    repeat = True
                    while repeat:
                        try:
                            fila_destino = int(input("Elija su movimiento en fila: "))
                            columna_destino = int(input("Elija su movimiento en columna: "))
                            if (fila_destino <= 7 and fila_destino >= 0) and (columna_destino <= 7 and columna_destino >= 0):

                                repeat = False
                        except:
                            print("El caracter no es numerico.")
                    
                    Tower = Torre.torre("N","T",fila,columna,fila_destino,columna_destino)
                    if Tower.movimiento(reyN):
                        print("Movimiento Valido")
                        print(grid.g())
                        turno = "B"
                    else:
                        print("Verifique su movimiento o si su rey esta en jaque")
                        print(grid.g())
                        turno ="N"
                        
                elif pieza[1] == "C":
                    print(pieza)
                    repeat = True
                    while repeat:
                        try:
                            fila_destino = int(input("Elija su movimiento en fila: "))
                            columan_destino = int(input("Elija su movimiento en columna: "))
                            if (fila_destino <= 7 and fila_destino >= 0) and (columan_destino <= 7 and columan_destino >= 0):

                                repeat = False
                        except:
                            print("El caracter no es numerico.")
                    
                    Caballo = caballo.caballo("N","C",fila,columna,fila_destino,columan_destino)
                    if Caballo.movimiento(reyN):
                        print("Movimiento valido")
                        print(grid.g())
                        turno = "B"
                    else:
                        print("Elija bien la fila y la columna nuevamente.")
                        print(grid.g())
                        turno = "N"

                elif pieza[1] == "A":
                    print(pieza)
                    repeat = True
                    while repeat:
                        try:
                            fila_destino = int(input("Elija su movimiento en fila: "))
                            columna_destino = int(input("Elija su movimiento en columna: "))
                            if (fila_destino <= 7 and fila_destino >= 0) and (columna_destino <= 7 and columna_destino >= 0):

                                repeat = False
                        except:
                            print("El caracter no es numerico.")
                    
                    Bishop = Alfil.alfill("N","A",fila,columna,fila_destino,columna_destino)
                    if Bishop.movimiento(reyN):
                        print("Movimiento valido")
                        print(grid.g())
                        turno = "B"
                    else:
                        print("Elija bien la fila y la columna nuevamente.")
                        print(grid.g())
                        turno = "N"

                elif pieza[1] == "D":
                    print(pieza)
                    repeat = True
                    while repeat:
                        try:
                            fila_destino = int(input("Elija su movimiento en fila: "))
                            columna_destino = int(input("Elija su movimiento en columna: "))
                            if (fila_destino <= 7 and fila_destino >= 0) and (columna_destino <= 7 and columna_destino >= 0):

                                repeat = False
                        except:
                            print("El caracter no es numerico.")
                    Queen = Dama.Dama("N","D",fila,columna,fila_destino,columna_destino)
                    if Queen.movimiento(reyN):
                        print("Movimiento valido")
                        print(grid.g())
                        turno = "B"
                    else:
                        print("Elija bien la fila y la columna nuevamente.")
                        print(grid.g())
                        turno = "N"

                elif pieza[1] == "R":
                    print(pieza)
                    repeat = True
                    while repeat:
                        try:
                            fila_destino = int(input("Elija su movimiento en fila: "))
                            columna_destino = int(input("Elija su movimiento en columna: "))
                            if (fila_destino <= 7 and fila_destino >= 0) and (columna_destino <= 7 and columna_destino >= 0):

                                repeat = False
                        except:
                            print("El caracter no es numerico.")

                    if reyN.movimiento(fila_destino,columna_destino):
                        print("Movimiento es valido.")
                        fila_reyN = fila_destino
                        columna_reyN = columna_destino
                        turno = "B"

                    else:
                        print("Movimiento invalido por causa de jaque, o seleccion de movimiento incorrecto.")
                        turno = "N"

                    """
                    if reyN.restricciones(fila_destino,columan_destino):
                        if reyN.Index_jaque >= 1:
                            print("Verifique su movimiento o si su rey esta en jaque.")
                            turno = "N"
                            print(grid.g())
                    else:
                        print("Movimiento valido.")
                        print(pieza)
                        turno = "B"
                        print(grid.g())
                        fila_destino = int(input("Elija su movimiento en fila: "))
                        columan_destino = int(input("Elija su movimiento en columna: "))
                        reyN = Rey.Rey("N","R",fila,columna,fila_destino,columan_destino)
                        reyN.movimiento() 
                        fila_ant_reyN = fila
                        columna_ant_reyN = columna         
                        fila_reyN = fila_destino
                        columan_reyN = columan_destino
                        print(grid.printeo())
                        """


            else:
                turno = "N"
        else:
            print("Elije bien la pieza!")
            print(pieza)
            turno = "N"
            
    #turno negro


