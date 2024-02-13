- Enumerate_containers.py
This script is inspired by the Invoke-EnumerateAzureBlobs function from NetSPI/MicroBurst. I encountered issues executing the function within PowerShell, prompting the creation of this Python script. It embodies the same concept of exploiting the URL parameter "?restype=container&comp=list".

Features:
Lists container names sourced from enumerate_containers_permutations.txt.
Allows for the expansion of the list at the user's discretion. However, for each entry, it performs a check on the URL three times. Therefore, caution is advised as this process can be considered a form of brute forcing.
Functionality
The script verifies container names exactly as they appear in the file, including both appending and prepending them to the account name.

Example:
Given an account name "allgoodcompany" and a permutation list containing "storage", the script checks against the URL as follows:

allgoodcompany
storageallgoodcompany
allgoodcompanystorage
Note: This revision aims to provide a clearer understanding of the script's purpose and usage. Ensure to review any technical details for accuracy to match your implementation.
