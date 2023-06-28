# ObservaSampa: Automação de indicadores
## Informações do processo
* **Processo:** Base de dados de Exportação e Importação
* **Versão:** 1.0
* **Objetivo:** Atualizar as variáveis do ObservaSampa que compõem os indicadores relacionados à base de dados de Exportação e Importação.

## Fontes
O [Repositório SEADE](https://repositorio.seade.gov.br/) possui o conjunto de dados [Comércio exterior - Painel](https://repositorio.seade.gov.br/dataset/comercio-exterior) o qual apresenta valores (em US$ FOB) e produtos de exportações e importações, no estado de São Paulo.

Devem ser utilizadas as bases [Valor das exportações por municípios do ESP](https://repositorio.seade.gov.br/dataset/comercio-exterior/resource/5a75827c-7797-4229-9867-500432ded8d1) e [Valor das importações por municípios do ESP](https://repositorio.seade.gov.br/dataset/comercio-exterior/resource/d562a340-64cd-4835-a079-7001438acf63).


## Destinos

Este processo tem como destino a criação da planilha com informações das variáveis (V0817 e V0818) formatada no template de importação do Intranet do ObservaSampa. Sendo uma tabela com as respectivas colunas: Variável, Região e Período (ver detalhes adiante na tabela de mapeamento).

Região analisada: Município de São Paulo.

## Frequência de execução

Espera-se executar esse processo anualmente com informações do último ano disponível.

## Descrição do processo

### Para a variável V0817 (Exportações totais (valor FOB, US$):
1. Baixar o arquivo correspondente no conjunto de dados de Exportação do Repositório SEADE [Valor das exportações por municípios do ESP](https://repositorio.seade.gov.br/dataset/comercio-exterior/resource/5a75827c-7797-4229-9867-500432ded8d1);
1. Para cada ano, na coluna "CO_ANO", somar os valores da coluna "VL_FOB_EXP", correspondentes ao Município de São Paulo, código 3550308 na coluna "CO_MUN";
1. Retornar valor inteiro.

### Para a variável V0818 (Importações totais  (valor FOB, US$)): 
1. Baixar o arquivo correspondente no conjunto de dados de Importação do Repositório SEADE [Valor das importações por municípios do ESP](https://repositorio.seade.gov.br/dataset/comercio-exterior/resource/d562a340-64cd-4835-a079-7001438acf63);
1. Para cada ano, na coluna "CO_ANO", somar os valores da coluna "VL_FOB", correspondentes ao Município de São Paulo, código 3550308 na coluna "CO_MUN";
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
