def calcular_pis(
    valor_saidas: float,
    valor_entradas: float,
    regime: str
) -> dict:

    if regime == "lucro_presumido":
        aliquota = 0.0065
        valor = valor_saidas * aliquota

        return {
            "pis": valor,
            "mensagem": "PIS cumulativo (Lucro Presumido), sem créditos."
        }

    elif regime == "lucro_real":
        aliquota = 0.0165

        debitos = valor_saidas * aliquota
        creditos = valor_entradas * aliquota
        valor = max(debitos - creditos, 0)

        return {
            "pis": valor,
            "mensagem": "PIS não cumulativo (Lucro Real), com aproveitamento de créditos."
        }

    return {
        "pis": None,
        "mensagem": "Regime não suportado no MVP."
    }