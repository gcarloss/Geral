import random
#from item import balaclava
import item

class Personagem:
    def __init__(self, nome, vidas) -> None:
        self.nome = nome
        self.vidas = vidas
        self.maxvidas = vidas
        self.arma = None
    
    def status(self):
        print(f"{self.nome}  HP:{self.vidas}/{self.maxvidas}")
    
    def atacar(self,inimigo) -> bool:
        if self.arma is None:
            dano = 1
        else:
            dano = random.randint(1, self.arma.valor)
        print(f"{self.nome} infligiu {dano} de dano com {self.arma.nome}!")
        inimigo.vidas = inimigo.vidas - dano
        if inimigo.vidas <= 0:
            return True
        return False

class Heroi(Personagem):
    def __init__(self, nome, vidas):
        super().__init__(nome, vidas)
        self.inventario = []
    
    def equipar (self, arma):
        if self.arma.tipo == "arma":
            print(f"{self.nome} está usando a poderosa {arma.nome}")
            self.arma = arma



class Monstro(Personagem):
    def __init__(self, nome, vidas):
        super().__init__(nome, vidas)
        self.Arma = balaclava