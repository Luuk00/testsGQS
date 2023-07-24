def aumento_queda_vendas(lista_percentuais):
    resultado = []
    for carro, percentual_atual, percentual_anterior in lista_percentuais:
        if percentual_atual > percentual_anterior:
            resultado.append((carro, 1))  # Aumento
        elif percentual_atual < percentual_anterior:
            resultado.append((carro, 0))  # Queda
        else:
            resultado.append((carro, 2))  # Mesmo percentual
    return resultado