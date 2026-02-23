from core.rules_engine.engine import executar_regras
from core.rules_engine.context import ContextoTributario

contexto = ContextoTributario(
    regime="lucro_real",
    tipo_empresa="industria",
    entradas=300_000,
    saidas=1_000_000,
    faturamento=1_000_000,
    ano=2025
)

resultado = executar_regras(contexto)

print(resultado)