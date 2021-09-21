from etl import dados_simples,dominio,empresa,estabelecimento,socios
from database.bigquery import BigQuery
from storage.bucket import Storage

cloud_storage = Storage()
big_query = BigQuery()

list_csv_names = []
for csv in list_csv_names:
    df = cloud_storage.get_csv(csv)

    data = df # em formato json
    big_query.insert_batch(data,'nome tabela')