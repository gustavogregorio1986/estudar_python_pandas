def calcular_fgts(salario_bruto):
    return salario_bruto * 0.08  # 8% de FGTS

def calcular_inss(salario_bruto):
    if salario_bruto <= 1302:
        inss = salario_bruto * 0.075  # 7.5%
    elif salario_bruto <= 2571.29:
        inss = salario_bruto * 0.09  # 9%
    elif salario_bruto <= 3856.94:
        inss = salario_bruto * 0.12  # 12%
    elif salario_bruto <= 7507.49:
        inss = salario_bruto * 0.14  # 14%
    else:
        inss = 1050.99  # Teto do INSS para salários maiores que 7507.49
    return inss

def calcular_salario_liquido(salario_bruto, inss):
    return salario_bruto - inss

# Entrada de dados
salario_bruto = float(input("Digite o salário bruto: "))

# Cálculos
fgts = calcular_fgts(salario_bruto)
inss = calcular_inss(salario_bruto)
salario_liquido = calcular_salario_liquido(salario_bruto, inss)

# Exibição dos resultados
print(f"FGTS: R${fgts:.2f}")
print(f"INSS: R${inss:.2f}")
print(f"Salário Bruto: R${salario_bruto:.2f}")
print(f"Salário Líquido: R${salario_liquido:.2f}")
