def calcular_pag(qtd_horas, valor_hora):
    horas = float(qtd_horas)
    valorhora = float(valor_hora)
    if horas <= 40:
        salario = horas * valor_hora
    else:
        extra = horas - 40
        salario = 40 * valorhora + (extra * horas * 1.5)
        return salario