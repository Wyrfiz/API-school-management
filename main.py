"""
API pública de dados abertos — Escola Dalva Pontes da Rocha
CC0464 - Interfaces de Programação de Aplicação (UFC, 2026.2)

Escopo (conforme Campo 3 do plano de ação):
  - Devolve matrículas, infraestrutura e desempenho médio por turma
  - NÃO inclui: dados individuais por aluno, comparação com outras
    escolas/município, série histórica ou painel visual.

Documentação interativa gerada automaticamente em:
  http://127.0.0.1:8000/docs
"""

from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import RedirectResponse, JSONResponse
from fastapi.exceptions import RequestValidationError

from models import Matriculas, Infraestrutura, DesempenhoResponse, ErroPadrao
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


MENSAGENS_PADRAO = {
    400: "Requisição inválida.",
    404: "Recurso não encontrado.",
    422: "Parâmetros inválidos na requisição.",
    500: "Erro interno no servidor. Tente novamente mais tarde.",
}


def _corpo_erro(codigo: int, detalhe: str) -> dict:
    return {
        "erro": MENSAGENS_PADRAO.get(codigo, "Erro."),
        "detalhe": detalhe,
        "codigo": codigo,
    }


@app.exception_handler(HTTPException)
async def handler_http_exception(request: Request, exc: HTTPException):
    """Padroniza qualquer HTTPException levantada (404, 400, etc.)."""
    return JSONResponse(
        status_code=exc.status_code,
        content=_corpo_erro(exc.status_code, str(exc.detail)),
    )


@app.exception_handler(RequestValidationError)
async def handler_validation_error(request: Request, exc: RequestValidationError):
    """Padroniza erros de validação de parâmetros (422)."""
    return JSONResponse(
        status_code=422,
        content=_corpo_erro(422, "Um ou mais parâmetros enviados são inválidos."),
    )


@app.exception_handler(Exception)
async def handler_erro_generico(request: Request, exc: Exception):
    """Captura qualquer erro não previsto e evita expor detalhes internos (500)."""
    return JSONResponse(
        status_code=500,
        content=_corpo_erro(500, "Erro interno no servidor. Tente novamente mais tarde."),
    )


@app.get("/", include_in_schema=False)
def raiz():
    # Redireciona a raiz para a documentação interativa
    return RedirectResponse(url="/docs")


@app.get(
    "/matriculas",
    response_model=Matriculas,
    tags=["Matrículas"],
    summary="Retorna os dados de matrículas da escola",
    responses={500: {"model": ErroPadrao, "description": "Erro interno no servidor"}},
)
def obter_matriculas():
    """
    Retorna o total de alunos matriculados no ano letivo vigente,
    separado por etapa de ensino.

    Fonte: Prefeitura de Caucaia (licença de uso em verificação).
    """
    return data.MATRICULAS


@app.get(
    "/infraestrutura",
    response_model=Infraestrutura,
    tags=["Infraestrutura"],
    summary="Retorna os dados de infraestrutura da escola",
    responses={500: {"model": ErroPadrao, "description": "Erro interno no servidor"}},
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
    responses={
        404: {"model": ErroPadrao, "description": "Nenhuma turma encontrada para a etapa informada"},
        422: {"model": ErroPadrao, "description": "Parâmetro 'etapa' inválido"},
        500: {"model": ErroPadrao, "description": "Erro interno no servidor"},
    },
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
