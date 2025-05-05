# 10. Contar vogais: Peça uma palavra e conte quantas vogais ela tem (a, e, i, o, u). 

palavra = input("Digite uma palavra:")
vogais = "aeiou AEIOU"
contador = 0

for letra in palavra:
        if letra in vogais:
                contador += 1

if contador == 0:
        print("A palavra não possui vogais.")
else:
        print("A palavra possui", contador, "vogais.")
        