## 💡 Github usage (Linux)

- **Use the git function:** `git clone https://github.com/Snoozekinezzar/Tools.git` **to get the script from GitHub.**

# enumerate_containers.py

> Inspired by the `Invoke-EnumerateAzureBlobs` function from `NetSPI/MicroBurst`, this Python script is designed to leverage the URL parameter "?restype=container&comp=list" for listing Azure blob storage containers.
> 
> [NetSPI/Microburst](https://github.com/NetSPI/MicroBurst)
> 
> [Microsoft API: list blobs](https://learn.microsoft.com/en-us/rest/api/storageservices/list-blobs?tabs=microsoft-entra-id)

## 📖 Features

- **Container Listing:** Utilizes `enumerate_containers_permutations.txt` for dynamic container name retrieval.
- **Expandable List:** Easily add to the permutation list. Note: Each entry initiates three checks against the URL, so use judiciously to avoid brute force detection.

## 📋 How It Works

The script checks container names directly from the list, appending and prepending them to the account name for comprehensive coverage.

### 📝 Example Usage

Given an account name `allgoodcompany` and a permutation list entry `storage`, the script performs checks against the URL as follows:

1. `allgoodcompany`
2. `storageallgoodcompany`
3. `allgoodcompanystorage`

## 🛠️ Setup and Dependencies (Linux)

- **Use the git function:** `git clone https://github.com/Snoozekinezzar/Tools.git` **to get the script from GitHub.**
- **Getting to your script:** `cd /to/your/path` **to get to the script.**
- **Use:** `chmod +x enumerate_containers.py` **to make the script into an executable.**
- **Use the Python script:** `.\enumerate_containers.py` **and type the container name.**
- **If it doesn't find any containers, then edit:** `.\enumerate_containers_permutations.txt` **to expand on the search parameters.**

---

*For more details on usage and enhancements, please refer to the comprehensive documentation and examples provided within the script.*

# list_blobs_info.py

> This script combines the account name and container name to list blobs, detailing file types, sizes, and modification dates.
>
> [Microsoft API: List Blobs](https://learn.microsoft.com/en-us/rest/api/storageservices/list-blobs?tabs=microsoft-entra-id)

## 📖 Features

- **Blob Information:** Lists blobs with file types, sizes, and last modified dates.
- **Combines Account and Container Names:** Efficiently retrieves blob information by combining account and container names.

## 📋 How It Works

The script requires the account name and container name as inputs to list the blobs and their information.

### 📝 Example of output

List of blobs:
- Name: Employee.ovpn, Size: 2921 bytes, Last Modified: Mon, 06 Aug 2023 11:09:12 GMT
- Name: permission.pem, Size: 3002 bytes, Last Modified: Mon, 18 Aug 2023 11:08:05 GMT
- Name: logocompany.png, Size: 10763 bytes, Last Modified: Mon, 16 Aug 2022 11:08:05 GMT

## 🛠️ Setup and Dependencies (Linux)

- **Getting to your script:** `cd /to/your/path` **to get to the script.**
- **Use:** `chmod +x list_blobs_info.py` **to make the script into an executable.**
- **Use the Python script:** `.\list_blobs_info.py` `<ACCOUNT NAME>` `<CONTAINER NAME>` **to start listing blobs with their details.**






## ⚠️ Disclaimer

These tools should be used responsibly and ethically during penetration testing or with explicit permission from the target organization. Ensure compliance with Azure policies when accessing URLs to list the information.

---

*Refer to the comprehensive documentation and examples provided within the script for further details on usage and enhancements.*

