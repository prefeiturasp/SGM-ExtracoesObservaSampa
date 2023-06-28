# ObservaSampa: Automação de indicadores
## Informações do processo
* **Processo:** Base de dados de Execução Orçamentária
* **Versão:** 1.0
* **Objetivo:** Atualizar as variáveis do ObservaSampa que compõem os indicadores relacionados à base de dados de Execução Orçamentária.

## Fontes
O [Portal de Dados Abertos](http://dados.prefeitura.sp.gov.br/) possui o conjunto de dados [Execução Orçamentária](http://dados.prefeitura.sp.gov.br/dataset/base-dados-execucao) o qual contém dados do valor liquidado no orçamento da Prefeitura Municipal de São Paulo por função.

Devem ser utilizadas as bases anuais [Base de dados da Execução Orçamentária](http://dados.prefeitura.sp.gov.br/dataset/base-dados-execucao/resource/86b6276e-2841-45f9-ba59-3616be207917).


## Destinos

Este processo tem como destino a criação da planilha com informações das variáveis (V0129, V0130, V0131, V0132, V0133, V0134, V0135, V0136, V0137, V0138, V0139, V0140, V0141, V0142, V0143, V0145, V0146, V0147, V0148, V0150, V0151, V0152, V0153, V0154, V0155 e V0162) formatada no template de importação do Intranet do ObservaSampa. Sendo uma tabela com as respectivas colunas: Variável, Região e Período (ver detalhes adiante na tabela de mapeamento).

Região analisada: Município de São Paulo.

## Frequência de execução

Espera-se executar esse processo anualmente com informações do último ano disponível.

## Descrição do processo

### Para a variável V0129 (Orçamento liquidado da Prefeitura Municipal de São Paulo):
1. Para cada ano, baixar o arquivo no seguinte formato: "Base de dados da Execução Orçamentária - {ANO}" [Execução Orçamentária](http://dados.prefeitura.sp.gov.br/dataset/base-dados-execucao) (Obs.: Baixar somente o arquivo do último ano disponível, caso o objetivo seja apenas a atualização do último ano e não baixar a série inteira);
1. Somar os valores da coluna "Vl_Liquidado", desconsiderando o código "91" da coluna "Cd_Modalidade" que se refere a despesas intraorçamentárias.
1. Retornar valor com duas casas decimais.

### Para a variável V0130 (Valor liquidado no orçamento da Prefeitura Municipal de São Paulo com a função orçamentária Administração):
1. No mesmo arquivo;
1. Somar os valores da coluna "Vl_Liquidado", filtrando "Administração" da coluna "Ds_Funcao" e desconsiderando o código "91" da coluna "Cd_Modalidade";
1. Retornar valor com duas casas decimais.

### Para a variável V0131 (Valor liquidado no orçamento da Prefeitura Municipal de São Paulo com a função orçamentária Agricultura): 
1. No mesmo arquivo;
1. Somar os valores da coluna "Vl_Liquidado", filtrando "Agricultura" da coluna "Ds_Funcao" e desconsiderando o código "91" da coluna "Cd_Modalidade";
1. Retornar valor com duas casas decimais.

### Para a variável V0132 (Valor liquidado no orçamento da Prefeitura Municipal de São Paulo com a função orçamentária Assistência Social): 
1. No mesmo arquivo;
1. Somar os valores da coluna "Vl_Liquidado", filtrando "Assistência Social" da coluna "Ds_Funcao" e desconsiderando o código "91" da coluna "Cd_Modalidade";
1. Retornar valor com duas casas decimais.

### Para a variável V0133 (Valor liquidado no orçamento da Prefeitura Municipal de São Paulo com a função orçamentária Comércio e Serviços): 
1. No mesmo arquivo;
1. Somar os valores da coluna "Vl_Liquidado", filtrando "Comércio e Serviços" da coluna "Ds_Funcao" e desconsiderando o código "91" da coluna "Cd_Modalidade";
1. Retornar valor com duas casas decimais.

### Para a variável V0134 (Valor liquidado no orçamento da Prefeitura Municipal de São Paulo com a função orçamentária Comunicações): 
1. No mesmo arquivo;
1. Somar os valores da coluna "Vl_Liquidado", filtrando "Comunicações" da coluna "Ds_Funcao" e desconsiderando o código "91" da coluna "Cd_Modalidade";
1. Retornar valor com duas casas decimais.

### Para a variável V0135 (Valor liquidado no orçamento da Prefeitura Municipal de São Paulo com a função orçamentária Cultura): 
1. No mesmo arquivo;
1. Somar os valores da coluna "Vl_Liquidado", filtrando "Cultura" da coluna "Ds_Funcao" e desconsiderando o código "91" da coluna "Cd_Modalidade";
1. Retornar valor com duas casas decimais.

### Para a variável V0136 (Valor liquidado no orçamento da Prefeitura Municipal de São Paulo com a função orçamentária Defesa Nacional): 
1. No mesmo arquivo;
1. Somar os valores da coluna "Vl_Liquidado", filtrando "Defesa Nacional" da coluna "Ds_Funcao" e desconsiderando o código "91" da coluna "Cd_Modalidade";
1. Retornar valor com duas casas decimais.

### Para a variável V0137 (Valor liquidado no orçamento da Prefeitura Municipal de São Paulo com a função orçamentária Desporto e Lazer): 
1. No mesmo arquivo;
1. Somar os valores da coluna "Vl_Liquidado", filtrando "Desporto e Lazer" da coluna "Ds_Funcao" e desconsiderando o código "91" da coluna "Cd_Modalidade";
1. Retornar valor com duas casas decimais.

### Para a variável V0138 (Valor liquidado no orçamento da Prefeitura Municipal de São Paulo com a função orçamentária Direitos da Cidadania): 
1. No mesmo arquivo;
1. Somar os valores da coluna "Vl_Liquidado", filtrando "Direitos da Cidadania" da coluna "Ds_Funcao" e desconsiderando o código "91" da coluna "Cd_Modalidade";
1. Retornar valor com duas casas decimais.

### Para a variável V0139 (Valor liquidado no orçamento da Prefeitura Municipal de São Paulo com a função orçamentária Educação): 
1. No mesmo arquivo;
1. Somar os valores da coluna "Vl_Liquidado", filtrando "Educação" da coluna "Ds_Funcao" e desconsiderando o código "91" da coluna "Cd_Modalidade";
1. Retornar valor com duas casas decimais.

### Para a variável V0140 (Valor liquidado no orçamento da Prefeitura Municipal de São Paulo com a função orçamentária Encargos Especiais): 
1. No mesmo arquivo;
1. Somar os valores da coluna "Vl_Liquidado", filtrando "Encargos Especiais" da coluna "Ds_Funcao" e desconsiderando o código "91" da coluna "Cd_Modalidade";
1. Retornar valor com duas casas decimais.

### Para a variável V0141 (Valor liquidado no orçamento da Prefeitura Municipal de São Paulo com a função orçamentária Energia): 
1. No mesmo arquivo;
1. Somar os valores da coluna "Vl_Liquidado", filtrando "Energia" da coluna "Ds_Funcao" e desconsiderando o código "91" da coluna "Cd_Modalidade";
1. Retornar valor com duas casas decimais.

### Para a variável V0142 (Valor liquidado no orçamento da Prefeitura Municipal de São Paulo com a função orçamentária Gestão Ambiental): 
1. No mesmo arquivo;
1. Somar os valores da coluna "Vl_Liquidado", filtrando "Gestão Ambiental" da coluna "Ds_Funcao" e desconsiderando o código "91" da coluna "Cd_Modalidade";
1. Retornar valor com duas casas decimais.

### Para a variável V0143 (Valor liquidado no orçamento da Prefeitura Municipal de São Paulo com a função orçamentária Habitação): 
1. No mesmo arquivo;
1. Somar os valores da coluna "Vl_Liquidado", filtrando "Habitação" da coluna "Ds_Funcao" e desconsiderando o código "91" da coluna "Cd_Modalidade";
1. Retornar valor com duas casas decimais.

### Para a variável V0145 (Valor liquidado no orçamento da Prefeitura Municipal de São Paulo com a função orçamentária Judiciária): 
1. No mesmo arquivo;
1. Somar os valores da coluna "Vl_Liquidado", filtrando "Judiciária" da coluna "Ds_Funcao" e desconsiderando o código "91" da coluna "Cd_Modalidade";
1. Retornar valor com duas casas decimais.

### Para a variável V0146 (Valor liquidado no orçamento da Prefeitura Municipal de São Paulo com a função orçamentária Legislativa): 
1. No mesmo arquivo;
1. Somar os valores da coluna "Vl_Liquidado", filtrando "Legislativa" da coluna "Ds_Funcao" e desconsiderando o código "91" da coluna "Cd_Modalidade";
1. Retornar valor com duas casas decimais.

### Para a variável V0147 (Valor liquidado no orçamento da Prefeitura Municipal de São Paulo com a função orçamentária Previdência Social): 
1. No mesmo arquivo;
1. Somar os valores da coluna "Vl_Liquidado", filtrando "Previdência Social" da coluna "Ds_Funcao" e desconsiderando o código "91" da coluna "Cd_Modalidade";
1. Retornar valor com duas casas decimais.

### Para a variável V0148 (Valor liquidado no orçamento da Prefeitura Municipal de São Paulo com a função orçamentária Relações Exteriores): 
1. No mesmo arquivo;
1. Somar os valores da coluna "Vl_Liquidado", filtrando "Relações Exteriores" da coluna "Ds_Funcao" e desconsiderando o código "91" da coluna "Cd_Modalidade";
1. Retornar valor com duas casas decimais.

### Para a variável V0150 (Valor liquidado no orçamento da Prefeitura Municipal de São Paulo com a função orçamentária Saneamento): 
1. No mesmo arquivo;
1. Somar os valores da coluna "Vl_Liquidado", filtrando "Saneamento" da coluna "Ds_Funcao" e desconsiderando o código "91" da coluna "Cd_Modalidade";
1. Retornar valor com duas casas decimais.

### Para a variável V0151 (Valor liquidado no orçamento da Prefeitura Municipal de São Paulo com a função orçamentária Saúde): 
1. No mesmo arquivo;
1. Somar os valores da coluna "Vl_Liquidado", filtrando "Saúde" da coluna "Ds_Funcao" e desconsiderando o código "91" da coluna "Cd_Modalidade";
1. Retornar valor com duas casas decimais.

### Para a variável V0152 (Valor liquidado no orçamento da Prefeitura Municipal de São Paulo com a função orçamentária Segurança Pública): 
1. No mesmo arquivo;
1. Somar os valores da coluna "Vl_Liquidado", filtrando "Segurança Pública" da coluna "Ds_Funcao" e desconsiderando o código "91" da coluna "Cd_Modalidade";
1. Retornar valor com duas casas decimais.

### Para a variável V0153 (Valor liquidado no orçamento da Prefeitura Municipal de São Paulo com a função orçamentária Trabalho): 
1. No mesmo arquivo;
1. Somar os valores da coluna "Vl_Liquidado", filtrando "Trabalho" da coluna "Ds_Funcao" e desconsiderando o código "91" da coluna "Cd_Modalidade";
1. Retornar valor com duas casas decimais.

### Para a variável V0154 (Valor liquidado no orçamento da Prefeitura Municipal de São Paulo com a função orçamentária Transporte): 
1. No mesmo arquivo;
1. Somar os valores da coluna "Vl_Liquidado", filtrando "Transporte" da coluna "Ds_Funcao" e desconsiderando o código "91" da coluna "Cd_Modalidade";
1. Retornar valor com duas casas decimais.

### Para a variável V0155 (Valor liquidado no orçamento da Prefeitura Municipal de São Paulo com a função orçamentária Urbanismo): 
1. No mesmo arquivo;
1. Somar os valores da coluna "Vl_Liquidado", filtrando "Urbanismo" da coluna "Ds_Funcao" e desconsiderando o código "91" da coluna "Cd_Modalidade";
1. Retornar valor com duas casas decimais.

### Para a variável V0162 (Investimento realizado pela Prefeitura - Valor Empenhado (R$)): 
1. No mesmo arquivo;
1. Somar os valores da coluna "Vl_EmpenhadoLiquido", filtrando "4" da coluna "Grupo_Despesa";
1. Retornar valor com duas casas decimais.


## Tabela de mapeamento dos dados

| Campo | Descrição | Tipo do dado | Tabela de origem | Campo de origem | Regra de transformação |
| ----- | --------- | ------------ | :--------------: | :-------------: | :--------------------: |
| Variável | Preencher com os nomes resumidos das variáveis, no caso desse processo, uma linha para cada variável | String | N/A | N/A | N/A |
| Região | Preencher com a sigla da região do município de São Paulo, no caso desse processo, M00 | String | N/A | N/A | N/A |
| Ano | Preencher o cabeçalho com o valor do ano, de acordo com o arquivo de origem, por exemplo 2022. Preencher as linhas de valores de acordo com o resultado obtido na contagem das linhas dos arquivos (ver descrição do processo acima) | String | N/A | N/A | N/A |

### Regras de transformações
Não se aplica

## Dependências (pré-requisitos e premissas)
Preenchido após desenvolvimento do script de automatização.

## Considerações sobre recuperação ou reinício
Preenchido após desenvolvimento do script de automatização.

## Considerações sobre registros rejeitados na carga
Preenchido após desenvolvimento do script de automatização.
