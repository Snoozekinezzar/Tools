# enumerate_containers.py

> Inspired by the `Invoke-EnumerateAzureBlobs` function from `NetSPI/MicroBurst`, this Python script is designed to leverage the URL parameter "?restype=container&comp=list" for listing Azure blob storage containers.
> 
> [NetSPI/Microburst](https://github.com/NetSPI/MicroBurst)
> 
> [Microsoft API: list blobs](https://learn.microsoft.com/en-us/rest/api/storageservices/list-blobs?tabs=microsoft-entra-id)

## 🚀 Features

- **Container Listing:** Utilizes `enumerate_containers_permutations.txt` for dynamic container name retrieval.
- **Expandable List:** Easily add to the permutation list. Note: Each entry initiates three checks against the URL, so use judiciously to avoid brute force detection.

## 📋 How It Works

The script checks container names directly from the list, appending and prepending them to the account name for comprehensive coverage.

### 📝 Example Usage

Given an account name `allgoodcompany` and a permutation list entry `storage`, the script performs checks against the URL as follows:

1. `allgoodcompany`
2. `storageallgoodcompany`
3. `allgoodcompanystorage`

## 🛠️ Setup and Dependencies

- **Use the git function:** git clone https://github.com/Snoozekinezzar/Tools.git` to get the script from github.
- **Getting to your script:** cd /to/your/path` to load the script.
- **Using:** chmod +x enumerate_containers.py` to make the script into an executable.
- **Using the Python script:** .\enumerate_containers.py` and type the container name.
- **If it doesn't find any containers, then edit:** .\enumerate_containers_permutations.txt` to expand on the search parameters.

## ⚠️ Disclaimer

Use this tool responsibly and ethically during penetration testing or with explicit permission from the target organization.
It is similar to bruteforcing, so it is important that you are within Azure policies when automatically target the url.

---

*For more details on usage and enhancements, please refer to the comprehensive documentation and examples provided within the script.*
