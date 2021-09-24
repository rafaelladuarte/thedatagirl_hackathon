from google.cloud import bigquery

# source: https://cloud.google.com/bigquery/docs/loading-data-cloud-storage-csv#python

client = bigquery.Client()

table_id = "hackathon-a3-data.the_data_girls.socios"

job_config = bigquery.LoadJobConfig(
    schema = [
        bigquery.SchemaField("cnpj_basico", "STRING"),
        bigquery.SchemaField("id_de_socio", "STRING"),
        bigquery.SchemaField("nome_socio_razao_social", "STRING"),
        bigquery.SchemaField("cnpj_cpf_socio", "STRING"),
        bigquery.SchemaField("qualificacao_do_socio", "STRING"),
        bigquery.SchemaField("data_entrada_sociedade", "STRING"),
        bigquery.SchemaField("pais", "STRING"),
        bigquery.SchemaField("cpf_representante_legal", "STRING"),
        bigquery.SchemaField("nome_representante", "STRING"),
        bigquery.SchemaField("qualificacao_representante", "STRING"),
        bigquery.SchemaField("faixa_etaria", "STRING"),
    ],
    skip_leading_rows = 0,
    source_format = bigquery.SourceFormat.CSV,
    encoding = "ISO-8859-1",
    field_delimiter = ";"
)

uri = "gs://thedatagirls-hackathon-a3/SOCIO*"

load_job = client.load_table_from_uri(
    uri, table_id, job_config = job_config
)

load_job.result()

destination_table = client.get_table(table_id)
print("Loaded {} rows.".format(destination_table.num_rows))