# FIAP - CAP 1 - Fase 2

Projeto de modelagem de um sistema de gerenciamento de pouso para uma base espacial em Marte. A aplicacao organiza modulos em uma fila de pouso, calcula prioridade, ordena a fila e valida se cada modulo pode pousar com seguranca.

O sistema foi desenvolvido em Python usando estruturas low-level, principalmente uma fila implementada manualmente em `modulos/fila.py`.

## Objetivo

O objetivo do projeto e simular o processo de decisao do MGPEB, o Modulo de Gerenciamento de Pouso da Base Espacial.

O MGPEB recebe modulos com diferentes tipos de carga, combustivel, massa e criticidade. Depois disso, ele:

1. cadastra os modulos;
2. classifica modulos em alerta ou espera;
3. calcula prioridade de pouso;
4. ordena a fila usando merge sort;
5. tenta pousar cada modulo;
6. separa os modulos entre pousados e em alerta.

## Estrutura

```text
.
+-- main.py
+-- fase2_mgpeb.py
+-- relatorio.ipynb
+-- modulos
|   +-- fila.py
|   +-- modulo.py
+-- README.md
```

## Principais classes

### `Modulos`

Representa cada modulo que precisa pousar na base.

Atributos principais:

- `nome`: identificacao do modulo.
- `tipo`: tipo de carga ou funcao.
- `combustivel`: percentual de combustivel disponivel.
- `massa`: massa do modulo em kg.
- `criticidade`: importancia operacional do modulo.
- `prioridade`: nota calculada de 0 a 10.
- `pouso`: indica se o modulo pousou.
- `pronto_pouso`: indica se o modulo foi aprovado para pouso.
- `hora_pouso`: horario definido automaticamente caso nao seja informado.

### `MGPEB`

Gerencia a fila e o processo de pouso.

Estruturas usadas:

- `lista_modulos`: todos os modulos cadastrados.
- `fila_pouso`: fila principal de pouso.
- `pousados`: modulos que pousaram com sucesso.
- `em_alerta`: modulos com falha ou risco operacional.
- `em_espera`: modulos com prioridade alta.

## Como executar

Execute o arquivo principal:

```bash
python main.py
```

O programa vai exibir:

- maior e menor prioridade;
- maior e menor combustivel;
- maior e menor massa;
- busca por tipo de carga;
- fila antes e depois da ordenacao;
- resultado da tentativa de pouso de cada modulo;
- simulacao matematica da descida em Marte.

## Ordenacao da fila de pouso

A fila de pouso e ordenada por prioridade usando merge sort.

A prioridade considera:

- criticidade;
- combustivel;
- massa.

Quanto maior a prioridade, mais cedo o modulo deve ser processado na fila.

## Bloqueio de pouso

O pouso segue uma regra conservadora: o modulo so pousa se todas as condicoes criticas forem verdadeiras.

A expressao logica usada e:

```text
AUTORIZAR POUSO = C AND A AND P AND S AND R AND H AND V
```

Ou seja, se qualquer uma das condicoes falhar, o pouso e bloqueado.

## Pontos observados para bloquear o pouso

Atualmente, a funcao `pousar()` verifica os seguintes pontos:

| Variavel | Condicao observada | Regra de bloqueio |
| --- | --- | --- |
| C | Combustivel suficiente | Bloqueia se `combustivel < 20` |
| A | Alinhamento de rota seguro | Bloqueia se `alinhamento_rota` for `False` |
| P | Pressao atmosferica dentro do limite | Bloqueia se `pressao_atmosferica_ok` for `False` |
| S | Sistemas operacionais | Bloqueia se `sistemas_ok` for `False` |
| R | Radiacao em nivel seguro | Bloqueia se `radiacao_ok` for `False` |
| H | Altura de pouso segura | Bloqueia se `altura_pouso_segura` for `False` |
| V | Velocidade de descida segura | Bloqueia se `velocidade_descida > 10` |

Quando o pouso nao e possivel, o sistema imprime o motivo e adiciona o modulo na lista `em_alerta` do MGPEB.

Exemplo de saida:

```text
Pouso do modulo Energia-01 nao foi possivel por: combustivel suficiente, alinhamento de rota seguro, sistemas operacionais.
```

Quando o pouso e aprovado, o modulo e adicionado na lista `pousados`.

Exemplo:

```text
Modulo Med-01 pousou com sucesso.
```

## Geracao automatica das variaveis de pouso

Algumas variaveis ja existem no modulo, como `combustivel` e `hora_pouso`.

As variaveis que ainda nao existem sao geradas automaticamente pela classe `Modulos`, sem necessidade de manipulacao manual no `main.py`.

Variaveis geradas automaticamente:

- `alinhamento_rota`;
- `pressao_atmosferica_ok`;
- `sistemas_ok`;
- `radiacao_ok`;
- `altura_pouso_segura`;
- `velocidade_descida`.

Essa geracao acontece dentro de `_gerar_variaveis_pouso()`. Para manter o comportamento previsivel, os valores aleatorios usam uma semente baseada no nome do modulo.

## Fluxo de pouso

1. Os modulos sao criados.
2. O MGPEB classifica cada modulo.
3. A fila e ordenada por prioridade.
4. `modulos_pousar()` percorre a fila.
5. Para cada modulo, a funcao `pousar()` valida as condicoes criticas.
6. Se todas forem aprovadas, o modulo vai para `pousados`.
7. Se alguma falhar, o modulo vai para `em_alerta`.

## Complexidades implementadas

- Busca por maior valor: `O(n)`.
- Busca por menor valor: `O(n)`.
- Busca por tipo de carga: `O(n)`.
- Ordenacao por merge sort: `O(n log n)`.

## Arquivo de apoio

O arquivo `relatorio.ipynb` documenta a modelagem do cenario de pouso, a logica booleana usada para autorizacao e bloqueio, alem das funcoes matematicas aplicadas a descida em Marte.
