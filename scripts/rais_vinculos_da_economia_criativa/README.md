# ObservaSampa: Automação de indicadores
## Informações do processo
***Processo:** Base de dados da RAIS - Vínculos da Economia Criativa
***Versão:** 1.0
***Objetivo:** Atualizar as variáveis do ObservaSampa que compõem os indicadores relacionados à base de dados da RAIS (Relação Anual das Informações Sociais) para vínculos em Economia Criativa no Município de São Paulo.

## Fontes
O [Ministério do Trabalho](http://pdet.mte.gov.br/rais) divulga os dados da RAIS em formato de Microdados [Microdados RAIS e CAGED](http://pdet.mte.gov.br/microdados-rais-e-caged) em que é possível analisar os dados de vínculos de trabalho formais no Município de São Paulo por distritos e setores de atividade econômica.

A base de dados é atualizada anualmente e é possível acessar através do link ftp://ftp.mtps.gov.br/pdet/microdados/.

Os dados são divulgados com defasagem aproximada de 1 ano. Exemplo: no final de 2022 foram divulgados os dados referentes ao ano de 2021.

## Destinos

Este processo tem como destino a criação da planilha com informações das variáveis (V0326, V0327, V0328, V0329) formatada no template de importação do Intranet do ObservaSampa. Sendo uma tabela com as respectivas colunas: Variável, Região e Período (ver detalhes adiante na tabela de mapeamento).

Regiões analisadas: Município de São Paulo, distritos e subprefeituras.

## Frequência de execução

Espera-se executar esse processo anualmente com informações do último ano disponível.

## Descrição do processo

### Para a variável V0326 (Estabelecimentos formais de Economia Criativa):
1. Para cada ano, baixar o arquivo correspondente no conjunto de dados dos [Microdados RAIS e CAGED](http://pdet.mte.gov.br/microdados-rais-e-caged). Até o ano de 2017 baixar o arquivo: ESTB{ANO}. A partir de 2018 baixar o arquivo: RAIS_ESTAB_PUB;
1. Selecionar: coluna ‘Município’=355030 e coluna ‘Ind Rais Negativa’=0, dessa forma, considera-se apenas os estabelecimentos no Município de São Paulo com empregados;
1. Acrescentar o filtro dos valores correspondentes à economia criativa conforme códigos da classe CNAE 2.0 [Códigos CNAE economia criativa](https://cloudprodamazhotmail.sharepoint.com/:x:/s/SGMCAGISEPEP/EbefD-vAnVdGmi_7CKVBPZcBrRRcfbHkWeoHi7m_tpdhzg?e=iFTZRe);
1. Contar a quantidade de linhas para o Município de São Paulo;
1. Criar coluna de correspondência para o código dos distritos: da coluna ‘Distritos SP’, equivalente à coluna ‘codigo_rais’ na planilha [RAIS_layout_distritos](https://cloudprodamazhotmail.sharepoint.com/:x:/s/SGMCAGISEPEP/Eby9h3-pRHhHmyYDnNxC8PgBuN6J0VJUpZf3OVZaSnnBuA?e=DT7zfg), pegar o código da coluna ‘codigo_distrito_observa’;
1. Contar a quantidade de linhas para cada distrito do Município de São Paulo;
1. Criar coluna para Subprefeituras, somando os valores dos distritos para cada Subprefeitura conforme planilha [Subprefeituras](https://cloudprodamazhotmail.sharepoint.com/:x:/s/SGMCAGISEPEP/ETYFVY6ef8RPma7Hnb41hS0B3_wI4OYLIE48EZfFrWqQ0w?e=3qTEli);
1. Retornar valores inteiros.

### Para a variável V0327 (Estabelecimentos formais de Gastronomia): 
1. No mesmo arquivo;
1. Repetir segundo procedimento da variável anterior;
1. Acrescentar o filtro dos valores correspondentes à economia criativa em gastronomia. Filtrar a coluna ‘CNAE 2.0 Classe’= 56112, 56121, 56201;
1. Repetir demais procedimentos da variável anterior;
1. Retornar valores inteiros.

### Para a variável V0328 (Empregos formais de Economia Criativa): 
1. Para cada ano, baixar o arquivo correspondente no conjunto de dados dos [Microdados RAIS e CAGED](http://pdet.mte.gov.br/microdados-rais-e-caged). Até o ano de 2017 baixar o arquivo: SP{ANO}. A partir de 2018 baixar o arquivo: RAIS_VINC_PUB_SP;
1. Selecionar: coluna ‘Município’=355030 e coluna 'Vínculo Ativo 31/12'= 1, dessa forma, considera-se apenas os vínculos no Município de São Paulo ativos em 31/12;
1. Acrescentar o filtro dos valores correspondentes à economia criativa conforme códigos da classe CNAE 2.0 [Códigos CNAE economia criativa](https://cloudprodamazhotmail.sharepoint.com/:x:/s/SGMCAGISEPEP/EbefD-vAnVdGmi_7CKVBPZcBrRRcfbHkWeoHi7m_tpdhzg?e=iFTZRe);
1. Contar a quantidade de linhas para o Município de São Paulo;
1. Criar coluna de correspondência para o código dos distritos: da coluna ‘Distritos SP’, equivalente à coluna ‘codigo_rais’ na planilha [RAIS_layout_distritos](https://cloudprodamazhotmail.sharepoint.com/:x:/s/SGMCAGISEPEP/Eby9h3-pRHhHmyYDnNxC8PgBuN6J0VJUpZf3OVZaSnnBuA?e=DT7zfg), pegar o código da coluna ‘codigo_distrito_observa’;
1. Contar a quantidade de linhas para cada distrito do Município de São Paulo;
1. Criar coluna para Subprefeituras, somando os valores dos distritos para cada Subprefeitura conforme planilha [Subprefeituras](https://cloudprodamazhotmail.sharepoint.com/:x:/s/SGMCAGISEPEP/ETYFVY6ef8RPma7Hnb41hS0B3_wI4OYLIE48EZfFrWqQ0w?e=3qTEli);
1. Retornar valores inteiros.

### Para a variável V0329 (Empregos formais de Gastronomia): 
1. No mesmo arquivo;
1. Repetir segundo procedimento da variável anterior;
1. Acrescentar o filtro dos valores correspondentes à economia criativa em gastronomia. Filtrar a coluna ‘CNAE 2.0 Classe’= 56112, 56121, 56201;
1. Repetir demais procedimentos da variável anterior.
1. Retornar valores inteiros.


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
