# Agora vamos solicitar uma string e um numero inteiro como entrada. Depois teremos que retornar a string repetida o numero de vezes informado.

string = input("Digite uma string: ")
numero = int(input("Digite um numero inteiro: "))

vezes_repetida = ' '.join([string] * numero)

print(vezes_repetida)