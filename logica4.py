def tabuada(numero):
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

# Exemplo de uso
numero = int(input("Digite o número para ver a tabuada: "))
tabuada(numero)
