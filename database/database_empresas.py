from google.cloud import bigquery

# source: https://cloud.google.com/bigquery/docs/loading-data-cloud-storage-csv#python

client = bigquery.Client()

table_id = "hackathon-a3-data.the_data_girls.empresas_1"

job_config = bigquery.LoadJobConfig(
    schema = [
        bigquery.SchemaField("cnpj_basico", "STRING"),
        bigquery.SchemaField("razao_social", "STRING"),
        bigquery.SchemaField("natureza_juridica", "STRING"),
        bigquery.SchemaField("qualificacao_responsavel", "STRING"),
        bigquery.SchemaField("capital_social", "STRING"),
        bigquery.SchemaField("porte_empresa", "STRING"),
        bigquery.SchemaField("ente_responsavel", "STRING")
    ],
    skip_leading_rows = 0,
    source_format = bigquery.SourceFormat.CSV,
    encoding = "ISO-8859-1",
    field_delimiter = ";"
)

uri = "gs://thedatagirls-hackathon-a3/EMPRESAS*"

load_job = client.load_table_from_uri(
    uri, table_id, job_config = job_config
)

load_job.result()

destination_table = client.get_table(table_id)
print("Loaded {} rows.".format(destination_table.num_rows))