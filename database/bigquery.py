from google.cloud import bigquery
import json

class BigQuery:
    def __init__(self):
        self.client = bigquery.Client()

    def insert_batch(self, data, table):

        table_name = ""

        errors = self.client.insert_rows_json(table_name, data)

        if errors == []:
            print(table_name + ": Success")
            print(f'Sent {len(data)} in {table_name}')
        else:
            print("Errors: {}".format(errors))