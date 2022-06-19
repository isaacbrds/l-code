dicionario = {}

dicionario = {'nome': 'Isaac', 'idade': 39, 'altura': 1.81 }

print(dicionario)
print(dicionario['idade'])

dicionario['programador'] = True

print(dicionario)

for chave in dicionario:
  print(chave, dicionario[chave])