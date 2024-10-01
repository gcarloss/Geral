SIZE = 20


datal = [
    [
        " o ",
        "ooo",
    ],
    [
        " o ",
        " oo",
        " o ",
    ],
]


class Block:
    def __init__(self, canvas):
        self.x =0
        self.y =0
        self.i = 0
        self.data = datal
        self.canvas = canvas
        self.board = board
        self.ids = []

    def get_bm(self):
        '''Retorna Bitmap atual'''
        return self.data[self.i]
    
    def erase (self):
        for id in self.ids:
            self.canvas.delete(id)


    def draw(self):
        self.erase() #Apaga antes de desenhar novamente!
        desenho = self.get_bm()
        yb = self.y = SIZE
        for linha in desenho:
            xb = self.x * SIZE
            for caractere in linha:
                if caractere != ' ':
                    id = self.canva.create_retangle(
                        xb,yb, xb+SIZE, yb+SIZE,
                        fill = "red")
                    self.ids.append(id)
                xb += SIZE
            yb += SIZE


    def rotate(self):
        new_i = self.i + 1
        if new_i >= len(self.data):
            new_i = 0
        
        if self.board.collide(self.data[new_i], self.x, self.y):
            return
        
        self.i = new_i
        self.draw()

    def move_left(self):
        if self.board.collide(self.get_bm(), self.x-1, self.y):
            return
        for id in self.ids:
            self.canvas.move(id, -SIZE, 0)
        self.x -= 1

    def move_right(self):
        if self.board.collide(self.get_bm(), self.x+1, self.y):
            return
        for id in self.ids:
            self.canvas.move(id, +SIZE, 0)
        self.x += 1

    def drop(self):
        if self.board.collide(self.get_bm(), self.x, self.y+1):
            return True
        for id in self.ids:
            self.canvas.move(id, 0, +SIZE)
        self.y += 1
