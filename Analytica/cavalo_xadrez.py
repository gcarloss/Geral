def valida_posicao(posicao):
    '''Verifica se a posição é válida no tabuleiro de xadrez'''
    eixo_x = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    
    if len(posicao) != 2:
        return False
    
    x = posicao[0]
    y = posicao[1]
    
    if x.lower() in eixo_x:
        try:
            y = int(y)
            if 1 <= y <= 8:
                return True
            else:
                return False
        except ValueError:
            return False
    else:
        return False

def letra_para_numero(letra):
    '''Recebe uma letra e transforma em um número'''
    letraparanumero = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8}
    return letraparanumero.get(letra.lower())

def numero_para_letra(numero):
    '''Recebe um número e transforma em uma letra'''
    numeroparaletra = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f', 7: 'g', 8: 'h'}
    return numeroparaletra.get(numero)

def movimentos(letra, numero):
    '''Calcula os movimentos possíveis do cavalo'''
    movimentos = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]
    
    coluna = letra_para_numero(letra)
    linha = numero

    mov_validos = []

    for movimento in movimentos:
        nova_coluna = coluna + movimento[0]
        nova_linha = linha + movimento[1]

        if 1 <= nova_coluna <= 8 and 1 <= nova_linha <= 8:
            nova_letra = numero_para_letra(nova_coluna)
            mov_validos.append(f'{nova_letra}{nova_linha}')
    
    return mov_validos

def main():
    while True:
        posicao = input("Digite a posição inicial do cavalo (ex: b1) ou 'f' para sair: ")

        if posicao.lower() == 'f':
            print("Fim.")
            break

        if not valida_posicao(posicao):
            print('Posição inválida.')
        else:
            letra = posicao[0]
            numero = int(posicao[1])

            movimentos_validos = movimentos(letra, numero)

            print(f'Movimentos possíveis: {", ".join(movimentos_validos)}')

main()
