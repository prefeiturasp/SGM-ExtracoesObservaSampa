# ObservaSampa: Automação de indicadores
## Informações do processo
* **Processo:** Base de dados de Servidores Ativos da Prefeitura de São Paulo
* **Versão:** 1.0
* **Objetivo:** Atualizar as variáveis do ObservaSampa que compõem os indicadores relacionados à base de Servidores Ativos da Prefeitura de São Paulo.

## Fontes
O [Portal de Dados Abertos](http://dados.prefeitura.sp.gov.br/) possui o conjunto de dados [Relação de Servidores Ativos da Prefeitura de São Paulo](http://dados.prefeitura.sp.gov.br/dataset/servidores-ativos-da-prefeitura) o qual lista a base de dados com diversas informações sobre todos os funcionários ativos da Administração Direta da Prefeitura de São Paulo, tais como nomes, cargos, órgão de lotação e perfil (sexo, idade, raça).

Devem ser utilizadas as bases [Base de dados - Funcionalismo](http://dados.prefeitura.sp.gov.br/dataset/servidores-ativos-da-prefeitura/resource/a7296f88-2223-47a0-8b76-3fc743b6bd72) referentes a dezembro de cada ano.


## Destinos

Este processo tem como destino a criação da planilha com informações das variáveis (V0199, V0200, V0266, V0267, V0514, V0518, V0519, V0520, V0521, V0522, V0525, V0821) formatada no template de importação do Intranet do ObservaSampa. Sendo uma tabela com as respectivas colunas: Variável, Região e Período (ver detalhes adiante na tabela de mapeamento).

Região analisada: Município de São Paulo.

## Frequência de execução

Espera-se executar esse processo anualmente com informações de dezembro do último ano disponível.

## Descrição do processo

### Para a variável V0199 (Servidores municipais ativos da administração direta do governo):
1. Para cada ano, baixar o arquivo csv de dezembro do conjunto de dados no seguinte formato “Base de dados - Funcionalismo - Mês de referência: dezembro de {ANO}" [Relação de Servidores Ativos da Prefeitura de São Paulo](http://dados.prefeitura.sp.gov.br/dataset/servidores-ativos-da-prefeitura) (Obs.: Baixar somente o arquivo de dezembro do último ano disponível, caso o objetivo seja apenas a atualização do último ano e não baixar a série inteira);
1. Contar a quantidade de linhas totais do arquivo desconsiderando qualquer filtro;
1. Retornar valor inteiro.

### Para a variável V0200 (Servidores ativos da administração direta do governo municipal que se autodeclaram com deficiência): 
1. No mesmo arquivo;
1. Contar a quantidade de linhas filtrando "SIM" da coluna "DEFICIENTE";
1. Retornar valor inteiro.

### Para a variável V0266 (Servidoras ativas da administração direta do governo): 
1. No mesmo arquivo;
1. Contar a quantidade de linhas filtrando "F" da coluna "SEXO";
1. Retornar valor inteiro.

### Para a variável V0267 (Servidores ativos da administração direta do governo municipal que se autodeclaram negros): 
1. No mesmo arquivo;
1. Contar a quantidade de linhas filtrando "PRETA" e "PARDA" da coluna "RACA";
1. Retornar valor inteiro.

### Para a variável V0514 (Servidoras da administração direta ativa com deficiência): 
1. No mesmo arquivo;
1. Contar a quantidade de linhas filtrando "F" da coluna "SEXO" e "SIM" da coluna "DEFICIENTE";
1. Retornar valor inteiro.

### Para a variável V0518 (Número de servidoras municipais ativas pretas): 
1. No mesmo arquivo;
1. Contar a quantidade de linhas filtrando "F" da coluna "SEXO" e "PRETA" da coluna "RACA";
1. Retornar valor inteiro.

### Para a variável V0519 (Número de servidoras municipais ativas pardas): 
1. No mesmo arquivo;
1. Contar a quantidade de linhas filtrando "F" da coluna "SEXO" e "PARDA" da coluna "RACA";
1. Retornar valor inteiro.

### Para a variável V0520 (Número de servidoras municipais ativas indígenas): 
1. No mesmo arquivo;
1. Contar a quantidade de linhas filtrando "F" da coluna "SEXO" e "INDIGENA" da coluna "RACA";
1. Retornar valor inteiro.

### Para a variável V0521 (Número de servidoras municipais ativas amarelas): 
1. No mesmo arquivo;
1. Contar a quantidade de linhas filtrando "F" da coluna "SEXO" e "AMARELA" da coluna "RACA";
1. Retornar valor inteiro.

### Para a variável V0522 (Número de servidoras municipais ativas brancas): 
1. No mesmo arquivo;
1. Contar a quantidade de linhas filtrando "F" da coluna "SEXO" e "BRANCA" da coluna "RACA";
1. Retornar valor inteiro.

### Para a variável V0525 (Número de ingressos de servidores(as) efetivos(as) na Prefeitura): 
1. No mesmo arquivo;
1. Identificar o ano da coluna "DATA_INICIO_EXERC";
1. Contar a quantidade de linhas filtrando da coluna "DATA_INICIO_EXERC" somente o ano que está sendo analisado, o objetivo é identificar o total de ingressos no ano;
1. Retornar valor inteiro.

### Para a variável V0821 (Número de servidores ativos homens): 
1. No mesmo arquivo;
1. Contar a quantidade de linhas filtrando "M" da coluna "SEXO";
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
