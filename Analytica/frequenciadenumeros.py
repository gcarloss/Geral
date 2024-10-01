def cont_frequencia ():

    frequencia = {}

    while True:

        entrada = input("Digite um número inteiro (ou 'f' para finalizar):")

        if entrada.lower() == 'f':
            break

        try:
            numero = int(entrada)

            if numero in frequencia:
                frequencia[numero] += 1
            else:
                frequencia[numero] = 1
        
        except ValueError:
            pass
    
    for numero, contagem in frequencia.items():
        if contagem == 1:
            print(f'O número {numero} apareceu {contagem} vez')
        else:
            print(f'O número {numero} apareceu {contagem} vezes')
    
    print('Fim...')


cont_frequencia()