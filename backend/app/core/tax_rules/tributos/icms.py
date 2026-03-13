def calcular_icms(
        valor_entrada: float,
        valor_saida: float,
        regime: str,
        setor: int 
) -> dict: 

    if setor == "prestacao_servico":
        aliquota = 0

        return {
            valor_icms == 0
        }
    
    elif setor == "comercio":
        aliquota = 0.0018,
        debitos = valor_saida  * aliquota,
        creditos = valor_entrada * aliquota,
        valor_icms = debitos - creditos

    return {
        icms:  valor_icms,
        "mensagem": "ICMS calculado com base em operações internas"
    }
        
    return {
        "pis": None,
        "mensagem": "Regime não suportado no MVP."
    }