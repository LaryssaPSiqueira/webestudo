# 14. Inverter palavra: Peça uma palavra e exiba-a invertida (ex: “python” → “nohtyp”). 

palavra = input("Digite uma palavra: ")
palavra_invertida = " "

for letra in palavra:
    palavra_invertida = letra + palavra_invertida

print("A palavra invertida é:" ,palavra_invertida,)