# core/rules_engine/engine.py

from core.rules.pis import calcular_pis
from core.rules.cofins import calcular_cofins

def executar_regras(contexto):
    resultados = {}

    resultados["pis"] = calcular_pis(
        contexto.saidas,
        contexto.entradas,
        contexto.regime
    )

    resultados["cofins"] = calcular_cofins(
        contexto.saidas,
        contexto.entradas,
        contexto.regime
    )

    return resultados