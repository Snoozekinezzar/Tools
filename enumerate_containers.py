#!/usr/bin/env python3

import requests

def read_container_names_from_file(file_path):
    """
    Read container name permutations from a given file.
    """
    with open(file_path, 'r') as file:
        return [line.strip() for line in file.readlines()]

def check_container_exists(account_name, container_name):
    """
    Check if a given container exists within an Azure Storage account.
    """
    url = f"https://{account_name}.blob.core.windows.net/{container_name}?restype=container&comp=list"
    response = requests.get(url)
    if response.status_code == 200:
        return True
    else:
        return False

def enumerate_containers(account_name, permutations_file):
    """
    Enumerate through a list of container name permutations to find which containers exist,
    trying the name as is, prepended, and appended to the account name.
    """
    container_names = read_container_names_from_file(permutations_file)
    existing_containers = []
    for name in container_names:
        # Direct permutation
        if check_container_exists(account_name, name):
            print(f"Container found: {name}")
            existing_containers.append(name)

        # Permutation appended to account name
        appended_name = f"{account_name}{name}"
        if check_container_exists(account_name, appended_name):
            print(f"Container found: {appended_name}")
            existing_containers.append(appended_name)

        # Permutation prepended to account name
        prepended_name = f"{name}{account_name}"
        if check_container_exists(account_name, prepended_name):
            print(f"Container found: {prepended_name}")
            existing_containers.append(prepended_name)

    return existing_containers

# Example usage
account_name = input("Enter the Azure Storage account name: ")
permutations_file = "enumerate_container_permutations.txt"

# Enumerate containers based on permutations
found_containers = enumerate_containers(account_name, permutations_file)
print("Found Containers:", found_containers)
