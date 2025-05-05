# 15. Jogo de adivinhação simples: O programa escolhe um número entre 1 e 10 e o usuário tenta adivinhar. Use random para gerar o número.

import random

def jogo_adivinhacao():
    numero_secreto = random.randint(1, 10)

    print("Bem-vindo ao jogo de adivinhação!")

    for _ in range(1_000_000):
        num = int(input("Adivinhe o número entre 1 e 10: "))
        
        if num == numero_secreto:
            print("Parabéns! Você adivinhou o número!")
            break
        else:
            print("Tente novamente!")

jogo_adivinhacao()