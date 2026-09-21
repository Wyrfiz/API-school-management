"""
API pública de dados abertos — Escola Dalva Pontes da Rocha
CC0464 - Interfaces de Programação de Aplicação (UFC, 2026.2)

Escopo:
  - Devolve matrículas, infraestrutura e desempenho médio por turma
  - NÃO inclui: dados individuais por aluno, comparação com outras
    escolas/município, série histórica ou painel visual.

Documentação interativa gerada automaticamente em:
  http://127.0.0.1:8000/docs
"""

from fastapi import FastAPI, HTTPException
from fastapi.responses import RedirectResponse

from models import Matriculas, Infraestrutura, DesempenhoResponse
import data

app = FastAPI(
    title="API Escola Dalva Pontes da Rocha",
    description=(
        "API pública que devolve dados de matrículas, infraestrutura e "
        "desempenho médio por turma da Escola Dalva Pontes da Rocha "
        "(Caucaia/CE), com base em dados da Prefeitura de Caucaia e "
        "avaliações internas agregadas por turma."
    ),
    version="0.1.0",
)


@app.get("/", include_in_schema=False)
def raiz():
    return RedirectResponse(url="/docs")


@app.get(
    "/matriculas",
    response_model=Matriculas,
    tags=["Matrículas"],
    summary="Retorna os dados de matrículas da escola",
)
def obter_matriculas():
    return data.MATRICULAS


@app.get(
    "/infraestrutura",
    response_model=Infraestrutura,
    tags=["Infraestrutura"],
    summary="Retorna os dados de infraestrutura da escola",
)
def obter_infraestrutura():
    """
    Retorna informações estruturais da escola: número de salas,
    presença de laboratório, biblioteca, quadra, acessibilidade
    e internet.

    Fonte: Prefeitura de Caucaia (licença de uso em verificação).
    """
    return data.INFRAESTRUTURA


@app.get(
    "/desempenho-turmas",
    response_model=DesempenhoResponse,
    tags=["Desempenho"],
    summary="Retorna o desempenho médio agregado por turma",
)
def obter_desempenho_turmas(etapa: str | None = None):
    """
    Retorna a média de desempenho nas avaliações mais recentes,
    agregada por turma. Nenhum aluno é identificado individualmente.

    Parâmetros opcionais:
      - etapa: filtra por etapa de ensino
        (ex.: "Anos Iniciais" ou "Anos Finais")
    """
    resultado = data.DESEMPENHO

    if etapa:
        turmas_filtradas = [
            t for t in resultado["turmas"] if t["etapa"].lower() == etapa.lower()
        ]
        if not turmas_filtradas:
            raise HTTPException(
                status_code=404,
                detail=f"Nenhuma turma encontrada para a etapa '{etapa}'.",
            )
        resultado = {**resultado, "turmas": turmas_filtradas}

    return resultado
