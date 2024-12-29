import pandas as pd

# Criando um DataFrame de exemplo
dados = pd.DataFrame({
    "Valor1": [10, 20, 30],
    "Valor2": [5, 15, 25]
})

print("DataFrame Original:")
print(dados)

# Função para realizar operações
def calculadora(df, operacao):
    if operacao == "soma":
        resultado = df["Valor1"] + df["Valor2"]
    elif operacao == "subtracao":
        resultado = df["Valor1"] - df["Valor2"]
    elif operacao == "multiplicacao":
        resultado = df["Valor1"] * df["Valor2"]
    elif operacao == "divisao":
        resultado = df["Valor1"] / df["Valor2"]
    else:
        raise ValueError("Operação inválida. Escolha: soma, subtracao, multiplicacao ou divisao.")
    return resultado

# Executando a calculadora
operacao = input("Digite a operação (soma, subtracao, multiplicacao, divisao): ").strip().lower()
resultado = calculadora(dados, operacao)

# Adicionando o resultado ao DataFrame
dados["Resultado"] = resultado

print("\nDataFrame com o Resultado:")
print(dados)
