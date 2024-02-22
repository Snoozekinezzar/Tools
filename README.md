## 💡 Github usage (Linux)

- **Use the git function:** `git clone https://github.com/Snoozekinezzar/Tools.git` **to get the scripts from GitHub.**

<br>
<br>

# enumerate_containers.py

> Inspired by the `Invoke-EnumerateAzureBlobs` function from `NetSPI/MicroBurst`, this Python script is designed to leverage the URL parameter "?restype=container&comp=list" for listing Azure blob storage containers.
> 
> [NetSPI/Microburst](https://github.com/NetSPI/MicroBurst)
> 
> [Microsoft API: list blobs](https://learn.microsoft.com/en-us/rest/api/storageservices/list-blobs?tabs=microsoft-entra-id)

## 📖 Features

- **Container Listing:** Utilizes `enumerate_containers_permutations.txt` for dynamic container name retrieval.
- **Expandable List:** Easily add to the permutation list. Note: Each entry initiates three checks against the URL, so use judiciously to avoid brute force detection or IP lockout.

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

<br>
<br>

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

<br>
<br>

# blob_activator.py

> This script combines the account name, container name and specific blob name to access and read a publicly available blob, anonymously.

## 📖 Features

- **Blob Information:** Assuming the content is text and UTF-8 encoded, it will print out the information contained in blob files.

## 📋 How It Works

The script requires the account name, container name and blob name as inputs to access and print out data in the blob.

### 📝 Example of output of a .pem file

```
-----BEGIN CERTIFICATE-----
MIIDHzCCAgegAwIBAgIUaEcJmhc/7DjCPPyZLV0fWO1gczwDQYJKoZIhvcNAQEL
BQAwHzELMAkGA1UEBhMCTkwxEDAOBgNVBAoMB1NlY3VyYSAHhcNMjIwMzIyMTQz
NjU3WhcNMzIwMzE5MTQzNjU3WjAfMQswCQYDVQQGEwJOTDEQA4GA1UECgwHU2Vj
dXJhIDCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEBAzepUaYNoTsuWSk
Zb9pgbIJrMEAp9oJuIGNlMgOxMcTHVix6Scb9Q3odWwBE39BhIc+cy8y3OpeuRq
ADo98RIlBv8HkVYdOubR84NZvD/ugZfWJMrNCYFzOrRLeY53OGGIxVJessyem5l
DQYJKoZIhvcNAQELBQADggEBAK5JzdK7q7eYegr93EA+mzm53+qCqdQtdFOAEzA
dGpQcV9LWKHxbiVMl8/QrGhlD5LNsLmNsrtWKbGAcHMPDPdwWCjsF7YALlu9Js9
lCRwyHaUTIss6YtnRVrcQSsclVzCG5yJoX8PHskGtvzg8Bs1xsPM5H9qXvjCQqU
9wYNe6QaCbpznNbewoqijLWkwDiHbmuxwBoTp8fFxjtFnBXYsf4oTPKFeBqIq07
SP9OM5Qp0jQLt54H1NcTNe+6Vw2/11ZH6NOiLgHBIK+50sCiYeh8d35t+PLrH4k
6CXu0gLU3UZeTR65rVpScRGLnS+fLCWgc0MzyuolbBLVYfw=
-----END CERTIFICATE-----
-----BEGIN PRIVATE KEY-----
MIIEvwIBADANBgkhkiG9w0BAQEFAASCBKkwggSlAgEAAoIBAQDM3qVGmDaE7Llk
pGW/aYGyCazBAKfabiBjZTIDsTHEx1YseknG/UN6HVsARN/QYSJnPnMvMtzqXrk
agA6PfESJQb/B5FWHrm0fODWbw/7oGX1iTKzQmBczq0S3mOdzhhoCMVSXrLMnpu
3NSGRbUg2x7xJd+eDtHLfcqVAWS21QvcNnjWkIi+zD1mh8kuNpz6hd3MH6lZfuz
FdFIPBGQAtUCgYEAjnnDRCh7A14fXQJHSsr2kd22JNODQ2kNKM0LMMdTBVk0pZ+
3Shz3th77ueB0NIzwDunKtIrpKHfMS/Y9CLaqB9p+LayFYqAfXl2mFB/NKje8cm
pGvRQa3xtQPU/VzJ1Xs/K/nzXpnlCy2gV79E2UE6AFAgoH7XjA5e4hO5O0CgYEA
qrrK+dhjhwP05bNa91F21uBHc+sl/d/5MN1w9ou1XE9IsQ0vDTiN4OwyAhmrNnO
fG/mnlpXfPzZmtTo58HnYruDrVHpdeIrZOmFsgtONkihW0X+189SSbBhESw3NUP
lOBF9rmceXDUGKxdL0Z3cp8IZ7xbmnv37bQ8/brTfECgYB38BuP+2JifsqhCO4V
QwqzeI6QhETFZNpwBMLua/J6B/beDYNQNylWNmhMZ5UrL+ZE+q83nHb6OuQvwwm
2JfOQqPWC33oDLgfSCJM4kZIt2K3AIozYmoSbRa1g5WEL/2Z39/Kg+qjz1cX1UG
h3A+1OWJej8nKg9XTz25Ra1qzg==
-----END PRIVATE KEY-----
```

## 🛠️ Setup and Dependencies (Linux)

- **Getting to your script:** `cd /to/your/path` **to get to the script.**
- **Use:** `chmod +x blob_activator.py` **to make the script into an executable.**
- **Use the Python script:** `.\blob_activator.py` **and type the container name, then storageaccount name, then blob name.**

<br>
<br>
<br>
<br>

# database_connector.py

> And alternative and pythoninc way to access databases using SQL. 

## 📖 Features

- **help function:** Gets a list of commonly used drivers
- **SQL query:** Enables the use of SQL to query the database tables 

## 📋 How It Works

The script guides you through the different information needed to access the database and enables you to write SQL to query the database tables.

### 📝 Example Usage

```
┌──┌──(brokenazure㉿ctf)
└─$ ./database_connector.py
Enter server name: <servername>.database.windows.net
Enter database name: <databasename>
Enter username: <user>
Enter password: <password>
Enter driver (type 'help' to list common drivers):
Enter driver: {ODBC Driver 17 for SQL Server}
Connected to the database. Type 'exit' to quit.
Enter SQL command: select table_name from <databasename>.information_schema.tables
['table_name']
('database_firewall_rules',)
('employee_data',)
```

```
Enter SQL command: select * from employee_data
['usernames', 'informations']
('Employee123', 'coolstuff',)
```

## 🛠️ Setup and Dependencies (Linux)

- **Use the git function:** `git clone https://github.com/Snoozekinezzar/Tools.git` **to get the script from GitHub.**
- **Getting to your script:** `cd /to/your/path` **to get to the script.**
- **Use:** `chmod +x database_connector.py` **to make the script into an executable.**
- **Use the Python script:** `.\database_connector.py` **and type the container name.**

---

*For more details on usage and enhancements, please refer to the comprehensive documentation and examples provided within the script.*

## ⚠️ Disclaimer

These tools should be used responsibly and ethically during penetration testing or with explicit permission from the target organization. Ensure compliance with Azure policies when accessing URLs to list the information.

---

*Refer to the comprehensive documentation and examples provided within the script for further details on usage and enhancements.*

