from google.cloud import bigquery

# source: https://cloud.google.com/bigquery/docs/loading-data-cloud-storage-csv#python

class BigQuery:
    def __init__(self):
        self.client = bigquery.Client() # Construct a BigQuery client object.
        self.uri = "gs://thedatagirls-hackathon-a3/"
        self.group_table = "hackathon-a3-data.the_data_girls."

    def create_schema(self,schema_base):
        """
        Receive a dictionary where the key is the field name
        and the value is the data type of the field in the table schema and
        returns a schema list in the default Big Query
        """

        schema = [
            bigquery.SchemaField(key, schema_base[key])
            for key in schema_base
        ] 

        return schema

    def create_job_config(self,schema_table):
        # Get the table schema by adding it to the table settings

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
        """
        Set the uri of the csv file in the bucket and the name of 
        the table it will receive the data load, then send it by API 
        request, waits for the job to complete and return api response
        """

        uri = self.uri + csv
        table_id = self.group_table + table

        load_job = self.client.load_table_from_uri(
            uri, 
            table_id, 
            job_config = job_config
        ) 

        load_job.result()

        destination_table = self.client.get_table(table_id) 

        return destination_table

    def start_send(self,schema_base,table,csv):
        """
        Function responsible for calling the schema creation functions,
        configuration of the request and sending the csv, returning to
        number of records entered
        """

        print(f'Creating schema for {table}...')
        schema = self.create_schema(schema_base)

        print('Creating configuration...')
        job_config = self.create_job_config(schema)

        print(f'Sending csv {csv} for {table}...')
        result = self.send_csv(table,csv,job_config)

        if result is None:
            print("Sent {} rows.".format(result.num_rows))


        
    


