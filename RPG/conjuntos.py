nadam = {'golfinho', 'pato', 'jacaré', 'homem'}
voam = {'sabiá', 'pato', 'galinha'}
andam = {'homem', 'jacaré', 'vaca', 'gato', 'pato', 'galinha'}

#a) Bichos nadam ou voam
print('Bichos nadam ou voam:')
print(nadam|voam)
print(nadam.union(voam))

#b) Bichos que nadam mas não voam
print('Bichos que nadam mas não voam:')
print(nadam - voam)
print(nadam.difference(voam))

#c) Bichos que voam, mas não nadam
print('Bichos que voam, mas não nadam:')
c = nadam - voam
print(c)
print(voam.difference(nadam))

#d) Bichos que voam mas não nadam
print('Bichos que voam mas não nadam:')
print(voam - nadam)
print(voam.difference(nadam))

#e) galinha está em c?
print('galinha está em c?', 'galinha' in c )

#f) Bichos que nadam E voam
print('Bichos que nadam E voam:')
f = nadam&voam
print(f)
print(nadam.intersection(voam))

#e) Bichos de f que começam com 'g'
for bicho in f:
    if bicho[0] == "g":
        print(bicho,"comaça com g")
    else:
        print("Nehum bicho em F começa com 'g'")

###----------------- Exercício 2---------------------

frase = "O rato roeu a roupa do rei de Roma, por isso nao ganhou queijo."
frase_minuscula = set(frase.lower())
print(frase_minuscula)

sinais = set('., !?')
# print(sinais)
novafrase = frase_minuscula.difference(sinais)
print(novafrase)
letras = len(novafrase)
print('Qtd letras: ', letras)

conj_vogais = set('aeiou')
conj_consoantes = set('bcdfghjklmnpqrstvxyz')

frase_consoantes = novafrase&conj_consoantes
frase_vogais = novafrase&conj_vogais

# print(frase_consoantes)
# print(frase_vogais)

vogais = len(frase_vogais)
consoantes = len(frase_consoantes)

print('Qtd vogais: ', vogais)
print("Qtd consoantes: ", consoantes)


