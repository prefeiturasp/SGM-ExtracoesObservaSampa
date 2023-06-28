# ObservaSampa: Automação de indicadores 
## Informações do processo
* **Processo:** Perfil dos Servidores da Educação Municipal
* **Versão:** 1.0
* **Objetivo:** Atualizar as variáveis do ObservaSampa que compõem os indicadores relacionados aos professores da Rede Municipal de Ensino.

## Fontes
O [Portal de Dados Abertos](http://dados.prefeitura.sp.gov.br/) possui o conjunto de dados [Microdados - Perfil dos Servidores da Educação](http://dados.prefeitura.sp.gov.br/dataset/microdados-servidores-perfil), o qual lista a base de dados com informações detalhadas sobre o perfil dos servidores da Educação no município.

Os valores trazidos pela base se referem à quantidade e às características dos servidores da Educação municipal.

Anualmente são inseridas bases como de [2021](http://dados.prefeitura.sp.gov.br/pt_PT/dataset/12a101f0-622b-43ad-946c-95c430ae6cab/resource/5ec984f0-6a1e-4272-b97f-2387d24ca8f1/download/perfilservidor2021.csv), que deve ser empregada para a automação.

O mês base para a coleta das informações que compõem a base referente ano é Dezembro, conforme apontado pela primeira coluna "DATA_BASE".

## Destinos

Este processo tem como destino a criação da planilha com informações das variáveis (V0064, V0065 e V0614) formatada no template de importação do Intranet do ObservaSampa. Sendo uma tabela com as respectivas colunas: Variável, Região e Período (ver detalhes adiante na tabela de mapeamento).

A presente base traz uma série de outros dados e recortes importantes, que poderiam gerar outros conteúdos para o ObservaSampa, como a raça, a idade, o sexo, a presença de deficiência e o ciclo do ensino ao qual pertencem esses servidores.

## Frequência de execução

Espera-se executar esse processo anualmente.

## Descrição do processo

### Para a variável V0064 (Professores da rede municipal com ensino superior completo):
1. Para cada ano, baixar o arquivo do conjunto de dados do Portal de Dados Abertos da PMSP, no formato "Microdados - Perfil dos Servidores {ANO}". Por exemplo, [2021](http://dados.prefeitura.sp.gov.br/pt_PT/dataset/12a101f0-622b-43ad-946c-95c430ae6cab/resource/5ec984f0-6a1e-4272-b97f-2387d24ca8f1/download/perfilservidor2021.csv);
2. Filtrar todos os cargos de professor (em todos os casos, o início do termo é "PROF.") na coluna "DC_CARGO_ATUAL";
3. Filtrar todos os cargos de nível superior na coluna "NIVEL_FORM". Para os arquivos até 2018, selecionar "SUPERIOR"; para os arquivos de 2019 em diante, selecionar "BACHARELADO", "DOUTORADO", "LICENCIATURA CURTA", "LICENCIATURA PLENA", "MESTRADO", "PÓS GRADUACAO LATO SENSU".
3. Para o total do Município, contar o número de linhas resultante das filtragens;
4. Para os resultados regionalizados, juntar o referido arquivo com o arquivo "Cadastro de escolas da cidade de São Paulo" com ano de extração correspondente da base ["Cadastro de escolas municipais, conveniadas e privadas"](http://dados.prefeitura.sp.gov.br/dataset/cadastro-de-escolas-municipais-conveniadas-e-privadas). A informação sobre o ano de extração consta na descrição, que tem o padrão "Sistema EOL - Extração em 12/{ANO};
5. Ainda para os resultados regionalizados, fazer a junção dos arquivos pela coluna "CD_UNIDADE_ATUAL" (do arquivo de microdados de servidores) com a coluna "CODESC" (do arquivo de cadastro de escolas);
6. A partir dessa junção, para os valores em nível de Distrito, filtrar o arquivo de microdados de servidores de acordo com a coluna "DISTRITO", do arquivo de cadastro de escolas;
7. Contar o número de linhas resultantes para cada um dos distritos;
8. Para os valores em nível de Subprefeitura, filtrar o arquivo de microdados de servidores de acordo com a coluna "SUBPREF", do arquivo de cadastro de escolas;
9. Contar o número de linhas resultantes para cada uma das subprefeituras;
10. Os resultados retornados devem, necessariamente, ser inteiros.

### Para a variável V0065 (Total de professores da rede municipal): 
1. No mesmo arquivo referente ao ano em questão, filtrar todos os cargos de professor (em todos os casos, o início do termo é "PROF.") na coluna "DC_CARGO_ATUAL";
2. Para o total do município, contar o número de linhas;
3. Para os resultados regionalizados, juntar o referido arquivo com o arquivo "Cadastro de escolas da cidade de São Paulo" com ano de extração correspondente da base ["Cadastro de escolas municipais, conveniadas e privadas"](http://dados.prefeitura.sp.gov.br/dataset/cadastro-de-escolas-municipais-conveniadas-e-privadas). A informação sobre o ano de extração consta na descrição, que tem o padrão "Sistema EOL - Extração em 12/{ANO};
4. Ainda para os resultados regionalizados, fazer a junção dos arquivos pela coluna "CD_UNIDADE_ATUAL" (do arquivo de microdados de servidores) com a coluna "CODESC" (do arquivo de cadastro de escolas);
5. A partir dessa junção, para os valores em nível de Distrito, filtrar o arquivo de microdados de servidores de acordo com a coluna "DISTRITO", do arquivo de cadastro de escolas;
6. Contar o número de linhas resultantes para cada um dos distritos;
7. Para os valores em Subprefeituras, filtrar o arquivo de microdados de servidores de acordo com a coluna "SUBPREF", do arquivo de cadastro de escolas;
8. Contar o número de linhas resultantes para cada uma das subprefeituras;
9. Os resultados retornados devem, necessariamente, ser inteiros.

### Para a variável V0614 (Número de professores da rede municipal com especialização): 
1. Esta variável só está presente nos arquivos a partir de 2019, não constando na base para os anos anteriores.
2. No mesmo arquivo referente ao ano em questão, filtrar todos os cargos de professor (em todos os casos, o início do termo é "PROF.") na coluna "DC_CARGO_ATUAL";
2. Filtrar "PÓS GRADUACAO LATO SENSU" na coluna "NIVEL_FORM";
3. Para o total do Município, contar o número de linhas;
4. Para os resultados regionalizados, juntar o referido arquivo com o arquivo "Cadastro de escolas da cidade de São Paulo" com ano de extração correspondente da base ["Cadastro de escolas municipais, conveniadas e privadas"](http://dados.prefeitura.sp.gov.br/dataset/cadastro-de-escolas-municipais-conveniadas-e-privadas). A informação sobre o ano de extração consta na decrição, que tem o padrão "Sistema EOL - Extração em 12/{ANO};
5. Ainda para os resultados regionalizados, fazer a junção dos arquivos pela coluna "CD_UNIDADE_ATUAL" (do arquivo de microdados de servidores) com a coluna "CODESC" (do arquivo de cadastro de escolas);
6. A partir dessa junção, para os valores em nível de Distrito, filtrar o arquivo de microdados de servidores de acordo com a coluna "DISTRITO", do arquivo de cadastro de escolas;
7. Contar o número de linhas resultantes para cada um dos distritos;
8. Para os valores em Subprefeituras, filtrar o arquivo de microdados de servidores de acordo com a coluna "SUBPREF", do arquivo de cadastro de escolas;
9. Contar o número de linhas resultantes para cada uma das subprefeituras;
10. Os resultados retornados devem, necessariamente, ser inteiros.

## Tabela de mapeamento dos dados

| Campo | Descrição | Tipo do dado | Tabela de origem | Campo de origem | Regra de transformação |
| ----- | --------- | ------------ | :--------------: | :-------------: | :--------------------: |
| Variável | Preencher com os nomes resumidos das variáveis. No caso deste processo, um conjunto de linhas para V0064, um para V0065 e outro para V0614 | String | N/A | N/A | N/A |
| Região | Preencher com os códigos da região referentes aos distritos, às subprefeituras e ao município de São Paulo | String | N/A | N/A | N/A |
| Ano | Preencher o cabeçalho com o valor do ano, de acordo com o arquivo de origem, por exemplo 2021 para o arquivo de origem 2021. Preencher as linhas de valores de acordo com o resultado da contagem de linhas dos arquivos (ver descrição do processo acima) | String | N/A | N/A | N/A |

### Regras de transformações
Não se aplica

## Dependências (pré-requisitos e premissas)
Preenchido após desenvolvimento do script de automatização.

## Considerações sobre recuperação ou reinício
Preenchido após desenvolvimento do script de automatização.

## Considerações sobre registros rejeitados na carga
Preenchido após desenvolvimento do script de automatização.

