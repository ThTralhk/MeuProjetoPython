saldo = 0.0

while True:
      opcao = input(
            "1 - Depositar\n"
            "2 - Sacar\n"
            "3 - Ver saldo\n"
            "4 - Sair\n"
      )
      if opcao == "1":
            deposito = float(input("Quantos R$ deseja depositar? R$ "))
            if deposito > 0:
                  saldo += deposito
                  print(f"Depósito realizado! Saldo atual: R${saldo:.2f}")
            else:
               print("Valor inválido!")

      elif opcao == "2":
            saque = float(input("Quantos R$ deseja sacar? R$"))
            if 0 < saque <= saldo:
                  saldo -= saque

                  print(f"Saque realizado! Saldo atual: R${saldo:.2f}")

            elif saque > saldo:
                  print("Saldo insuficiente!")
            else:
                  print("Valor inválido!")

      elif opcao == "3":
            print(f"Saldo atual: R${saldo:.2f}")

      elif opcao == "4":
            break

      else:
            print("Opção inválida!")