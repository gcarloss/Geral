#matrix.py - Módulo Aluno A

class DimensionError(Exception):
    def __init__(self, msg = "Incompatilble Dimensios for this Matrix") -> None:
        super().__init__(msg)


class Matrix:
    def __init__ (self, r, c, label = '', iv=0.0):
        self.nrows = r
        self.ncols = c
        self.label = label
        m = []
        for i in range(r):
            m.append([iv]*c) #initial value
        self.m = m # contém os dados da matriz
    
    def __str__(self) -> str:
        if self.label:
            t = self.label + " =\n"
        else:
            t = ""
        for linha in self.m:
            t += "| "
            for num in linha:
                t += f"{num: 8.3f} "
            t += " |\n"
        return t

    def __add__ (self, B):
        #Comparar dimensões de self e B,
        #se diferentes raise DimensionErros
        if self.ncols != B.ncols or self.nrows !=B.nrows:
            raise DimensionError
        
        nomeC = self.label + "+" + B.label
        C = Matrix(self.nrows, self.ncols, nomeC)

        for r in range(self.nrows):
            for c in range(self.ncols):
                C.m[r][c] = self.m[r][c] + B.m[r][c]


        return C # C é do tipo Matrix

# CASOS DE TESTE
if __name__ == "__main__":
    A = Matrix(4,5, "A", 1.0)
    B = Matrix(5,4,"B", 3.5)
    D = Matrix(5,4,"D", 0.5)
    print(A,B,D)
    try:
        c = A + B
    except DimensionError as e:
        print(e)

