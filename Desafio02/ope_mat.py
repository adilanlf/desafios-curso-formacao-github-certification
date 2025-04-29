# Vamos solicitar como entrada dois numeros e depois vamos realizar uma operaçao simples entre eles.

def solicitar_numero(texto):
    return float(input(texto))

def solicitar_operacao():
    return input("Escolha a operação (+, -, *, /): ")

def calcular(n1, n2, op):
    if op == '+':
        return n1 + n2
    elif op == '-':
        return n1 - n2
    elif op == '*':
        return n1 * n2
    elif op == '/':
        if n2 != 0:
            return n1 / n2
        else:
            return "Erro: divisão por zero!"
    else:
        return "Operação inválida!"

def main():
    n1 = solicitar_numero("Digite o primeiro número: ")
    n2 = solicitar_numero("Digite o segundo número: ")
    op = solicitar_operacao()
    resultado = calcular(n1, n2, op)
    print(f"Resultado: {resultado}")

if __name__ == "__main__":
    main()