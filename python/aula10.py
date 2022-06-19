def saudacao(nome, curso):
  print(f'Bem vindo {nome}!')
  print(f'É um prazer ter você fazendo parte do curso de {curso}')

saudacao('Isaac', 'Python')

def calculadora(numero1,numero2, operacao="+"):
  if operacao == '-':
    return numero1 - numero2
  elif operacao == '*':
    return numero1 * numero2
  elif operacao == '/':
    return numero1 / numero2
  else:
    return numero1 + numero2

print(calculadora(1,3,'-'))
print(calculadora(1,3))
print(calculadora(1,3,'/'))
print(calculadora(1,3,'*'))