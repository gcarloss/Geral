def validacao (entrada):
    '''Verifica se o valor recebido é válido
    '''
    try:
        valor = float(entrada)
        if valor >= 0:
            return True
        else:
            return False
    except ValueError:
        return False

def decomposicao (valor):
    '''Decomponhe os valor em relação as notas e moedas'''

    dinheiros = [100, 50, 20, 10, 5, 2, 1, 0.5, 0.25, 0.10,0.05, 0.01]

    qauntidades = {}

    for dinheiro in dinheiros:
        qauntidades[dinheiro] = int(valor // dinheiro)
        valor %= dinheiro
    
    return qauntidades


def main():
    while True:
        entrada = input("Digite o valor ('f para sair'):")

        if entrada.lower() == 'f':
            print('Fim.')
            break

        if not validacao(entrada):
            print("Input inválido. Digite um valor válido (ex.:2.56)")
            continue

        valor = float(entrada)

        quantidades = decomposicao(valor)
        
        print("NOTAS:")
        for nota in [100, 50, 20, 10, 5, 2]:
            print(f"{quantidades[nota]} nota(s) de R$ {nota:.2f}")
        
        print("MOEDAS:")
        for moeda in [1, 0.5, 0.25, 0.10, 0.05, 0.01]:
            print(f"{quantidades[moeda]} moeda(s) de R$ {moeda:.2f}")

main()
