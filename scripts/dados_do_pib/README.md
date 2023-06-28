# ObservaSampa: Automação de indicadores
## Informações do processo
* **Processo:** Base de dados do PIB
* **Versão:** 1.0
* **Objetivo:** Atualizar as variáveis do ObservaSampa que compõem os indicadores relacionados à base de dados do PIB.

## Fontes
O [Repositório SEADE](https://repositorio.seade.gov.br/) possui o conjunto de dados [PIB Municipal 2002-2020](https://repositorio.seade.gov.br/dataset/pib-municipal-2002-2018) o qual apresenta dados do Valor Adicionado total e desagregado por setores, dos Impostos, do PIB e do PIB per capita para os Municípios do Estado de São Paulo.

Anualmente são inseridas bases como de [Tabela - PIB 2020](https://repositorio.seade.gov.br/dataset/1bd90672-72a8-47cb-a34d-ab9eb703735d/resource/13af6a0f-e731-4fc7-8664-73e57de8f465/download/pib-municipios-2020.xlsx) que deve ser empregada para a automação.

Os dados são divulgados com defasagem de 2 anos. Exemplo: no final de 2022 foram diviulgados os dados referentes ao ano de 2020.

O [Repositório SEADE](https://repositorio.seade.gov.br/) possui também conjunto de dados [PIB Anual 2002 - 2020](https://repositorio.seade.gov.br/dataset/pib-anual-2002-2020) o qual apresenta dados do PIB do Brasil e do Deflator do PIB, que são usados para os cálculos de variáveis desta documentação.

## Destinos

Este processo tem como destino a criação da planilha com informações das variáveis (V0169, V0812, V0813, V0814, V0815, V0816, V0819 e V0820) formatada no template de importação do Intranet do ObservaSampa. Sendo uma tabela com as respectivas colunas: Variável, Região e Período (ver detalhes adiante na tabela de mapeamento).

Região analisada: Município de São Paulo.

## Frequência de execução

Espera-se executar esse processo anualmente com informações do último ano disponível.

## Descrição do processo

### Para a variável V0169 (Produto Interno Bruto (PIB) a preços correntes):
1. Para cada ano, baixar o arquivo correspondente no conjunto de dados do PIB do Repositório SEADE no seguinte formato “Tabela – PIB {ANO}” [Tabela - PIB 2020](https://repositorio.seade.gov.br/dataset/1bd90672-72a8-47cb-a34d-ab9eb703735d/resource/13af6a0f-e731-4fc7-8664-73e57de8f465/download/pib-municipios-2020.xlsx); (Obs.: Baixar somente o arquivo do último ano disponível, caso o objetivo seja apenas a atualização do último ano e não baixar a série inteira);
1. Pegar o valor correspondente à linha "São Paulo" e coluna "PIB (1)";
1. Retornar valor inteiro.

### Para a variável V0812 (Valor adicionado bruto da Agropecuária, a preços correntes (R$ 1.000)): 
1. No mesmo arquivo;
1. Pegar o valor correspondente à linha "São Paulo" e coluna "Agropecuária";
1. Retornar valor inteiro.

### Para a variável V0813 (Valor adicionado bruto da Indústria, a preços correntes (R$ 1.000)): 
1. No mesmo arquivo;
1. Pegar o valor correspondente à linha "São Paulo" e coluna "Indústria";
1. Retornar valor inteiro.

### Para a variável V0814 (Valor adicionado bruto dos Serviços, a preços correntes (R$ 1.000)): 
1. No mesmo arquivo;
1. Pegar o valor correspondente à soma da linha "São Paulo" e coluna "Administração Pública" com a linha "São Paulo" e coluna "Total  (exclusive Administração Pública)";
1. Retornar valor inteiro.

### Para a variável V0815 (Valor adicionado bruto total, a preços correntes (R$ 1.000)): 
1. No mesmo arquivo;
1. Pegar o valor correspondente à linha "São Paulo" e coluna "Total geral";
1. Retornar valor inteiro.

### Para a variável V0816 (Produto Interno Bruto (PIB) do Município, valores reais (R$ 1.000)): 
1. Baixar o arquivo "PIB - 2002 a 2020" do Repositório SEADE [PIB Anual 2002 - 2020](https://repositorio.seade.gov.br/dataset/pib-anual-2002-2020);
1. Na aba "Tabela 18", baixar os valores da Coluna "PIB Total" e Subcoluna "Deflator Base: 2010 = 100", para as linhas correspondentes aos anos de 2002 a 2020;
1. Calcular o índice para o deflator considerando os preços do último ano: definir último ano = 1, múltiplicar o valor de t-1 por (t-1/t);
1. Considerar os valores já baixados para a variável V0169 e multiplicá-los pelo valor do índice calculado, conforme o ano;
1. Retornar valor inteiro.

### Para a variável V0819 (Produto Interno Bruto (PIB) do Estado de São Paulo a preços correntes (R$ mil)): 
1. Baixar o arquivo "PIB - 2002 a 2020" do Repositório SEADE [PIB Anual 2002 - 2020](https://repositorio.seade.gov.br/dataset/pib-anual-2002-2020);
1. Na aba "Tabela 5", pegar os valores da Coluna "PIB Total" e Subcoluna "Preço corrente", para as linhas correspondentes aos anos de 2002 a 2020;
1. Multiplicar os valores por 1000.
1. Retornar valor inteiro.

### Para a variável V0820 (Produto Interno Bruto (PIB) do Brasil a preços correntes (R$ mil)): 
1. Baixar o arquivo "PIB - 2002 a 2020" do Repositório SEADE [PIB Anual 2002 - 2020](https://repositorio.seade.gov.br/dataset/pib-anual-2002-2020);
1. Na aba "Tabela 18", pegar os valores da Coluna "PIB Total" e Subcoluna "Preço corrente", para as linhas correspondentes aos anos de 2002 a 2020;
1. Multiplicar os valores por 1000.
1. Retornar valor inteiro.


## Tabela de mapeamento dos dados

| Campo | Descrição | Tipo do dado | Tabela de origem | Campo de origem | Regra de transformação |
| ----- | --------- | ------------ | :--------------: | :-------------: | :--------------------: |
| Variável | Preencher com os nomes resumidos das variáveis, no caso desse processo, uma linha para cada variável | String | N/A | N/A | N/A |
| Região | Preencher com a sigla da região do município de São Paulo, no caso desse processo, M00  | String | N/A | N/A | N/A |
| Ano | Preencher o cabeçalho com o valor do ano, de acordo com o arquivo de origem, por exemplo 2020. Preencher as linhas de valores de acordo com o resultado obtido na contagem das linhas dos arquivos (ver descrição do processo acima) | String | N/A | N/A | N/A |

### Regras de transformações
Não se aplica

## Dependências (pré-requisitos e premissas)
Preenchido após desenvolvimento do script de automatização.

## Considerações sobre recuperação ou reinício
Preenchido após desenvolvimento do script de automatização.

## Considerações sobre registros rejeitados na carga
Preenchido após desenvolvimento do script de automatização.
