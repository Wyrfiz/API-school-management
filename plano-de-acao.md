# Plano de ação — modelo

Rascunho em 11/09, versão final no Marco 1 (02/10). O roteiro completo, com exemplos e o critério de
cada campo, está no PDF `extensao/plano-de-acao.pdf` — leia antes de preencher.

**Duas páginas bastam.** Plano longo costuma esconder escopo mal resolvido. O que estiver aqui é o
que será cobrado nos três marcos.

---

## Identificação

- **Equipe:** Kayo - 493552
- **Trilha:** (A) API pública de dados abertos
- **Área temática da PREX:** Tecnologia e Produção
- **Por que essa área,** em uma linha: Em conversa com a coordenadora de uma escola ela me explicou que tinha dificuldades de armazenar e buscar dados de servidores e alunos além de uma análise mais aprofundada das aptidões dos alunos
- **Repositório:** https://github.com/Wyrfiz/API-school-management

## Campo 1 — O problema

"Precisamos de Reavaliar a situação dos alunos com relação ao SPAECE, dado que as informações que tivemos do grau de aptidão em português e matemática no incio do ano não ficou clara"
dito isso pretendo fazer a API para auxiliar na gestão de servidores (como bônus) e na análise e criação de perfil dos alunos da escola.

## Campo 2 — O público externo

Quem é, onde está, quantos são.

- **Quem é:** funcionários da escola, Dalva Pontes da Rocha
- **Duas ou três pessoas reais desse grupo:** as Coordenadoras, Isabel e Kátia
- **Já falamos com alguma? Quando falaremos?** Já entrei em contato com as coordenadoras, e conseguimos a autorização, mas não temos os dados ainda
- **Como essa pessoa vai descobrir que o produto existe:**
será entregue o link para o gestor e ele utilizará para fazer as análises necessárias

## Campo 3 — Trilha e produto

- **O que é, em uma frase que caiba num tuíte, e onde ficará publicado:**
Uma API pública que devolve, para a escola [nome], dados de matrículas e infraestrutura do censo escolar mais recente, com documentação e exemplo pronto para copiar, publicada em [endereço do repositório/link].

- **O que NÃO faz parte:**
Não inclui análise comparativa com outras escolas ou média do município, não inclui série histórica de anos anteriores, e não inclui painel visual (dashboard) — apenas os dados estruturados via API.

## Campo 4 — Fontes de dados

Uma tabela por fonte.

| | |
| :-- | :-- |
| Nome e órgão | |
| Endereço | |
| Licença — e o que ela permite ao nosso produto | |
| Atualização — periodicidade declarada e data do dado mais recente | |
| Dado pessoal? — se sim, granularidade e o que será agregado | |

## Campo 5 — Papéis

Um por integrante, com responsabilidade verificável. Quando um papel girar, registre no diário.

| Integrante | Papel | O que fica sob sua responsabilidade |
| :-- | :-- | :-- |
| | | |
| | | |
| | | |

## Campo 6 — Cronograma

Uma frase por marco, dizendo o que estará pronto. Nada de "avançar no projeto".

| Data | O que estará pronto |
| :-- | :-- |
| 02/10 (Marco 1) | |
| 13/11 (Marco 2) | |
| 27/11 (Marco 3) | |
| 04/12 (Socialização) | |

**Dependências externas.** O que depende de terceiro (cadastro, chave de acesso, autorização,
resposta de parceiro) e o que fazemos se falhar. Faça *esta semana* o pedido que demora.

## Campo 7 — Indicadores

Defina agora, antes de executar. Indicador sem instrumento de coleta é intenção. Cada coleta vira
depois uma linha do `evidencias.csv`.

| | Medida | Como será coletada | Valor que seria bom |
| :-- | :-- | :-- | :-- |
| Contagem | | | |
| Qualitativa | | | |

## Antes de entregar: a prova dos nove

- [ ] Riscamos tudo o que não conseguiríamos terminar até 13/11.
- [ ] O que sobrou ainda ajuda alguém.
- [ ] Uma pessoa de fora entende o Campo 1 e o Campo 3 sem explicação oral.
- [ ] A data da primeira conversa com o público está marcada.
- [ ] Os indicadores podem ser coletados sem depender de terceiro.

---

## Exemplo de campo preenchido

Para calibrar o tamanho e o tom — é o nível de concretude esperado, não um modelo a copiar.

> **Campo 1 — O problema.** Uma coordenadora pedagógica que quer comparar sua escola com a média do
> município precisa baixar uma planilha de 300 mil linhas e saber filtrar.
>
> **Campo 3 — Trilha e produto.** Uma API pública que devolve, por escola de Fortaleza, matrículas e
> infraestrutura do censo mais recente, com documentação e exemplo pronto para copiar. **Não** inclui
> série histórica nem painel visual.
>
> **Campo 7 — Indicadores.** Contagem: acessos únicos ao endereço público, pelo registro do
> servidor, entre 02/10 e 27/11; seria bom passar de 30. Qualitativa: retorno escrito de pelo menos
> duas pessoas de fora que usaram, coletado por e-mail depois do primeiro contato.
