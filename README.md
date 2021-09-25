# Hackathon de Engenharia de Dados - A3 Data Challenge Woman

<p align="center">
<img src="https://github.com/elladarte/thedatagirl_hackathon/blob/main/images/logo_hackathon.png"/>
</p>

## Equipe The Data Girls

<p align="center">
<img src="https://github.com/elladarte/thedatagirl_hackathon/blob/main/images/the_data_girls.png" alt="Image" height="200" width="200"/>
</p>

Participantes:
Rafaella Duarte
Carolina Dias

### Desafio

-  Os  times  devem  implementar  pipeline  de  extração,  transformação  e  disponibilização  de  dados.  Após  extração,  limpeza, organização e estruturação dos dados, as perguntas  chave do desafio devem ser respondidas de maneira visual;
- Fonte: Base CNPJ (Dado de 2010 a junho-2021);
- Livre utilização de ferramentas para compor a solução.

### Tabela de conteúdos
<!--ts-->
* [O Desafio](#desafio)
* [Tabela de Conteudo](#tabela-de-conteudo)
* [Perguntas Chaves](#perguntas-chaves)
* [Avaliação](#avaliação)
* [Solução](#solução)
    * [Arquitetura](#arquitetura)
    * [Extração dos dados](#extração-dos-dados)
    * [Tratamento dos dados](#tratamento-dos-dados)
    * [Analise dos dados](#analise-dos-dados)
    * [Visualização dos dados](#visualização-dos-dados)
<!--te-->

### Perguntas Chaves

1. Número de indústrias ativas por mês/ano entre 2010 - 2021, discriminado por MEI ou Simples, em cada município brasileiro.
2. Número de comércios que fecharam por mês/ano entre 2010 - 2021, discriminado por MEI ou Simples, em cada município brasileiro.
3. Número de CNPJ novos por mês/ano entre 2010 - 2021, discriminado por MEI ou Simples, em cada município brasileiro.
4. Qual o número de CNPJ que surgiram do grupo de educação superior, entre 2015 e 2021, discriminado por ano, em cada estado brasileiro?
5. Qual a classe de CNAE com o maior capital social médio no Brasil no último ano?
6. Qual a média do capital social das empresas de pequeno porte por natureza  jurídica no último ano?

### Avaliação

As soluções serão avaliadas pelos mentores de acordo com os  seguintes critérios:
- Escalabilidade;
- Confiabilidade;
- Facilidade de integração em Produção;
- Eficiência Operacional;
- Otimização de Custos.

### Solução
- Arquitetura
Foi utilizado o ecossistema do Google para a solução desse problema, em particular a Google Cloud Storage (GCP) e o Google Data Studio. Os motivos para a escolha dessas ferramentas são a facilidade de uso e integração total entre todas as ferramentas, além do baixo custo. Além disso, para contas novas há um bônus de 300 dólares em créditos, influenciando mais ainda a decisão de escolha desse serviço como um todo.

Na GCP foram utilizados os seguintes serviços:
Google Cloud Engine Computing para rodar os códigos.
Google Cloud Storage para o armazenamento dos dados.
Google BigQuery para a análise dos dados.
O Google Data Studio foi utilizado para as visualizações dos dados.

<p align="center">
<img src="https://github.com/elladarte/thedatagirl_hackathon/blob/main/images/arquitetura.png" alt="Image" height="600" width="800"/>
</p>

- Extração dos dados
- Tratamento dos dados
- Analise dos dados
- Visualização dos dados

### Deploy