# ObservaSampa: Automação de indicadores 
## Informações do processo
* **Processo:** Servidores ativos da PMSP
* **Versão:** 1.0
* **Objetivo:** Atualizar as variáveis do ObservaSampa que compõem os indicadores dos servidores da PMSP.

## Fontes
O [Portal de Dados Abertos](http://dados.prefeitura.sp.gov.br/) possui o conjunto de dados [Relação de Servidores Ativos da Prefeitura de São Paulo](http://dados.prefeitura.sp.gov.br/pt_PT/dataset/servidores-ativos-da-prefeitura) o qual lista a base de dados com diversas informações sobre todos os funcionários ativos da Administração Direta da Prefeitura de São Paulo, tais como nomes, cargos, órgão de lotação e perfil (sexo, idade, raça).

Mensalmente são inseridas bases como de [novembro de 2022](http://dados.prefeitura.sp.gov.br/dataset/bf5df0f4-4fb0-4a5e-b013-07d098cc7b1c/resource/a9e76078-8e89-472c-89ad-546ca71bf566/download/verificadoativos01-12-2022nov-2022.xlsx) que deve ser empregada para a automação.

## Destinos

Este processo tem como destino a criação da planilha com informações das variáveis (V0266 e V0199) formatada no template de importação do Intranet do ObservaSampa. Sendo uma tabela com as respectivas colunas: Variável, Região e Período (ver detalhes adiante na tabela de mapeamento).

## Frequência de execução

Espera-se executar esse processo anualmente com informações do mês de Dezembro de cada ano.

## Descrição do processo

### Para a variável V0266 (Servidoras ativas da administração direta do governo):
1. Baixar o arquivo de dezembro do último ano do conjunto de dados do Portal de Dados Abertos da PMSP [(dezembro-2021)](http://dados.prefeitura.sp.gov.br/dataset/bf5df0f4-4fb0-4a5e-b013-07d098cc7b1c/resource/6676c7de-9f1a-428b-91f7-3ff0f23f86b3/download/verificadoativos03-01-2022dez-2021.xlsx);
1. Contar a quantidade de linhas do arquivo considerando como filtro os registros da coluna "Sexo" igual a "F".

### Para a variável V0199 (Servidores municipais ativos da administração direta do governo): 
1. No mesmo arquivo de dezembro do último ano, contar a quantidade de linhas do arquivo desconsiderando qualquer filtro.

## Tabela de mapeamento dos dados

| Campo | Descrição | Tipo do dado | Tabela de origem | Campo de origem | Regra de transformação |
| ----- | --------- | ------------ | :--------------: | :-------------: | :--------------------: |
| Variável | Preencher com os nomes resumidos das variáveis, no caso desse processo, uma linha para V0266 e outra linha V0199 | String | N/A | N/A | N/A |
| Região | Preencher com a sigla da região do município de São Paulo | String | N/A | N/A | N/A |
| Ano | Preencher o cabeçalho com o valor do ano, de acordo com o arquivo de origem, por exemplo 2022 para o arquivo de origem dezembro/2022. Preencher as linhas de valores de acordo com o resultado obtido na contagem das linhas dos arquivos (ver descrição do processo acima) | String | N/A | N/A | N/A |

### Regras de transformações
Não se aplica

## Dependências (pré-requisitos e premissas)
Preenchido após desenvolvimento do script de automatização.

## Considerações sobre recuperação ou reinício
Preenchido após desenvolvimento do script de automatização.

## Considerações sobre registros rejeitados na carga
Preenchido após desenvolvimento do script de automatização.
