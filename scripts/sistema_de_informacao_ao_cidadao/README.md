# ObservaSampa: Automação de indicadores
## Informações do processo
* **Processo:** Base de dados do Sistema de Informação ao Cidadão (SIC) 
* **Versão:** 1.0
* **Objetivo:** Atualizar as variáveis do ObservaSampa que compõem os indicadores relacionados à base do Sistema de Informação ao Cidadão (SIC).

## Fontes
O [Portal de Dados Abertos](http://dados.prefeitura.sp.gov.br/) possui o conjunto de dados [Pedidos de informação protocolados à Prefeitura via sistema e-SIC](http://dados.prefeitura.sp.gov.br/dataset/pedidos-de-informacao-protocolados-a-prefeitura-via-e-sic1) o qual lista a base de dados com diversas informações sobre .

Devem ser utilizadas as bases [Base de Pedidos de Informação]http://dados.prefeitura.sp.gov.br/dataset/pedidos-de-informacao-protocolados-a-prefeitura-via-e-sic1/resource/4c1e1580-5c0a-4f8a-8da9-7adb305f6a0b) de cada ano.


## Destinos

Este processo tem como destino a criação da planilha com informações das variáveis (V0441, V0442, V0457, V0458 e V0461) formatada no template de importação do Intranet do ObservaSampa. Sendo uma tabela com as respectivas colunas: Variável, Região e Período (ver detalhes adiante na tabela de mapeamento).

Região analisada: Município de São Paulo.

## Frequência de execução

Espera-se executar esse processo anualmente com informações do último ano disponível.

## Descrição do processo

### Para a variável V0441 (Número de recursos registrados no sistema de informação ao cidadão):
1. Para cada ano, baixar o arquivo do conjunto de dados no seguinte formato “Base de Pedidos de Informação {ANO}" [Pedidos de informação protocolados à Prefeitura via sistema e-SIC](http://dados.prefeitura.sp.gov.br/dataset/pedidos-de-informacao-protocolados-a-prefeitura-via-e-sic1) (Obs.: Baixar somente o arquivo do último ano disponível, caso o objetivo seja apenas a atualização do último ano e não baixar a série inteira);
1. Filtrar opções que contenham "1ª instância", "2ª instância" e "3ª instância" da coluna "dc_status_pedido" e contar a quantidade de registros exclusivos da coluna "cd_pedido";
1. Retornar valor inteiro.

### Para a variável V0442 (Total de pedidos de acesso à informação registrados pelos cidadãos(ãs) no Sistema de Acesso à Informação (SIC)):
1. No mesmo arquivo;
1. Contar a quantidade de registros exclusivos da coluna "cd_pedido";
1. Retornar valor inteiro.

### Para a variável V0457 (Total de pedidos de acesso à informação negados no Sistema de Informação ao Cidadão (SIC)): 
1. No mesmo arquivo;
1. Contar a quantidade de linhas filtrando "Pedido indeferido" da coluna "dc_status_pedido";
1. Retornar valor inteiro.

### Para a variável V0458 (Total de pedidos de acesso à informação registrados no Sistema de Acesso à Informação (SIC)): 
1. No mesmo arquivo;
1. Contar a quantidade de registros exclusivos da coluna "cd_pedido";
1. Retornar valor inteiro. 

### Para a variável V0461 (Total de pedidos de acesso à informação respondidos no Sistema de Informação ao Cidadão (SIC) na fase inicial de atendimento): 
1. No mesmo arquivo;
1. Contar a quantidade de linhas filtrando "Atendido" da coluna "dc_status_pedido";
1. Retornar valor inteiro.



## Tabela de mapeamento dos dados

| Campo | Descrição | Tipo do dado | Tabela de origem | Campo de origem | Regra de transformação |
| ----- | --------- | ------------ | :--------------: | :-------------: | :--------------------: |
| Variável | Preencher com os nomes resumidos das variáveis, no caso desse processo, uma linha para cada variável | String | N/A | N/A | N/A |
| Região | Preencher com a sigla da região do município de São Paulo, no caso desse processo, M00  | String | N/A | N/A | N/A |
| Ano | Preencher o cabeçalho com o valor do ano, de acordo com o arquivo de origem, por exemplo 2022. Preencher as linhas de valores de acordo com o resultado obtido na contagem das linhas dos arquivos (ver descrição do processo acima) | String | N/A | N/A | N/A |

### Regras de transformações
Não se aplica

## Dependências (pré-requisitos e premissas)
Preenchido após desenvolvimento do script de automatização.

## Considerações sobre recuperação ou reinício
Preenchido após desenvolvimento do script de automatização.

## Considerações sobre registros rejeitados na carga
Preenchido após desenvolvimento do script de automatização.
