while True:
    tabuada = int(input("Digite um numero: "))
    for valor in range(1, 11) :
        print(f"{tabuada} x {valor} = {tabuada * valor}")
    print(f"Fim da tabuada do número {tabuada}")

    sair = input("Deseja sair? [S/N] ")
    if sair.lower() == "s":
      break
