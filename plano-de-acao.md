# Plano de ação — CC0464

## Identificação

**Equipe:** Kayo — 493552;
**Trilha:** (A) API pública de dados abertos
**Área temática da PREX:** Tecnologia e Produção (ou Tecnologia)
**Por que essa área, em uma linha:** tenho ligação com pessoas da educação e quero ajudar aos educadores no seus métodos de análises e consequentemente nos ensinos
**Repositório:** (https://github.com/Wyrfiz/API-school-management)

## Campo 1 — O problema

Uma coordenadora pedagógica que precisa consultar matrícula, infraestrutura, docentes e desempenho da escola tem que cruzar manualmente o Censo Escolar do INEP com os boletins do SPAECE, dois arquivos e dois formatos diferentes.

## Campo 2 — O público externo

- **Quem é:** gestores e coordenadores pedagógicos da Escola Municipal Dalva Pontes da Rocha (Caucaia/CE)
- **Duas ou três pessoas reais desse grupo:** coordenadoras Isabel e Kátia
- **Já falamos com alguma? Quando falaremos?** Sim, contato já feito com coordenadoria e diretoria; obtivemos autorização e um sinal positivo de dentro do colégio
- **Como essa pessoa vai descobrir que o produto existe:** o link da API será entregue diretamente ao gestor, que o utilizará para suas análises

## Campo 3 — Trilha e produto

- **O que é, em uma frase que caiba num tuíte, e onde ficará publicado:** Uma API pública que devolve, para a Escola Dalva Pontes da Rocha, dados de matrícula, infraestrutura e docentes (Censo Escolar INEP) e resultados de proficiência (SPAECE/SEDUC), com documentação e exemplo pronto para copiar, publicada em (https://github.com/Wyrfiz/API-school-management).
- **O que NÃO faz parte:** Não inclui dado de aluno individual, não inclui comparação com outras escolas ou com a média do município, não inclui série histórica de anos anteriores, e não inclui painel visual (dashboard).

## Campo 4 — Fontes de dados

| | Fonte 1 | Fonte 2 |
|---|---|---|
| **Nome e órgão** | Censo Escolar — INEP | SPAECE — SEDUC-CE |
| **Endereço** | (https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/microdados/censo-escolar) | https://prototipos.caeddigital.net/arquivos/ce/colecoes/2025/SPAECE_2025_RR%20Web.pdf |
| **Licença — o que permite ao produto** | Aberta (dados públicos) — permite uso e redistribuição | Pública — confirmar termos de reuso no site da SEDUC |
| **Atualização — periodicidade x dado mais recente** | Anual / 2025 | Anual, por ciclo avaliativo / 2025 |
| **Dado pessoal?** | Não — agregado por escola | Não — proficiência agregada por escola |

## Campo 5 — Papéis

| Integrante | Papel | O que fica sob sua responsabilidade |
|---|---|---|
| Kayo | Tudo

## Campo 6 — Cronograma

| Data | O que estará pronto |
|---|---|
| **02/10 (Marco 1)** | Plano de ação finalizado; repositório criado; microdados corretos do INEP e do SPAECE para a escola localizados e validados |
| **13/11 (Marco 2)** | Dados do Censo e do SPAECE tratados; API funcional entregando os dois endpoints, com documentação básica |
| **27/11 (Marco 3)** | API revisada, exemplos testados, documentação completa; validação com as coordenadoras sobre a utilidade real dos dados |
| **04/12 (Socialização)** | Apresentação da API e dos resultados, com feedback registrado das coordenadoras/gestor |

**Dependências externas:** confirmação dos termos de reuso dos dados do SPAECE no site da SEDUC (pedido a ser feito esta semana); se a resposta demorar, seguir com os dados do Censo INEP isoladamente e adicionar o SPAECE assim que confirmado.

## Campo 7 — Indicadores

| Medida | Como será coletada | Valor que seria bom |
|---|---|---|
| Contagem | Acessos únicos ao endereço público da API, pelo registro do servidor, entre 02/10 e 27/11 | Passar de 30 |
| Qualitativa | Retorno escrito das coordenadoras Isabel e/ou Kátia sobre a utilidade dos dados entregues, coletado por e-mail após uso | Confirmam que a API resolve a consulta que faziam manualmente |

## Antes de entregar: a prova dos nove

- [ ] Riscamos tudo o que não conseguiríamos terminar até 13/11
- [ ] O que sobrou ainda ajuda alguém
- [ ] Uma pessoa de fora entende o Campo 1 e o Campo 3 sem explicação oral
- [ ] A data da primeira conversa com o público está marcada
- [ ] Os indicadores podem ser coletados sem depender de terceiro
