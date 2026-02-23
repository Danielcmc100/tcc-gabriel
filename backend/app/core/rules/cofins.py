def calcular_cofins(
    valor_saidas: float,
    valor_entradas: float,
    regime: str
) -> dict:

    if regime == "lucro_presumido":
        aliquota = 0.03
        valor = valor_saidas * aliquota

        return {
            "cofins": valor,
            "mensagem": "COFINS cumulativo (Lucro Presumido), sem créditos."
        }

    elif regime == "lucro_real":
        aliquota = 0.076

        debitos = valor_saidas * aliquota
        creditos = valor_entradas * aliquota
        valor = max(debitos - creditos, 0)

        return {
            "cofins": valor,
            "mensagem": "COFINS não cumulativo (Lucro Real), com aproveitamento de créditos."
        }

    return {
        "cofins": None,
        "mensagem": "Regime não suportado no MVP."
    }