# 13. Verificador de número primo: Peça um número e diga se ele é primo (divisível apenas por 1 e por ele mesmo). 

n = int(input("Digite um número:"))
primo = True

if n < 2:
    primo = False

else:
    for i in range(2, n):
        if n % i == 0:
            primo = False


if primo:
    print("O número", n, "é primo.")

else:
    print("O número", n, "não é primo.")