# ObservaSampa: Automação de indicadores 
## Informações do processo
* **Processo:** Perfil das Turmas e EMEFs
* **Versão:** 1.0
* **Objetivo:** Atualizar as variáveis do ObservaSampa que compõem os indicadores sobre as turmas da Rede Municipal de Ensino, sobre o uso de Transporte Escolar Gratuito e sobre as EMEFs.

## Fontes
O [Portal de Dados Abertos](http://dados.prefeitura.sp.gov.br/) possui o conjunto de dados [Perfil das turmas e unidades educacionais em funcionamento](http://dados.prefeitura.sp.gov.br/dataset/perfil-das-turmas-e-unidades-educacionais-em-funcionamento), o qual lista a base de dados com informações sobre número de matrículas, turmas, turnos de funcionamento, portadores de necessidades especiais, transporte escolar gratuito, entre outros.

Os valores trazidos pela base se referem à quantidade e às características das turmas da Rede Municipal.

Semestralmente (em junho e dezembro) são inseridas bases como de [dezembro de 2022](http://dados.prefeitura.sp.gov.br/dataset/afa17bfd-3286-4c40-87c9-52933066a592/resource/6f6d2924-8bc7-4625-ae13-069418d666be/download/turmas122022.csv), que deve ser empregada para a automação.

Os arquivos de referência para a obtenção de valores para o ObservaSampa são sempre os de dezembro, com a consolidação dos valores do encerramento do ano letivo. 

## Destinos

Este processo tem como destino a criação da planilha com informações das variáveis (V0014, V0022, V0024, V0026, V0044, V0063 V0399, V0400, V0609 e V0610) formatada no template de importação do Intranet do ObservaSampa, sendo uma tabela com as respectivas colunas: Variável, Região e Período (ver detalhes adiante na tabela de mapeamento).

## Frequência de execução

Espera-se executar esse processo anualmente.

## Descrição do processo

### Para a variável V0014 (Turmas Ensino Fundamental da rede municipal):
1. Para cada ano, baixar o arquivo do conjunto de dados do Portal de Dados Abertos da PMSP, no formato "Perfil de turmas e turnos", com o ano de extração constando na definição, seguindo o formato "Extraído do Sistema EOL em Dez/{ANO}". Por exemplo, [2022](http://dados.prefeitura.sp.gov.br/dataset/afa17bfd-3286-4c40-87c9-52933066a592/resource/6f6d2924-8bc7-4625-ae13-069418d666be/download/turmas122022.csv);
2. Filtar as turmas de Ensino Fundamental ("FUND") na coluna "MODAL";
3. Para o total do Município, contar o número de linhas;
4. Para os resultados em nível de Distrito, filtrar pelo nome de cada um dos distritos na coluna "DISTRITO", e contar o número de linhas;
5. Para os resultados em nível de Subprefeitura, filtrar pelo nome de cada uma das subprefeituras na coluna "SUBPREF", e contar o número de linhas;
6. Os resultados retornados devem, necessariamente, ser inteiros.

### Para a variável V0022 (Turmas em creches da rede municipal e conveniada):
1. No mesmo arquivo referente ao ano em questão, filtrar as turmas de creches ("CRECHE") na coluna "MODAL";
2. Para o total do Município, contar o número de linhas;
3. Para os resultados em nível de Distrito, filtrar pelo nome de cada um dos distritos na coluna "DISTRITO", e contar o número de linhas;
4. Para os resultados em nível de Subprefeitura, filtrar pelo nome de cada uma das subprefeituras na coluna "SUBPREF", e contar o número de linhas;
5. Os resultados retornados devem, necessariamente, ser inteiros.

### Para a variável V0024 (Turmas de pré-escola da rede municipal e conveniada):
1. No mesmo arquivo referente ao ano em questão, filtrar as turmas de pré-escola ("PRE") na coluna "MODAL";
2. Para o total do Município, contar o número de linhas;
3. Para os resultados em nível de Distrito, filtrar pelo nome de cada um dos distritos na coluna "DISTRITO", e contar o número de linhas;
4. Para os resultados em nível de Subprefeitura, filtrar pelo nome de cada uma das subprefeituras na coluna "SUBPREF", e contar o número de linhas;
5. Os resultados retornados devem, necessariamente, ser inteiros.

### Para a variável V0026 (Turmas Ensino Médio da rede municipal):
1. No mesmo arquivo referente ao ano em questão, filtrar as turmas de Ensino Médio ("MEDIO") na coluna "MODAL";
2. Para o total do Município, contar o número de linhas;
3. Para os resultados em nível de Distrito, filtrar pelo nome de cada um dos distritos na coluna "DISTRITO", e contar o número de linhas;
4. Para os resultados em nível de Subprefeitura, filtrar pelo nome de cada uma das subprefeituras na coluna "SUBPREF", e contar o número de linhas;
5. Os resultados retornados devem, necessariamente, ser inteiros.

### Para a variável V0044 (Alunos do Ensino Fundamental que utilizam Transporte Escolar Gratuito):
1. No mesmo arquivo referente ao ano em questão, filtrar as turmas de Ensino Fundamental ("FUND") na coluna "MODAL";
2. Para o total do Município, somar os valores na coluna "ALU_TEG";
3. Para os resultados em nível de Distrito, filtrar pelo nome de cada um dos distritos na coluna "DISTRITO", e então somar os valores na coluna "ALU_TEG";
4. Para os resultados em nível de Subprefeitura, filtrar pelo nome de cada uma das subprefeituras na coluna "SUBPREF", e então somar os valores na coluna "ALU_TEG";
5. Os resultados retornados devem, necessariamente, ser inteiros.

### Para a variável V0063 (Matrículas - tempo integral educação infantil municipal): 
1. No mesmo arquivo referente ao ano em questão, filtrar as turmas educação infantil (usando os códigos "CRECHE" e "PRE") na coluna "MODAL";
2. Filtrar as turmas de tempo integral (todos os resultados iguais a "6") na coluna "TURNO";
3. Para o resultado do Município, somar todos os valores da coluna "MATRIC";
4. Para os resultados em nível de Distrito, filtrar pelo nome de cada um dos distritos na coluna "DISTRITO", e somar todos os valores da coluna "MATRIC";
5. Para os resultados em nível de Subprefeitura, filtrar pelo nome de cada uma das subprefeituras na coluna "SUBPREF", e somar todos os valores da coluna "MATRIC";
6. Os resultados retornados devem, necessariamente, ser inteiros.

### Para a variável V0399 (EMEFs que oferecem turmas em educação integral em tempo integral):
1. No mesmo arquivo referente ao ano em questão, filtrar as EMEFs (em todos os casos, "EMEF") na coluna "TIPOESC";
2. Filtrar as turmas de tempo integral (todos os resultados iguais a "6") na coluna "TURNO";
3. Para o valor do Município, contar o número de valores diferentes para a coluna "CODESC";
4. Para os resultados em nível de Distrito, filtrar pelo nome de cada um dos distritos na coluna "DISTRITO", e contar o número de valores diferentes resultantes na coluna "CODESC";
5. Para os resultados em nível de Subprefeitura, filtrar pelo nome de cada uma das subprefeituras na coluna "SUBPREF", e contar o número de valores diferentes resultantes na coluna "CODESC";
6. Os resultados retornados devem, necessariamente, ser inteiros.

### Para a variável V0400 (Total de EMEFs): 
1. No mesmo arquivo referente ao ano em questão, filtrar as EMEFs (em todos os casos, "EMEF") na coluna "TIPOESC";
2. Para o total do município, contar o número de valores diferentes para a coluna "CODESC";
3. Para os resultados em nível de Distrito, filtrar pelo nome de cada um dos distritos na coluna "DISTRITO", e contar o número de valores diferentes resultantes na coluna "CODESC";
4. Para os resultados em nível de Subprefeitura, filtrar pelo nome de cada uma das subprefeituras na coluna "SUBPREF", e contar o número de valores diferentes resultantes na coluna "CODESC";
5. Os resultados retornados devem, necessariamente, ser inteiros.

### Para a variável V0609 (Número de alunos matriculados em tempo integral no Ensino Fundamental - anos iniciais): 
1. No mesmo arquivo referente ao ano em questão, filtrar as turmas de anos iniciais (1º ao 5º) do Ensino Fundamental de acordo com o código dos anos ("110"; "111"; "112"; "116"; e "117" na coluna "CODSERIE")
2. Filtrar as turmas de tempo integral (todos os resultados iguais a "6") na coluna "TURNO";
3. Para o resultado do Município, somar todos os valores da coluna "MATRIC";
4. Para os resultados em nível de Distrito, filtrar pelo nome de cada um dos distritos na coluna "DISTRITO", e somar todos os valores da coluna "MATRIC";
5. Para os resultados em nível de Subprefeitura, filtrar pelo nome de cada uma das subprefeituras na coluna "SUBPREF", e somar todos os valores da coluna "MATRIC";
6. Os resultados retornados devem, necessariamente, ser inteiros.

### Para a variável V0610 (Número de alunos matriculados em tempo integral no Ensino Fundamental - anos finais): 
1. No mesmo arquivo referente ao ano em questão, filtrar as turmas de anos finais (6º ao 9º) do Ensino Fundamental de acordo com o código dos anos ("115"; "118"; "119"; e "120" na coluna "CODSERIE")
2. Filtrar as turmas de tempo integral (todos os resultados iguais a "6") na coluna "TURNO";
3. Para o resultado do Município, somar todos os valores da coluna "MATRIC";
4. Para os resultados em nível de Distrito, filtrar pelo nome de cada um dos distritos na coluna "DISTRITO", e somar todos os valores da coluna "MATRIC";
5. Para os resultados em nível de Subprefeitura, filtrar pelo nome de cada uma das subprefeituras na coluna "SUBPREF", e somar todos os valores da coluna "MATRIC";
6. Os resultados retornados devem, necessariamente, ser inteiros.

## Tabela de mapeamento dos dados

| Campo | Descrição | Tipo do dado | Tabela de origem | Campo de origem | Regra de transformação |
| ----- | --------- | ------------ | :--------------: | :-------------: | :--------------------: |
| Variável | Preencher com os nomes resumidos das variáveis. No caso deste processo, um conjunto de linhas para V0014, um para V0022, um para V0024, um para V0026, um para V0063, um para V0399, um para V0400, um para V0609 e outro para V0610 | String | N/A | N/A | N/A |
| Região | Preencher com os códigos da região referentes aos distritos, às subprefeituras e ao município de São Paulo | String | N/A | N/A | N/A |
| Ano | Preencher o cabeçalho com o valor do ano, de acordo com o arquivo de origem, por exemplo 2021 para o arquivo de origem 2021. Preencher as linhas de valores de acordo com o resultado obtido na coleta dos valores das linhas indicadas dos arquivos (ver descrição do processo acima) | String | N/A | N/A | N/A |

### Regras de transformações
Não se aplica

## Dependências (pré-requisitos e premissas)
Preenchido após desenvolvimento do script de automatização.

## Considerações sobre recuperação ou reinício
Preenchido após desenvolvimento do script de automatização.

## Considerações sobre registros rejeitados na carga
Preenchido após desenvolvimento do script de automatização.
