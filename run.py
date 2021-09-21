from google.cloud import bigquery
from etl import dados_simples,dominio,empresa,estabelecimento,socios
from database.bigquery import BigQuery
from download import DownloadFiles
from storage.bucket import Storage


cloud_storage = Storage()
big_query = BigQuery()

## download and send to storage
download = DownloadFiles()
download.start_download()

## etl dataframes
df = cloud_storage.get_csv()

## send to big query
data = df # em formato json
big_query.insert_batch(data,'nome tabela')

