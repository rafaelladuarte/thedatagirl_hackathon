from etl import dados_simples, dominio, empresa, estabelecimento, socios
from database.bigquery import BigQuery
from mycloud.bucket import MyStorage

import dask.dataframe as dd

cloud_storage = MyStorage()
big_query = BigQuery()

list_csv_names = cloud_storage.list_files()

for csv in list_csv_names:
    df = cloud_storage.get_csv(csv)
    
    print(df.head())
#    data = df # em formato json
#    big_query.insert_batch(data, 'nome tabela')