class Tablero():
    
    lista = [[0 for y in range(8)] for x in range(8)]

    def printeo(self):
        return Tablero.lista   
        

    def set_Tablero(self,row,col,Pieza):
        Tablero.lista[row][col] = Pieza
        return Tablero.lista

    def get_Tablero(self,row,col):
        return Tablero.lista[row][col]

    def g(self):

        for i in range(0,8):
            print(Tablero.lista[i])
