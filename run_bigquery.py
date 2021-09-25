from schemas.schema import all_schemas
from database.bigquery import BigQuery

big_query = BigQuery()

for csv_table in all_schemas:
    schema_base = csv_table['schema']
    table = csv_table['table']
    csv = csv_table['csv']
    
    big_query.start_send(
        schema_base=schema_base,
        table= table,
        csv= csv
    )


if __name__ == "__main__":
    schema_teste = {
        'codigo':"STRING",
        'nome':"STRING",
    }

    table_teste = 'cnae'
    csv_teste = 'CNAE*'

    big_query.start_send(
        schema_base=schema_teste,
        table= table_teste,
        csv= csv_teste
    )



