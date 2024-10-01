from matrix import Matrix

def pergunta_matriz(nome):
    print(f"Digite os valores da matriz {nome} separados por espaço:")

    m = []

    r = 0
    while r < 1000:
        texto = input(f"linha (r+1): ")
        if texto == "": break
        linha =  map(float, texto.split())
        m.append( list(linha))
        r = r + 1
    
    nrows = len(m)
    ncols = len(m[0])
    M = Matrix(nrows, ncols, nome)
    M.m = m  #atuazliando os valores
    return M

def main():
    A = pergunta_matriz("A")
    B = pergunta_matriz("B")
    print(A + B)

main()