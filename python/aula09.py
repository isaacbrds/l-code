lista = [1,3,8,12,2]

print(lista)
lista.append(5)

print(lista)

lista.insert(2,13)

print('Depois do insert', lista)

lista2 = [2,9,0]
lista.extend(lista2)


print('Depois do extend', lista)


fruta = 'banana'

print('Quantidade de a', fruta.count('a'))

print('tamanho', len(fruta))

print('Soma', sum(lista))

print('Min', min(lista))

print('Max',max(lista))

