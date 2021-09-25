from google.cloud import bigquery

# source: https://cloud.google.com/bigquery/docs/loading-data-cloud-storage-csv#python

class BigQuery:
    def __init__(self):
        self.client = bigquery.Client() # Construct a BigQuery client object.
        self.uri = "gs://thedatagirls-hackathon-a3/"
        self.group_table = "hackathon-a3-data.the_data_girls."

    def create_schema(self,schema_base):
        schema = [
            bigquery.SchemaField(key, schema_base[key])
            for key in schema_base
        ] 

        return schema

    def create_job_config(self,schema_table):
        job_config = bigquery.LoadJobConfig(
            schema = schema_table,
            skip_leading_rows = 0,
            # The source format defaults to CSV, so the line below is optional.
            source_format = bigquery.SourceFormat.CSV,
            encoding = "ISO-8859-1",
            field_delimiter = ";"
        )

        return job_config

    def send_csv(self,table,csv,job_config):
        uri = self.uri + csv
        table_id = self.group_table + table

        load_job = self.client.load_table_from_uri(
            uri, 
            table_id, 
            job_config = job_config
        ) # Make an API request.

        load_job.result() # Waits for the job to complete.

        destination_table = self.client.get_table(table_id) # Make an API request.

        return destination_table

    def start_send(self,schema_base,table,csv):

        print(f'Creating schema for {table}...')
        schema = self.create_schema(schema_base)

        print('Creating configuration...')
        job_config = self.create_job_config(schema)

        print(f'Sending csv {csv} for {table}...')
        result = self.send_csv(table,csv,job_config)

        if result is None:
            print("Sent {} rows.".format(result.num_rows))


        
    


