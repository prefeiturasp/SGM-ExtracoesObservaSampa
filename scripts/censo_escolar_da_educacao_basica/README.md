# ObservaSampa: Automação de indicadores 
## Informações do processo
* **Processo:** Microdados do Censo Escolar da Educação Básica
* **Versão:** 1.0
* **Objetivo:** Atualizar as variáveis do ObservaSampa que compõem os indicadores sobre as escolas, as matrículas e os serviços das escolas (de todas as redes) no município de São Paulo.

## Fontes
O site do [Instituto Nacional de Estudos e Pesquisas Educacionais Anísio Teixeira - INEP](https://www.gov.br/inep/pt-br) possui os conjuntos de dados [Microdados do Censo Escolar da Educação Básica](https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/microdados/censo-escolar) o qual lista a base de dados com informações sobre as instituições de ensino da Educação Básica em todo o país.

Anualmente, são inseridas bases como de [2022](https://download.inep.gov.br/dados_abertos/microdados_censo_escolar_2022.zip), em formato .zip, e, quando extraídas, resultam em arquivos variados, incluindo as bases, em formato .xlsx, que devem ser utilizadas para a automação.

## Destinos

Este processo tem como destino a criação da planilha com informações das variáveis (V0007, V0012, V0029, V0031, V0060, V0128, V0611, e V0612) formatada no template de importação do Intranet do ObservaSampa, sendo uma tabela com as respectivas colunas: Variável, Região e Período (ver detalhes adiante na tabela de mapeamento).

## Frequência de execução

Espera-se executar esse processo anualmente com informações de cada ano.

## Descrição do processo

### Para a variável V0007 (Matrículas - creches todas as redes):
1. Para cada ano, baixar o arquivo de microdados do Censo Escolar referente àquele ano, no formato "Microdados do Censo Escolar da Educação Básica {Ano}";
2. Extrair o arquivo baixado;
3. Na pasta da extração, seguir o caminho pasta "Microdados do Censo Escolar da Educação Básica {ANO}" > pasta "dados" > arquivo "microdados_ed_basica_{ANO}";
4. No arquivo referente aos resultados para o ano, filtrar o município de São Paulo, utilizando o código "3550308" na coluna "CO_MUNICIPIO";
5. Para o total do Município, somar todos os valores da coluna "QT_MAT_INF_CRE";
6. Para os resultados em nível de Distrito, filtrar o distrito de acordo com seu código na coluna "CO_DISTRITO" (no formato "3550308{nº do distrito}), e então somar os valores da coluna "QT_MAT_INF_CRE";
7. Para os resultados em nível de Subprefeitura, somar os valores dos distritos que compõem cada subprefeitura;
8. Os resultados retornados devem, necessariamente, ser inteiros.

### Para a variável V0012 (Matrículas - ensino básico redes pública e privada):
1. No mesmo arquivo referente ao ano, filtrar o município de São Paulo, utilizando o código "3550308" na coluna "CO_MUNICIPIO";
2. Para o total do Município, somar todos os valores da coluna "QT_MAT_BAS";
3. Para os resultados em nível de Distrito, filtrar o distrito de acordo com seu código na coluna "CO_DISTRITO" (no formato "3550308{nº do distrito}), e então somar os valores da coluna "QT_MAT_BAS";
4. Para os resultados em nível de Subprefeitura, somar os valores dos distritos que compõem cada subprefeitura;
5. Os resultados retornados devem, necessariamente, ser inteiros.

### Para a variável V0029 (Matrículas - fundamental todas as redes):
1. No mesmo arquivo referente ao ano, filtrar o município de São Paulo, utilizando o código "3550308" na coluna "CO_MUNICIPIO";
2. Para o total do Município, somar todos os valores da coluna "QT_MAT_FUND";
3. Para os resultados em nível de Distrito, filtrar o distrito de acordo com seu código na coluna "CO_DISTRITO" (no formato "3550308{nº do distrito}), e então somar os valores da coluna "QT_MAT_FUND";
4. Para os resultados em nível de Subprefeitura, somar os valores dos distritos que compõem cada subprefeitura;
5. Os resultados retornados devem, necessariamente, ser inteiros.

### Para a variável V0031 (Matrículas - pré-escola todas as redes):
1. No mesmo arquivo referente ao ano, filtrar o município de São Paulo, utilizando o código "3550308" na coluna "CO_MUNICIPIO";
2. Para o total do Município, somar todos os valores da coluna "QT_MAT_INF_PRE";
3. Para os resultados em nível de Distrito, filtrar o distrito de acordo com seu código na coluna "CO_DISTRITO" (no formato "3550308{nº do distrito}), e então somar os valores da coluna "QT_MAT_INF_PRE";
4. Para os resultados em nível de Subprefeitura, somar os valores dos distritos que compõem cada subprefeitura;
5. Os resultados retornados devem, necessariamente, ser inteiros.

### Para a variável V0060 (Matrículas de crianças na Creche da rede pública):
1. No mesmo arquivo referente ao ano, filtrar o município de São Paulo, utilizando o código "3550308" na coluna "CO_MUNICIPIO";
2. Filtrar os estabelecimentos da rede pública, selecionando as escolas da rede federal (código "1" na coluna "TP_DEPENDENCIA"), da rede estadual (código "2" na coluna "TP_DEPENDENCIA") e da rede municipal (código "3" na coluna "TP_DEPENDENCIA");
3. Para o total do Município, somar todos os valores da coluna "QT_MAT_INF_CRE";
4. Para os resultados em nível de Distrito, filtrar o distrito de acordo com seu código na coluna "CO_DISTRITO" (no formato "3550308{nº do distrito}), e então somar os valores da coluna "QT_MAT_BAS";
5. Para os resultados em nível de Subprefeitura, somar os valores dos distritos que compõem cada subprefeitura;
6. Os resultados retornados devem, necessariamente, ser inteiros.

### Para a variável V0128 (Matrículas - ensino médio todas as redes):
1. No mesmo arquivo referente ao ano, filtrar o município de São Paulo, utilizando o código "3550308" na coluna "CO_MUNICIPIO";
2. Para o total do Município, somar todos os valores da coluna "QT_MAT_MED";
3. Para os resultados em nível de Distrito, filtrar o distrito de acordo com seu código na coluna "CO_DISTRITO" (no formato "3550308{nº do distrito}), e então somar os valores da coluna "QT_MAT_MED";
4. Para os resultados em nível de Subprefeitura, somar os valores dos distritos que compõem cada subprefeitura;
5. Os resultados retornados devem, necessariamente, ser inteiros.

### Para a variável V0611 (Número de escolas públicas):
1. No mesmo arquivo referente ao ano, filtrar o município de São Paulo, utilizando o código "3550308" na coluna "CO_MUNICIPIO";
2. Filtrar os estabelecimentos da rede pública, selecionando as escolas da rede federal (código "1" na coluna "TP_DEPENDENCIA"), da rede estadual (código "2" na coluna "TP_DEPENDENCIA") e da rede municipal (código "3" na coluna "TP_DEPENDENCIA");
3. Para o total do Município, contar o número de linhas;
4. Para os resultados em nível de Distrito, filtrar o distrito de acordo com seu código na coluna "CO_DISTRITO" (no formato "3550308{nº do distrito}), e então contar o número de linhas;
5. Para os resultados em nível de Subprefeitura, somar os valores dos distritos que compõem cada subprefeitura;
6. Os resultados retornados devem, necessariamente, ser inteiros.

### Para a variável V0612 (Escolas públicas com atendimento educacional especializado):
1. No mesmo arquivo referente ao ano, filtrar o município de São Paulo, utilizando o código "3550308" na coluna "CO_MUNICIPIO";
2. Filtrar os estabelecimentos da rede pública, selecionando as escolas da rede federal (código "1" na coluna "TP_DEPENDENCIA"), da rede estadual (código "2" na coluna "TP_DEPENDENCIA") e da rede municipal (código "3" na coluna "TP_DEPENDENCIA");
3. Filtrar os estabelecimentos da rede pública que oferecem Atendimento Educacional Especializado, filtrando os códigos "1" e "2" ("Não exclusivamente" e "Exclusivamente", respectivamente) na coluna "TP_AEE";
4. Para o total do Município, contar o número de linhas;
5. Para os resultados em nível de Distrito, filtrar o distrito de acordo com seu código na coluna "CO_DISTRITO" (no formato "3550308{nº do distrito}), e então contar o número de linhas;
6. Para os resultados em nível de Subprefeitura, somar os valores dos distritos que compõem cada subprefeitura;
7. Os resultados retornados devem, necessariamente, ser inteiros.

## Tabela de mapeamento dos dados

| Campo | Descrição | Tipo do dado | Tabela de origem | Campo de origem | Regra de transformação |
| ----- | --------- | ------------ | :--------------: | :-------------: | :--------------------: |
| Variável | Preencher com os nomes resumidos das variáveis. No caso deste processo, um conjunto de linhas para V0007, um para V0012, um para V0029, um para V0031, um para V0060, um para V0128, um para V0611 e outro para V0612 | String | N/A | N/A | N/A |
| Região | Preencher com os códigos da região referentes aos distritos, às subprefeituras e ao município de São Paulo | String | N/A | N/A | N/A |
| Ano | Preencher o cabeçalho com o valor do ano, de acordo com o arquivo de origem, por exemplo 2022 para o arquivo de 2022. Preencher as linhas de valores de acordo com o resultado obtido na coleta dos valores das linhas indicadas dos arquivos (ver descrição do processo acima) | String | N/A | N/A | N/A |

### Regras de transformações
Não se aplica

## Dependências (pré-requisitos e premissas)
Preenchido após desenvolvimento do script de automatização.

## Considerações sobre recuperação ou reinício
Preenchido após desenvolvimento do script de automatização.

## Considerações sobre registros rejeitados na carga
Preenchido após desenvolvimento do script de automatização.
