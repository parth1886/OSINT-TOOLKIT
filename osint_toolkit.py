import whois
import requests
from bs4 import BeautifulSoup
import subprocess
import json
import os

# Module 1: Domain and IP Reconnaissance
def domain_recon(domain):
    try:
        domain_info = whois.whois(domain)
        print("WHOIS Information:\n", domain_info)
    except Exception as e:
        print(f"Error in WHOIS lookup: {e}")

# Module 2: Email Reconnaissance
def email_recon(email):
    try:
        response = requests.get(f"https://haveibeenpwned.com/api/v3/breachedaccount/{email}")
        if response.status_code == 200:
            print("This email has been part of a breach.")
        else:
            print("This email has not been found in any breach.")
    except Exception as e:
        print(f"Error checking email breaches: {e}")

# Module 3: Username Reconnaissance
def username_recon(username):
    try:
        print(f"Checking social networks for username: {username}")
        subprocess.run(["sherlock", username], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Sherlock error: {e}")

# Module 4: Social Media Reconnaissance
def social_media_recon(username):
    social_urls = {
        'Twitter': f"https://twitter.com/{username}",
        'GitHub': f"https://github.com/{username}",
        'LinkedIn': f"https://www.linkedin.com/in/{username}/"
    }
    print("Social Media Presence:")
    for platform, url in social_urls.items():
        response = requests.get(url)
        if response.status_code == 200:
            print(f"Found {username} on {platform}: {url}")
        else:
            print(f"{username} not found on {platform}")

# Module 5: Website Data Extraction
def website_data_extraction(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        print("Title of the page:", soup.title.string)
        print("Links on the page:")
        for link in soup.find_all('a'):
            print(link.get('href'))
    except Exception as e:
        print(f"Error in website data extraction: {e}")

# Module 6: Password Breach Check (Sample Check with Have I Been Pwned)
def password_breach_check(password):
    try:
        sha1_pass = hashlib.sha1(password.encode()).hexdigest().upper()
        response = requests.get(f"https://api.pwnedpasswords.com/range/{sha1_pass[:5]}")
        if sha1_pass[5:] in response.text:
            print("This password has been found in a data breach.")
        else:
            print("This password has not been found in any data breach.")
    except Exception as e:
        print(f"Error checking password breach: {e}")

# Module 7: Search Engine Recon
def google_dorking(query):
    print("Use Google Dorking manually for best results:")
    print(f"https://www.google.com/search?q={query}")

# Module 8: People Search
def people_search(name):
    print(f"Performing people search for: {name}")
    urls = [
        f"https://www.whitepages.com/name/{name.replace(' ', '%20')}",
        f"https://www.linkedin.com/search/results/people/?keywords={name.replace(' ', '%20')}"
    ]
    for url in urls:
        print(f"Check: {url}")

# Main Program Execution
def main():
    print("Welcome to the OSINT Toolkit")
    print("Select an option:")
    print("1. Domain Recon")
    print("2. Email Recon")
    print("3. Username Recon")
    print("4. Social Media Recon")
    print("5. Website Data Extraction")
    print("6. Password Breach Check")
    print("7. Google Dorking")
    print("8. People Search")
    
    option = input("Enter your choice: ")
    if option == '1':
        domain = input("Enter domain: ")
        domain_recon(domain)
    elif option == '2':
        email = input("Enter email: ")
        email_recon(email)
    elif option == '3':
        username = input("Enter username: ")
        username_recon(username)
    elif option == '4':
        username = input("Enter username: ")
        social_media_recon(username)
    elif option == '5':
        url = input("Enter website URL: ")
        website_data_extraction(url)
    elif option == '6':
        password = input("Enter password to check: ")
        password_breach_check(password)
    elif option == '7':
        query = input("Enter search query: ")
        google_dorking(query)
    elif option == '8':
        name = input("Enter name: ")
        people_search(name)
    else:
        print("Invalid option selected.")

if __name__ == "__main__":
    main()

