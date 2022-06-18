for variavel in range(10):
  print(variavel)

soma = 0

for contador in range(4):
  nota = int(input(f"Digite sua nota_{contador}: "))

  soma += nota


media = soma / 4
print("Sua média foi: ", media)