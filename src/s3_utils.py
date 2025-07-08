"""
s3_utils.py

Description:
Provides utility functions for AWS S3 interaction

Purpose:
To manage data contributions into and out of the raw data lake

Author: Benjamin DeHass
Date: 2025-07-08
Version: 0.1.0

Dependencies:
    boto3

Usage:
    run directly via python src/s3_utils.py.
"""
import boto3
from botocore.exceptions import ClientError

def list_s3_buckets():
    """ 
    Lists all S3 buckets associated with the configured AWS credentials.
    """
    s3_client = boto3.client('s3')
    try:
        response = s3_client.list_buckets()
        print("Existing S3 Buckets:")
        for bucket in response['Buckets']:
            print(f"- {bucket['Name']}")
        return [bucket['Name'] for bucket in response['Buckets']]
    except ClientError as e:
        print(f"Error listing buckets: {e}")
        return []

def upload_file_to_s3(local_file_path, bucket_name, s3_key):
    """
    Uploads a local file to an S3 bucket.

    Args:
        local_file_path (str): The path to the local file to upload.
        bucket_name (str): The name of the S3 bucket.
        s3_key (str): The key (path) for the object in S3.
    """
    s3_client = boto3.client('s3')
    try:
        s3_client.upload_file(local_file_path, bucket_name, s3_key)
        print(f"Successfully uploaded {local_file_path} to s3://{bucket_name}/{s3_key}")
    except ClientError as e:
        print(f"Error uploading file {local_file_path}: {e}")

def download_file_from_s3(bucket_name, s3_key, local_file_path):
    """
    Downloads a file from an S3 bucket to a local path.

    Args:
        bucket_name (str): The name of the S3 bucket.
        s3_key (str): The key (path) for the object in S3.
        local_file_path (str): The path where the file will be saved locally.
    """
    s3_client = boto3.client('s3')
    try:
        s3_client.download_file(bucket_name, s3_key, local_file_path)
        print(f"Successfully downloaded s3://{bucket_name}/{s3_key} to {local_file_path}")
    except ClientError as e:
        print(f"Error downloading file {s3_key}: {e}")

if __name__ == "__main__":
    list_s3_buckets()

    RAW_BUCKET = "pokemon-tcg-raw-data-bdehass"

    # Test upload
    local_test_file_upload = "my_first_upload.txt"
    s3_object_key = "test_uploads/programmatic_upload.txt"
    upload_file_to_s3(local_test_file_upload, RAW_BUCKET, s3_object_key)

    # Test download
    local_test_file_download = "downloaded_from_s3.txt"
    download_file_from_s3(RAW_BUCKET, s3_object_key, local_test_file_download)