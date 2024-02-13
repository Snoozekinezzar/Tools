# Enumerate_containers.py

> Inspired by the `Invoke-EnumerateAzureBlobs` function from `NetSPI/MicroBurst`, this Python script is designed to leverage the URL parameter "?restype=container&comp=list" for listing Azure blob storage containers.

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

- **Importing the Module:** Run `Import-Module .\Enumerate_containers.psm1` to load the script into your environment.
- **Trusting the Code:** Use `dir -Recurse .\PathToScript | Unblock-File` to recursively trust the downloaded files.

## ⚠️ Disclaimer

Use this tool responsibly and ethically during penetration testing or with explicit permission from the target organization.

---

*For more details on usage and enhancements, please refer to the comprehensive documentation and examples provided within the script.*
