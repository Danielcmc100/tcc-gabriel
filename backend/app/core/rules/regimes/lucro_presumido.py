def rule_carga_tributaria_estimada(
    faturamento_anual: float,
    regime: str
) -> dict:
    TAXAS = {
        "lucro_presumido": {
            "pis": 0.0065,
            "cofins": 0.03
        }
    }

    if regime not in TAXAS:
        return {
            "rule": "carga_tributaria",
            "status": "erro",
            "message": "Regime não suportado.",
            "impact": None
        }

    taxa_total = sum(TAXAS[regime].values())
    impacto = faturamento_anual * taxa_total

    return {
        "rule": "carga_tributaria",
        "status": "aplicada",
        "message": (
            "Carga tributária estimada calculada com base "
            "em alíquotas padrão."
        ),
        "impact": impacto
    }

if __name__ == "__main__":
    resultado = rule_carga_tributaria_estimada(
        faturamento_anual=1_000_000,
        regime="lucro_presumido"
    )
    print(resultado)