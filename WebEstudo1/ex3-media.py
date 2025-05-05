# 3. Média de três notas: Leia três notas de um aluno, calcule a média e informe se ele foi aprovado (média ≥ 7).

# Dados
nota1 = float(input("Digite a primeira nota:"))
nota2 = float(input("Digite a segunda nota:"))
nota3 = float(input("Digite a terceira nota:"))

media = (nota1 + nota2 + nota3) / 3


print("A média do aluno é:" ,media)
if media >=7:
    print("O aluno foi aprovado.")
else:
    print("O aluno foi reprovado.")
    