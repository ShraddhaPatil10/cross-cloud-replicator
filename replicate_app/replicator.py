# replicate_app/replicator.py
import os
import shutil
from .utils import retry_on_exception

@retry_on_exception
def replicate_file(s3_bucket, s3_key):
    source_path = f"mock_storage/s3/{s3_key}"
    dest_path = f"mock_storage/gcs/{s3_key}"

    os.makedirs(os.path.dirname(dest_path), exist_ok=True)

    if os.path.exists(dest_path):
        return "Already Exists"

    shutil.copy(source_path, dest_path)
    return "Success"

