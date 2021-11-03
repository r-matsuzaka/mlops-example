from google.cloud import storage

bucket_name = "ml_model_store"
storage_client = storage.Client()
storage_client.create_bucket(bucket_name)

for bucket in storage_client.list_buckets():
    print(bucket.name)
