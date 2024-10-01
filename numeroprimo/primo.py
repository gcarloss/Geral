def primo(x):
    '''Retorna True se um numero for primo.
        (int) -> bool
    '''
    if x >= 2:
        for n in range(2,x):
            if x % n == 0:
                return False
        return True
    return False

def filtra_primos(lista):
    '''Retorna uma lsita com os números primos de lista.
    (list) -> list
    '''
    lista_primos = []
    for x in lista:
        if primo(x):
            list.append(lista_primos, x)
    return lista_primos

# CASOS DE TESTE
if __name__ == "__main__":
    print( primo(-5)) #false
    print(primo(1)) #false
    print( primo(2)) #true
    print( primo(3)) #true
    print( primo(4)) #false
    print( primo(17)) #false
    print(filtra_primos([-5, 1, 2, 3, 4, 17, 2147483647]))