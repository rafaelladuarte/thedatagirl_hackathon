from schemas.schema import all_schemas
from database.bigquery import BigQuery

big_query = BigQuery()

# for csv_table in all_schemas:
#     schema_base = csv_table['schema']
#     table = csv_table['table']
#     csv = csv_table['csv']
    
#     big_query.start_send(
#         schema_base=schema_base,
#         table= table,
#         csv= csv
#     )


if __name__ == "__main__":
    schema_teste = {
        'cnpj_basico' :"STRING",
        'cnpj_ordem' :"STRING",
        'cnpj_dv' :"STRING",
        'id_matriz_filial' :"STRING",
        'nome_fantasia':"STRING",
        'situacao_cadastral' :"STRING",
        'data_situ_cadastral' :"STRING",
        'motivo_situ_cadastral' :"STRING",
        'nome_cidade_exterior' :"STRING",
        'pais' :"STRING",
        'data_inicio_atividade':"STRING",
        'cnae_principal':"STRING",
        'cnae_secundario':"STRING",
        'tipo_logradouro':"STRING",
        'logradouro':"STRING",
        'numero':"STRING",
        'complemento':"STRING",
        'bairro':"STRING",
        'cep':"STRING",
        'uf':"STRING",
        'municipio':"STRING",
        'ddd1':"STRING",
        'telefone1':"STRING",
        'ddd2':"STRING",
        'telefone2':"STRING",
        'ddd_fax':"STRING",
        'fax':"STRING",
        'email':"STRING",
        'situacao_especial':"STRING",
        'data_situ_especial':"STRING"
    }

    table_teste = 'estabelecimento'
    csv_teste = 'ESTABELECIMENTO*'

    big_query.start_send(
        schema_base=schema_teste,
        table= table_teste,
        csv= csv_teste
    )



