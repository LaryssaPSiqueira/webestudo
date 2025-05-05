# 11. Verificar ano bissexto: Peça um ano e diga se ele é bissexto (divisível por 4 e não por 100, exceto se divisível por 400). 

ano = int(input("Digite um ano: "))

if (ano % 4 == 0 
    and ano % 100 != 0) or (ano % 400 == 0):
    
    print(f"O ano {ano} é bissexto.")

else:
    print(f"O ano {ano} não é bissexto.")
