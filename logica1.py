import pandas as pd

# Criando um DataFrame de exemplo
dados = pd.DataFrame({
    "Números": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
})

# Filtrando apenas os números pares
numeros_pares = dados[dados["Números"] % 2 == 0]

# Exibindo os resultados
print("Números pares:")
print(numeros_pares)
