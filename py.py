def calcular_rendimento(valor_inicial, dias):

    taxa_anual = 14.15 / 100
    taxa_diaria = (1 + taxa_anual) ** (1 / 365) - 1

    rendimento_bruto = valor_inicial * ((1 + taxa_diaria) ** dias - 1)

    
    tabela_iof = {
        1: 96, 2: 93, 3: 90, 4: 86, 5: 83, 6: 80, 7: 76, 8: 73, 9: 70, 10: 66,
        11: 63, 12: 60, 13: 56, 14: 53, 15: 50, 16: 46, 17: 43, 18: 40, 19: 36, 20: 33,
        21: 30, 22: 26, 23: 23, 24: 20, 25: 16, 26: 13, 27: 10, 28: 6, 29: 3, 30: 0
    }

    aliquota_iof = 0
    if dias <= 30:
        aliquota_iof = tabela_iof.get(dias, 0) / 100
    valor_iof = rendimento_bruto * aliquota_iof

    
    if dias <= 180:
        aliquota_ir = 22.5 / 100
    elif dias <= 360:
        aliquota_ir = 20 / 100
    elif dias <= 720:
        aliquota_ir = 17.5 / 100
    else:
        aliquota_ir = 15 / 100

    valor_ir = (rendimento_bruto - valor_iof) * aliquota_ir

    
    valor_liquido = valor_inicial + rendimento_bruto - valor_iof - valor_ir

    return {
        'valor_investido': valor_inicial,
        'rendimento_bruto': round(rendimento_bruto, 2),
        'iof': round(valor_iof, 2),
        'ir': round(valor_ir, 2),
        'valor_liquido': round(valor_liquido, 2)
    }

valor = 1000.00
dias = 45

resultado = calcular_rendimento(valor, dias)

print("\n--- RESUMO DA APLICAÇÃO ---")
print(f"Valor Investido: R$ {resultado['valor_investido']:.2f}")
print(f"Rendimento Bruto: R$ {resultado['rendimento_bruto']:.2f}")
print(f"Desconto IOF: R$ {resultado['iof']:.2f}")
print(f"Desconto IR: R$ {resultado['ir']:.2f}")
print(f"Valor Líquido Final: R$ {resultado['valor_liquido']:.2f}")
