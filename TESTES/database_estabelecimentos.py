from google.cloud import bigquery

# source: https://cloud.google.com/bigquery/docs/loading-data-cloud-storage-csv#python

client = bigquery.Client()

table_id = "hackathon-a3-data.the_data_girls.estabelecimentos"

job_config = bigquery.LoadJobConfig(
    schema = [
        bigquery.SchemaField("cnpj_basico", "STRING"),
        bigquery.SchemaField("cnpj_ordem", "STRING"),
        bigquery.SchemaField("cnpj_dv", "STRING"),
        bigquery.SchemaField("id_matriz_filial", "STRING"),
        bigquery.SchemaField("nome_fantasia", "STRING"),
        bigquery.SchemaField("situacao_cadastral", "STRING"),
        bigquery.SchemaField("data_situ_cadastral", "STRING"),
        bigquery.SchemaField("motivo_situ_cadastral", "STRING"),
        bigquery.SchemaField("nome_cidade_exterior", "STRING"),
        bigquery.SchemaField("pais", "STRING"),
        bigquery.SchemaField("data_inicio_atividade", "STRING"),
        bigquery.SchemaField("cnae_principal", "STRING"),
        bigquery.SchemaField("cnae_secundario", "STRING"),
        bigquery.SchemaField("tipo_logradouro", "STRING"),
        bigquery.SchemaField("logradouro", "STRING"),
        bigquery.SchemaField("numero", "STRING"),
        bigquery.SchemaField("complemento", "STRING"),
        bigquery.SchemaField("bairro", "STRING"),
        bigquery.SchemaField("cep", "STRING"),
        bigquery.SchemaField("uf", "STRING"),
        bigquery.SchemaField("municipio", "STRING"),
        bigquery.SchemaField("ddd1", "STRING"),
        bigquery.SchemaField("telefone1", "STRING"),
        bigquery.SchemaField("ddd2", "STRING"),
        bigquery.SchemaField("telefone2", "STRING"),
        bigquery.SchemaField("ddd_fax", "STRING"),
        bigquery.SchemaField("fax", "STRING"),
        bigquery.SchemaField("email", "STRING"),
        bigquery.SchemaField("situacao_especial", "STRING"),
        bigquery.SchemaField("data_situ_especial", "STRING")
    ],
    skip_leading_rows = 0,
    source_format = bigquery.SourceFormat.CSV,
    encoding = "ISO-8859-1",
    field_delimiter = ";"
)

uri = "gs://thedatagirls-hackathon-a3/ESTABELECIMENTO*"

load_job = client.load_table_from_uri(
    uri, table_id, job_config = job_config
)

load_job.result()

destination_table = client.get_table(table_id)
print("Loaded {} rows.".format(destination_table.num_rows))