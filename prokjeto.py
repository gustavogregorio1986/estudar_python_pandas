import pandas as pd

dados = pd.read_csv("C:\estudar_python/base_vendas.csv")

print(dados)


print("Primeiros registros do arquvio CSV: ")
print(dados.head())

dados2 = pd.read_csv("C:\estudar_python/base_vendas.csv", encoding="ISO-8859-1")

print(dados2)

print(dados.bfill())