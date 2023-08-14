import socket


# Function to check if a subdomain is valid (resolves to an IP address)
def is_subdomain_valid(subdomain, domain):
    try:
        socket.gethostbyname(f"{subdomain}.{domain}")
        return True
    except socket.gaierror:
        return False


# Ask the user for the target domain and wordlist file path
target_domain = input("Enter the target domain: ")
wordlist_path = input("Enter the path to the wordlist file: ")

# Read the wordlist from the specified file into a list
with open(wordlist_path, "r") as file:
    wordlist = file.read().splitlines()

# Print the subdomains being scanned
print(f"Scanning subdomains for {target_domain} using {wordlist_path} wordlist:")
found_subdomains = []

# Loop through each subdomain in the wordlist
for subdomain in wordlist:
    # Check if the current subdomain is valid for the target domain
    if is_subdomain_valid(subdomain, target_domain):
        # If valid, add it to the list of found subdomains and print it
        found_subdomains.append(subdomain)
        print(f"Found: {subdomain}.{target_domain}")

# If no subdomains were found, print a message
if not found_subdomains:
    print("No subdomains found.")
