login_certo = "santanaturbo"
senha_certa = "meusantanaturbo011"
tentativas = 3
login = ""
senha = ""

while tentativas > 0:
    login = input("Digite seu login: ")
    senha = input("Digite sua senha: ")

    if login == login_certo and senha == senha_certa:
        print("Acesso liberado!")
        input("O que deseja hoje chefe?")
        break

    else:
        tentativas -= 1
        print(f"Login ou senha incorreto! Você tem {tentativas} tentativas restantes.")

if tentativas == 0:
    print("Acesso bloqueado!")