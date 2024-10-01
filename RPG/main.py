from personagem import Heroi, Monstro
from item import espada

def inicial():
    global heroi, monstro
    heroi = Heroi("Galadriel", 20)
    monstro = Monstro("Globin", 10)
    heroi.equipar(espada)

def turno():
    global heroi, monstro
    print("O que fazer?")
    print("  1. Atacar")
    print("  2. Fugir")
    opcao = input("? ")
    if opcao == "1":
        if heroi.atacar(monstro) == True:
            print("Você venceu o inimigo!")
            print("Ele pediu deasculas e foi embora na paz")
            return False
    elif opcao == "2":
        print("Fuja seu covarde!")
        return False
    
    if monstro.atacar(heroi) == True:
        print("Você foi vencido pelo monstro")
        print("Mas ele foi piedoso e vocês fizeram as pazer")
        return False
    heroi.status()
    monstro.status()
    return True


def main():
    inicial()
    while turno() == True:
        print()
    print("ACABOU!")
    turno()

main()