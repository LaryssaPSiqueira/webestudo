# 12. Gerador de sequência: Peça um número e gere uma sequência de 0 até esse número, pulando de 2 em 2. 

n = int(input("Digite um número:"))

for i in range(0, n+ 1, 2):
    print(i, end= " ")

