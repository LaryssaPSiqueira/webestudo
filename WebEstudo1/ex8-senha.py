# 8. Verificador de senha: Peça uma senha e só permita continuar se for igual a "1234", usando while. 

senha = input("Digite a senha:")

while senha != "1234":
    print("Senha incorreta. Tente novamente.")
    senha = input("Digite a senha:")

while senha == "1234":
    print("Senha correta. Acesso permitido.")
    print("Bem-vindo(a) 😊")
