#!/usr/bin/env python3

import sys
import requests
from xml.etree import ElementTree

def list_blobs(account_name, container_name):
    session = requests.Session()  # Use a session for connection pooling
    url = f"https://{account_name}.blob.core.windows.net/{container_name}?restype=container&comp=list"
    
    try:
        response = session.get(url)
        response.raise_for_status()  # Raises an HTTPError for bad responses
    except requests.exceptions.HTTPError as e:
        print(f"Failed to list blobs. HTTP Error: {e.response.status_code}")
        return None
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None
    
    root = ElementTree.fromstring(response.content)
    blobs = []
    for blob in root.findall(".//Blob"):
        blobs.append({
            "name": blob.find("Name").text,
            "size": int(blob.find("Properties/Content-Length").text),
            "last_modified": blob.find("Properties/Last-Modified").text
        })
    
    return blobs

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: ./azure_blob_list.py <account_name> <container_name>")
        sys.exit(1)
    
    account_name, container_name = sys.argv[1:3]
    blob_list = list_blobs(account_name, container_name)
    if blob_list:
        print("\nList of blobs:")
        for blob in blob_list:
            print(f"- Name: {blob['name']}, Size: {blob['size']} bytes, Last Modified: {blob['last_modified']}")
