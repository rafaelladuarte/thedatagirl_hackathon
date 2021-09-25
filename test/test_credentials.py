from google.cloud import storage

def implicit():
    """
    Function used to check Google Cloud credentials. If everything's
    working fine, it prints the available buckets in that account.
    """
    storage_client = storage.Client()
    buckets = list(storage_client.list_buckets())
    print(buckets)

if __name__ == "__main__":
    implicit()