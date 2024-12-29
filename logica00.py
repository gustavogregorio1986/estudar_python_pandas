import pandas as pd

try:
    # Solicitar ao usuário o número da tabuada
    numero = int(input("Digite o número para gerar a tabuada: "))
    
    # Gerar a tabuada
    valores = list(range(1, 11))  # Valores de 1 a 10
    resultados = [numero * i for i in valores]
    
    # Criar um DataFrame para organizar a tabuada
    tabuada = pd.DataFrame({
        "Multiplicador": valores,
        f"{numero} x Multiplicador": resultados
    })
    
    # Exibir a tabuada
    print("\nTabuada:")
    print(tabuada)

except ValueError:
    print("Erro: Por favor, digite um número inteiro válido.")
except Exception as e:
    print(f"Erro inesperado: {e}")
