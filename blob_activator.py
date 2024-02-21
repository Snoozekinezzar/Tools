#!/usr/bin/env python3
from azure.storage.blob import BlobClient

def access_blob(storage_account_name, container_name, blob_name):
    """
    Access and print the contents of a publicly accessible blob.

    Parameters:
    - storage_account_name: The name of the Azure Storage account.
    - container_name: The name of the blob container.
    - blob_name: The name of the blob to access.
    """

    # Constructing the full blob URL
    base_url = f"https://{storage_account_name}.blob.core.windows.net/{container_name}"
    full_blob_url = f"{base_url}/{blob_name}"

    # Creating a BlobClient object to access the blob anonymously
    blob_client = BlobClient.from_blob_url(full_blob_url)

    # Downloading and printing the content of the blob
    blob_data = blob_client.download_blob()
    content = blob_data.readall()
    print(content.decode('utf-8'))  # Assuming the content is text and UTF-8 encoded.

if __name__ == "__main__":
    storage_account_name = input("Storage account name: ")
    container_name = input("Container name: ")
    blob_name = input("Blob name: ")

    access_blob(storage_account_name, container_name, blob_name)
