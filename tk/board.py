class Board:
    def __init__(self, rows, cols):
        data = []
        for i in range(rows):
            data.append([0]*cols)
        
        self.rows = rows
        self.cols = cols
        self.data = data
    
    def collide (self, bm, x, y) -> bool:
        '''Retorna True se o desenho colide com alguma coisa ou sai
            do tabuleiro
        '''
        i = y
        for linha in bm:
            j = x
            for caractere in linha:
                if caractere != ' ':
                    if i >= self.rows: return True
                    if j < 0 or j >= self.cols: return True
                    if i >= self.cols: return True
                    if self.data[i][j] != 0: return True
                j += 1
            i += 1

        return False
