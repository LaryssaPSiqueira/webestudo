# 6. Tabuada: Peça um número e mostre a tabuada dele de 1 a 10. 

num1 = int(input("Digite um número:"))

print("Tabuada de" , num1)

for i in range(1, 11):
    resultado = num1 * i
    print(num1, "x", i, "=", resultado)