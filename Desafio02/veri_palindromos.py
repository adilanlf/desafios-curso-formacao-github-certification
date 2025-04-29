#Vamos testar se uma palavra é um palíndromo

# Recebe uma palavra do usuário
palavra = input("Digite uma palavra: ")

# Remove espaços e deixa tudo minúsculo para facilitar a comparação
palavra = palavra.replace(" ", "").lower()

# Verifica se a palavra é igual a ela mesma invertida
if palavra == palavra[::-1]:
    print("É um palíndromo!")
else:
    print("Não é um palíndromo.")
