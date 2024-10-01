import tkinter as tk
import block
import board

ROWS = 30
COLS = 20
SIZE = 15
block.SIZE =  SIZE


class App(tk.Frame):
    def __init__ (self, master):
        super().__init__(master)

        self.canvas = tk.Canvas(
            width = COLS*SIZE,
            height = ROWS*SIZE,
            bg = 'black')

        self.canvas.pack()
        self.canvas.bind("<Key>", self.on_key)
        self.canvas.focus_set()

        self.board = board.Board(ROWS, COLS)

        self.block = block.Block(self.canvas, self.board)
        self.block.draw()

        self.after(200, self.animate)

def animate(self):
    if self.block.drop() == True:
        self.block = block.Block(self.canvas, self.board)
        self.block.draw()
    self.after(200, self.animate)

def on_key(self,event):
    k = event.kesym
    if k == "left":
        self.block.move_left()
    elif k == "right":
        self.block.move_right()
    elif k == "up":
        self.block.rotate()

app = App(master = tk.Tk())
app.mainloop()