# Hackathon de Engenharia de Dados - A3 Data Challenge Women

<p align="center">
<img src="https://github.com/elladarte/thedatagirl_hackathon/blob/main/images/logo_hackathon.png" alt="Image" height="250" width="600"/>
</p>

## Equipe The Data Girls

<p align="center">
<img src="https://github.com/elladarte/thedatagirl_hackathon/blob/main/images/the_data_girls.png" alt="Image" height="200" width="200"/>
</p>

Participantes:
- [Carolina Dias](https://www.linkedin.com/in/carodias/)
- [Rafaella Duarte](https://www.linkedin.com/in/rafaella-duarte-044276130/)

### 🟣 [Pitch da Solução (2 minutos)](https://youtu.be/bd6tAhl_dVQ)
### 🟣 [Demonstraçao da Solução (5 minutos)]()
### 🟣 [Dashboard com as Respostas](https://datastudio.google.com/u/0/reporting/e24cf11b-9f7d-45ae-864e-807b0b874004/page/p_v4vb5pcunc)


## Desafio

-  Os  times  devem  implementar  pipeline  de  extração,  transformação  e  disponibilização  de  dados.  Após  extração,  limpeza, organização e estruturação dos dados, as perguntas  chave do desafio devem ser respondidas de maneira visual;
- Fonte: Base CNPJ (Dado de 2010 a junho-2021);
- Livre utilização de ferramentas para compor a solução.

## Tabela de Conteúdos
<!--ts-->
* [O Desafio](#desafio)
* [Tabela de Conteudo](#tabela-de-conteudo)
* [Perguntas Chaves](#perguntas-chaves)
* [Avaliação](#avaliação)
* [Solução](#solução)
    * [Arquitetura](#arquitetura)
    * [Extração dos dados](#extração-dos-dados)
    * [Tratamento e Analise dos dados](#tratamento-e-analise-dos-dados)
    * [Visualização dos dados](#visualização-dos-dados)
<!--te-->

## Perguntas Chave

1. Número de indústrias ativas por mês/ano entre 2010 - 2021, discriminado por MEI ou Simples, em cada município brasileiro.
2. Número de comércios que fecharam por mês/ano entre 2010 - 2021, discriminado por MEI ou Simples, em cada município brasileiro.
3. Número de CNPJ novos por mês/ano entre 2010 - 2021, discriminado por MEI ou Simples, em cada município brasileiro.
4. Qual o número de CNPJ que surgiram do grupo de educação superior, entre 2015 e 2021, discriminado por ano, em cada estado brasileiro?
5. Qual a classe de CNAE com o maior capital social médio no Brasil no último ano?
6. Qual a média do capital social das empresas de pequeno porte por natureza  jurídica no último ano?

## Avaliação

As soluções serão avaliadas pelos mentores de acordo com os  seguintes critérios:
- Escalabilidade;
- Confiabilidade;
- Facilidade de integração em Produção;
- Eficiência Operacional;
- Otimização de Custos.

## Solução

###Arquitetura

Foi utilizado o ecossistema do Google para a solução desse problema, em particular a Google Cloud Storage (GCP) e o Google Data Studio. Os motivos para a escolha dessas ferramentas são a facilidade de uso e integração total entre todas as ferramentas, além do baixo custo. Além disso, para contas novas há um bônus de 300 dólares em créditos, influenciando mais ainda a decisão de escolha desse serviço como um todo.

Na GCP foram utilizados os seguintes serviços:
- Google Cloud Engine Computing para rodar os códigos.
- Google Cloud Storage para o armazenamento dos dados.
- Google BigQuery para a análise dos dados.
- Google Data Studio foi utilizado para as visualizações dos dados.

<p align="center">
<img src="https://github.com/elladarte/thedatagirl_hackathon/blob/main/images/arquitetura.png" alt="Image" height="400" width="600"/>
</p>

- Extração dos dados

Os dados foram extraidos por meio de um scraper que percorre a pagina da Receita Federal, baixamos os arquivos zip e em seguida extraimos os arquivos csv para o Google Cloud Storage. Decidimos enviar para a cloud os dados brutos, para nao ser necessario refazer a coleta para o tratamento dos dados, assim economizando capacidade computacional e tempo.

Script automatizado responsável ==> run_storage.py

- Tratamento e Análise dos dados

Para economizar poder computacional, preferimos realizar o tratamento e a analise de dados no Google BigQuery. Desta forma, realizamos a carga dos arquivos csv brutos existentes no Google Cloud Storage, enviando cada um deles para suas respectivas tabelas, de acordo com o schema criado.

<p align="center">
<img src="https://github.com/elladarte/thedatagirl_hackathon/blob/main/images/diagrama_DB.png" alt="Image" height="400" width="600"/>
</p>

Apos a carga das tabelas no Google BigQuery, criamos uma tabela unica com junção das informações das empresas, estabelecimentos, e socios pelo cnpj basico, alem de combinar as colunas com chaves estrangeiras das tabelas de dominio (municipio, pais, motivo, atuação juridica, qualificação do socio e cnae), para facilitar a criação das tabelas utilizadas para a visualização. 

Script automatizado responsavel ==> run_bigquery.py

- Visualização dos dados

Como há um volume muito grande de dados, decidimos refletir os dados por meio de dashboards no Google DataStudio, uma ferramente de geração de relatorios compativel com varias ferramentas, incluido o Google BigQuery onde esta nossos dados. Com o Google DataStudio conseguimos gerar relatorios interativos em tempo real, alem de ser uma ferramenta gratuita.

<img src="https://github.com/elladarte/thedatagirl_hackathon/blob/main/images/dash_questao1.png" alt="Image" height="200" width="350"/>
<img src="https://github.com/elladarte/thedatagirl_hackathon/blob/main/images/dash_questao2.png" alt="Image" height="200" width="350"/>
<img src="https://github.com/elladarte/thedatagirl_hackathon/blob/main/images/dash_questao3.png" alt="Image" height="200" width="350"/>
<img src="https://github.com/elladarte/thedatagirl_hackathon/blob/main/images/dash_questao4.png" alt="Image" height="200" width="350"/>
<img src="https://github.com/elladarte/thedatagirl_hackathon/blob/main/images/dash_questao5.png" alt="Image" height="200" width="350"/>
<img src="https://github.com/elladarte/thedatagirl_hackathon/blob/main/images/dash_questao6.png" alt="Image" height="200" width="350"/>

