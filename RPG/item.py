class Item:
    def __init__(self, nome, valor, tipo):
        self.nome = nome
        self.valor = valor
        self.tipo = tipo

class Arma(Item):
    def __init__(self, nome, valor):
        super().__init__(nome, valor, "arma")
        # self.nome = nome
        # self.valor = valor
        # self.tipo = "arma"

class Comida(Item):
    def __init__(self, nome, valor):
        super().__init__(nome, valor, "comida")

#ARMAS
espada = Arma("espada longa", 10)
balaclava = Arma("bataclava", 7)

#COMIDA
maca = Comida("maçã", 5)

#Poções
panaceia = Item("panaceia", 10, "poção")