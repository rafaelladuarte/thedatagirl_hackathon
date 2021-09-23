from google.cloud import bigquery

# Construct a BigQuery client object.
client = bigquery.Client()

table_id = "hackathon-a3-data.the_data_girls.empresas_1"

job_config = bigquery.LoadJobConfig(
    schema=[
        bigquery.SchemaField("cnpj_basico", "STRING"),
        bigquery.SchemaField("razao_social", "STRING"),
        bigquery.SchemaField("natureza_juridica", "STRING"),
        bigquery.SchemaField("qualificacao_responsavel", "STRING"),
        bigquery.SchemaField("porte_empresa", "STRING")
    ],
    skip_leading_rows=1,
    # The source format defaults to CSV, so the line below is optional.
    source_format=bigquery.SourceFormat.CSV,
)
uri = "gs://thedatagirls-hackathon-a3/EMPRESAS_2021-09-22_23-30-23.644004.csv"

load_job = client.load_table_from_uri(
    uri, table_id, job_config=job_config
)  # Make an API request.

load_job.result()  # Waits for the job to complete.

destination_table = client.get_table(table_id)  # Make an API request.
print("Loaded {} rows.".format(destination_table.num_rows))
