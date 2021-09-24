from google.cloud import bigquery

# source: https://cloud.google.com/bigquery/docs/loading-data-cloud-storage-csv#python

client = bigquery.Client()

table_id = "hackathon-a3-data.the_data_girls.pais"

job_config = bigquery.LoadJobConfig(
    schema = [
        bigquery.SchemaField("codigo", "STRING"),
        bigquery.SchemaField("pais", "STRING")
    ],
    skip_leading_rows = 0,
    source_format = bigquery.SourceFormat.CSV,
    encoding = "ISO-8859-1",
    field_delimiter = ";"
)

uri = "gs://thedatagirls-hackathon-a3/PAIS*"

load_job = client.load_table_from_uri(
    uri, table_id, job_config = job_config
)

load_job.result()

destination_table = client.get_table(table_id)
print("Loaded {} rows.".format(destination_table.num_rows))