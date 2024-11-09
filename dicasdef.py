def dica_paridade(numero):
    if numero % 2 == 0:
        return f"O número {numero} é par."
    else:
        return f"O número {numero} é ímpar."
      
def dica_divisao(numero):
  if numero % 5 == 0:
      return f"O número {numero} é divisivel por 5"
  else:
      return f"O número {numero} não é divisivel por 5"

# Testando o código
numero = int(input("Digite um número: "))
print(dica_paridade(numero))
print(dica_divisao(numero))

