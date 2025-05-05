# 7. Soma de 1 até N: Peça um número N e calcule a soma de todos os números de 1 até N. 

n = int(input("Digite um número:"))
soma = 0

for i in range(1, n + 1):
    soma += i

print("A soma de 1 até" , n, "é:", soma)
    