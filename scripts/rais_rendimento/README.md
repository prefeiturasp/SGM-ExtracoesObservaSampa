# ObservaSampa: Automação de indicadores
## Informações do processo
***Processo:** Base de dados da RAIS - Rendimento
***Versão:** 1.0
***Objetivo:** Atualizar as variáveis do ObservaSampa que compõem os indicadores relacionados à base de dados da RAIS (Relação Anual das Informações Sociais) para rendimento no Município de São Paulo.

## Fontes
O [Ministério do Trabalho](http://pdet.mte.gov.br/rais) divulga os dados da RAIS em formato de Microdados [Microdados RAIS e CAGED](http://pdet.mte.gov.br/microdados-rais-e-caged) em que é possível analisar os dados de rendimento do trabalho formal no Município de São Paulo.

A base de dados é atualizada anualmente e é possível acessar através do link ftp://ftp.mtps.gov.br/pdet/microdados/.

Os dados são divulgados com defasagem aproximada de 1 ano. Exemplo: no final de 2022 foram divulgados os dados referentes ao ano de 2021.

## Destinos

Este processo tem como destino a criação da planilha com informações das variáveis (V0805, V0331, V0332, V0333, V0334) formatada no template de importação do Intranet do ObservaSampa. Sendo uma tabela com as respectivas colunas: Variável, Região e Período (ver detalhes adiante na tabela de mapeamento).

Regiões analisadas: Município de São Paulo.

## Frequência de execução

Espera-se executar esse processo anualmente com informações do último ano disponível.

## Descrição do processo

### Para a variável V0805 (Renda Média do Emprego Formal (R$)):
1. Para cada ano, baixar o arquivo correspondente no conjunto de dados dos [Microdados RAIS e CAGED](http://pdet.mte.gov.br/microdados-rais-e-caged). Até o ano de 2017 baixar o arquivo: SP{ANO}. A partir de 2018 baixar o arquivo: RAIS_VINC_PUB_SP;
1. Selecionar: coluna ‘Município’=355030 e coluna 'Vínculo Ativo 31/12'= 1, dessa forma, considera-se apenas os vínculos no Município de São Paulo ativos em 31/12;
1. Da coluna "Faixa Remun Dezem (SM)" desconsiderar os valores não classificados;
1. Da coluna "Vl Remun Dezembro Nom", calcular a média dos valores;
1. Retornar valor decimal.

### Para a variável V0331 (Rendimento médio nominal do trabalho entre as mulheres):
1. No mesmo arquivo;
1. Repetir segundo procedimento da variável anterior;
1. Repetir terceiro procedimento da variável anterior;
1. Filtrar da coluna "Sexo Trabalhador", "2";
1. Da coluna "Vl Remun Dezembro Nom", calcular a média dos valores;
1. Retornar valor decimal.

### Para a variável V0332 (Rendimento médio nominal do trabalho entre os homens): 
1. No mesmo arquivo;
1. Repetir segundo procedimento da variável anterior;
1. Repetir terceiro procedimento da variável anterior;
1. Filtrar da coluna "Sexo Trabalhador", "1";
1. Da coluna "Vl Remun Dezembro Nom", calcular a média dos valores;
1. Retornar valor decimal.

### Para a variável V0333 (Rendimento médio nominal do trabalho entre os negros): 
1. No mesmo arquivo;
1. Repetir segundo procedimento da variável anterior;
1. Repetir terceiro procedimento da variável anterior;
1. Filtrar da coluna "Raça Cor", "4" e "8";
1. Da coluna "Vl Remun Dezembro Nom", calcular a média dos valores;
1. Retornar valor decimal.

### Para a variável V0334 (Rendimento médio nominal do trabalho entre os não negros): 
1. No mesmo arquivo;
1. Repetir segundo procedimento da variável anterior;
1. Repetir terceiro procedimento da variável anterior;
1. Filtrar da coluna "Raça Cor", "1", "2" e "6";
1. Da coluna "Vl Remun Dezembro Nom", calcular a média dos valores;
1. Retornar valor decimal.




## Tabela de mapeamento dos dados

| Campo | Descrição | Tipo do dado | Tabela de origem | Campo de origem | Regra de transformação |
| ----- | --------- | ------------ | :--------------: | :-------------: | :--------------------: |
| Variável | Preencher com os nomes resumidos das variáveis, no caso desse processo, uma linha para cada variável | String | N/A | N/A | N/A |
| Região | Preencher com a sigla da região, por exemplo M00 para o município de São Paulo  | String | N/A | N/A | N/A |
| Ano | Preencher o cabeçalho com o valor do ano, de acordo com o arquivo de origem, por exemplo 2020. Preencher as linhas de valores de acordo com o resultado obtido na contagem das linhas dos arquivos (ver descrição do processo acima) | String | N/A | N/A | N/A |


### Regras de transformações
Não se aplica

## Dependências (pré-requisitos e premissas)
Preenchido após desenvolvimento do script de automatização.

## Considerações sobre recuperação ou reinício
Preenchido após desenvolvimento do script de automatização.

## Considerações sobre registros rejeitados na carga
Preenchido após desenvolvimento do script de automatização.
