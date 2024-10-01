from datetime import time

def valida_horario(horario):
    '''Verifica se a variável está num formato Hora válido.'''
    if len(horario) != 5:
        return False
    
    try:
        time.fromisoformat(horario)
        return True
    except ValueError:
        return False

def conversor(horario):
    '''Converte o input em horas e minutos e verifica a validade.'''
    horas = int(horario[:2])
    minutos = int(horario[3:])

    if 0 <= horas <= 23 and 0 <= minutos <= 59:
        return (horas, minutos)
    else:
        return False

def calcula_angulos(hora, minutos):
    '''Calcula os ângulos e retorna o menor.'''
    angulo_horas = (hora%12) * 30 + (minutos * 0.5)
    angulo_minutos = minutos * 6

    angulo_abs = abs(angulo_horas - angulo_minutos)

    menor_angulo = (360 - angulo_abs)

    return menor_angulo

def main():
    while True:
        horario = input("Digite um horário no formato HH:MM (ou 'f' para sair): ")
        
        if horario.lower() == 'f':
            print("Fim...")
            break
        
        if not valida_horario(horario):
            print("Input inválido.")
            continue
        
        resultado = conversor(horario)
        if resultado:
            horas, minutos = resultado
            menor_angulo = calcula_angulos(horas, minutos)
            print(f"O menor ângulo é de {menor_angulo}°")
        else:
            print("Input inválido.")

# Executa o programa
if __name__ == "__main__":
    main()
