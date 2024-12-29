from datetime import datetime

def calcular_verbas_rescisorias(tipo_demissao, salario_mensal, dias_trabalhados, tem_férias_vencidas, tem_13º, fgts_devido):
    # Cálculos básicos
    saldo_salario = (salario_mensal / 30) * dias_trabalhados  # Proporcional ao número de dias trabalhados no mês
    aviso_previo = salario_mensal if tipo_demissao == "sem_justa_causa" else 0
    
    # Férias vencidas e 13º salário proporcional
    ferias_vencidas = salario_mensal / 3 if tem_férias_vencidas else 0
    decimo_terceiro = (salario_mensal / 12) * tem_13º  # Proporcional se o trabalhador for demitido antes de dezembro
    
    # FGTS e Multa
    fgts = salario_mensal * 0.08 * dias_trabalhados / 30  # 8% do salário por dia trabalhado
    multa_fgts = fgts * 0.4 if tipo_demissao == "sem_justa_causa" else 0  # Multa de 40% no caso de demissão sem justa causa
    
    # Calcular total de verbas rescisórias
    total_verbas = (saldo_salario + aviso_previo + ferias_vencidas + decimo_terceiro + fgts + multa_fgts)
    
    return {
        "saldo_salario": saldo_salario,
        "aviso_previo": aviso_previo,
        "ferias_vencidas": ferias_vencidas,
        "decimo_terceiro": decimo_terceiro,
        "fgts": fgts,
        "multa_fgts": multa_fgts,
        "total_verbas_rescisorias": total_verbas
    }

def gerar_relatorio(verbas_rescisorias):
    relatorio = f"""
    ** Relatório de Verbas Rescisórias **
    
    Saldo de Salário: R${verbas_rescisorias['saldo_salario']:.2f}
    Aviso Prévio: R${verbas_rescisorias['aviso_previo']:.2f}
    Férias Vencidas: R${verbas_rescisorias['ferias_vencidas']:.2f}
    13º Salário Proporcional: R${verbas_rescisorias['decimo_terceiro']:.2f}
    FGTS Devido: R${verbas_rescisorias['fgts']:.2f}
    Multa de 40% sobre FGTS: R${verbas_rescisorias['multa_fgts']:.2f}
    
    ** Total de Verbas Rescisórias: R${verbas_rescisorias['total_verbas_rescisorias']:.2f} **
    """
    return relatorio

# Entradas do usuário
tipo_demissao = input("Digite o tipo de demissão (sem_justa_causa / com_justa_causa): ").lower()
salario_mensal = float(input("Digite o salário mensal do empregado: R$ "))
dias_trabalhados = int(input("Digite o número de dias trabalhados no mês da rescisão: "))
tem_férias_vencidas = input("O trabalhador tem férias vencidas? (s/n): ").lower() == 's'
tem_13º = int(input("Digite o número de meses trabalhados para calcular o 13º salário proporcional: "))
fgts_devido = float(input("Digite o valor do FGTS devido ao trabalhador (caso haja algum valor): R$ "))

# Calcular e gerar o relatório
verbas_rescisorias = calcular_verbas_rescisorias(tipo_demissao, salario_mensal, dias_trabalhados, tem_férias_vencidas, tem_13º, fgts_devido)
relatorio = gerar_relatorio(verbas_rescisorias)

# Exibir o relatório
print("\n" + relatorio)
