import Peon
import grig_general
import identifier
import pygame 
import time
from pygame import mixer

pygame.init()
pygame.mixer.init()
mixer.music.load('Sounds/GameStart.wav')
mixer.music.play()
display=pygame.display.set_mode((580,580))


grid = grig_general.gridd
board = grid
disponibilildad = True
 
def drawgrid(display):
    color1 = (240,217,181)
    color2 = (148,111,81)
    for row in range(8):
        for col in range(8):
            odd = (row + col) % 2
            if odd is 1:
               pygame.draw.rect(display,color2,pygame.Rect(col*(580//8),row*(580//8),(580//8),(580//8)))
            else:
               pygame.draw.rect(display,color1,pygame.Rect(col*(580//8),row*(580//8),(580//8),(580//8)))

 
  
def selection():
    enable = True
    
    while enable:
        for event in pygame.event.get():
            if event.type== pygame.QUIT:
                pass
            if event.type == pygame.MOUSEBUTTONDOWN:
 
                col,row= pygame.mouse.get_pos()
                
                col = (col // 72)
                row = abs((row // 72)-7)
                print(row,col) 
                try:
                  
                    if (row <= 7 and row >= 0) and (col <= 7 and col >= 0):

                        enable = False
                     
                except:
                    print("El caracter no es numerico.")
                
    return row, col
  
def drawpieces():
    drawgrid(display)
    for row in range(7,-1,-1):
        for col in range(8):
            piece = board.get_Tablero(abs(row-7),col)
            if piece != 0:
                print(row*72,col*72)
                
                display.blit(pygame.transform.scale(pygame.image.load("image/"+piece[0]+piece[1]+".png"),((72),(72))),(col*72,row*(72)))    
    time.sleep(0.1)
    pygame.display.update()
            


while disponibilildad:
    print(type(grid))
    drawgrid(display)
    drawpieces()
    pygame.display.update()
    print(grid.g())
    turno = "B"
    #turno blanco
    while turno == "B":
 

        verification = identifier.ID.verify_checks(turno)
        if verification == 2:
            turno = "NO"
            disponibilildad = False
            print("Game over, ganan las negras.")
            moveSound = mixer.Sound('Sounds/GameOver.wav')
            moveSound.play()
            time.sleep(1)
            break
        elif verification == 1:
            moveSound = mixer.Sound('Sounds/Check.wav')
            moveSound.play()
            time.sleep(0.1)
        else:
            print("No hay jaque")     
   
       
         
        Peon.peon.Borrado_de_registro("B")
          
        coord = selection()
        target = selection()
        check_move =  identifier.ID.verification(turno,coord,target)
        if check_move:
            print()
            print()
            print("Turno De las negras")
            print(grid.g())
                                    
            turno = "N"
        else:
            print("Elija bien la fila y la columna nuevamente.")
        
       
                

     
    moveSound = mixer.Sound('Sounds/Move.wav')
    moveSound.play()
    time.sleep(0.01)
        

    while turno == "N":

        drawgrid(display)
        drawpieces()
        
        verification = identifier.ID.verify_checks(turno)
        if verification == 2:
            turno = "NO"
            disponibilildad = False
            print("Game over, ganan las blancas.")
            moveSound = mixer.Sound('Sounds/GameOver.wav')
            moveSound.play()
            time.sleep(1)
            break
        elif verification == 1:
            moveSound = mixer.Sound('Sounds/Check.wav')
            moveSound.play()
            time.sleep(0.1)
        else:
            print("No hay jaque")   
        
        coord = selection()
        target = selection()
        check_move =  identifier.ID.verification(turno,coord,target)
        if check_move:
            print()
            print()
            print("Turno De las blancas")
            print(grid.g())
                                    
            turno = "B"
        else:
            print("Elija bien la fila y la columna nuevamente.")
 
    pygame.display.update()
    moveSound = mixer.Sound('Sounds/Move.wav')
    moveSound.play()
    time.sleep(0.01)
            
    #turno negro



pygame.quit()   