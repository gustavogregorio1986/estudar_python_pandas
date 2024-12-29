import pandas as pd

# Criando um DataFrame de exemplo
dados = pd.DataFrame({
    "A": [1, 2, 3],
    "B": [4, 5, 6],
    "C": [7, 8, 9]
})

print("DataFrame Original:")
print(dados)

# Soma das colunas
soma_colunas = dados.sum(axis=0)
print("\nSoma das colunas:")
print(soma_colunas)

# Soma das linhas
soma_linhas = dados.sum(axis=1)
print("\nSoma das linhas:")
print(soma_linhas)
