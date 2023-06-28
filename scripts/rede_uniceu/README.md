# ObservaSampa: Automação de indicadores 
## Informações do processo
* **Processo:** Rede UniCEU
* **Versão:** 1.0
* **Objetivo:** Atualizar as variáveis do ObservaSampa referentes à Rede UniCEU.

## Fontes
O [Portal de Dados Abertos](http://dados.prefeitura.sp.gov.br/) possui o conjunto de dados [UniCEU - Polos, cursos e vagas](http://dados.prefeitura.sp.gov.br/dataset/uniceu-polos-cursos-e-vagas), o qual lista a base de dados com informações sobre a RedeUniCEU.

Os valores trazidos pela base se referem aos polos, aos cursos, às Instituições de Ensino Superior parceiras e às vagas disponibilizadas na Rede UniCEU.

Anualmente são inseridas bases como de [dezembro de 2021](http://dados.prefeitura.sp.gov.br/dataset/b0216bc7-dd2e-4e6b-b02c-a259ce2e43bb/resource/3afa3feb-aaec-4900-bdb4-bb0bd53c6864/download/uniceu2021.csv), que devem ser empregadas para a automação.

## Destinos

Este processo tem como destino a criação da planilha com informações das variáveis (V0626 e V0627) formatada no template de importação do Intranet do ObservaSampa, sendo uma tabela com as respectivas colunas: Variável, Região e Período (ver detalhes adiante na tabela de mapeamento).

## Frequência de execução

Espera-se executar esse processo anualmente.

## Descrição do processo

### Para a variável V0626 (Número de vagas na rede UNICEU para Bacharelado e Licenciatura):
1. Para cada ano, baixar o arquivo do conjunto de dados do Portal de Dados Abertos da PMSP, no formato "Polos, cursos e vagas UNICEU - Dez/{ANO}". Por exemplo, [2021](http://dados.prefeitura.sp.gov.br/dataset/b0216bc7-dd2e-4e6b-b02c-a259ce2e43bb/resource/3afa3feb-aaec-4900-bdb4-bb0bd53c6864/download/uniceu2021.csv);
2. Filtrar todos os cursos de graduação ("Graduação" ou "Bacharelado" ou "Licenciatura") na coluna "Modalidade";
3. Somar os valores das linhas na coluna "Vagas";
4. Os resultados retornados devem, necessariamente, ser inteiros.

### Para a variável V0627 (Número de vagas ofertadas para cursos de Especialização na Rede UNICEU): 
1. No mesmo arquivo referente ao ano em questão, filtrar todos os cursos de especialização (em todos os casos, "Especialização") na coluna "Modalidade";
2. Somar os valores das linhas na coluna "Vagas";
3. Os resultados retornados devem, necessariamente, ser inteiros.

## Tabela de mapeamento dos dados

| Campo | Descrição | Tipo do dado | Tabela de origem | Campo de origem | Regra de transformação |
| ----- | --------- | ------------ | :--------------: | :-------------: | :--------------------: |
| Variável | Preencher com os nomes resumidos das variáveis. No caso deste processo, um conjunto de linhas V0626 e outro para V0627 | String | N/A | N/A | N/A |
| Região | Preencher com os códigos da região referente ao município de São Paulo | String | N/A | N/A | N/A |
| Ano | Preencher o cabeçalho com o valor do ano, de acordo com o arquivo de origem, por exemplo 2021 para o arquivo de origem 2021. Preencher as linhas de valores de acordo com o resultado obtido na coleta dos valores das linhas indicadas dos arquivos (ver descrição do processo acima) | String | N/A | N/A | N/A |

### Regras de transformações
Não se aplica

## Dependências (pré-requisitos e premissas)
Preenchido após desenvolvimento do script de automatização.

## Considerações sobre recuperação ou reinício
Preenchido após desenvolvimento do script de automatização.

## Considerações sobre registros rejeitados na carga
Preenchido após desenvolvimento do script de automatização.
