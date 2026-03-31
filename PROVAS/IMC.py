nome = input("Digite seu nome: ")
altura = float(input("Digite sua altura: "))
peso = float(input("Digite seu peso: "))
imc = peso / altura ** 2

print(f"Nome: {nome}")
print(f"altura: {altura} m")
print(f"peso: {peso} kg")
print(f"imc: {imc:.2f}")