import requests
import re

def scrape_website(url):
    response = requests.get(url)
    if response.status_code != 200:
        print("Error: Failed to scrape website")
        return

    html = response.text

    # search and extraction of usernames and passwords in the HTML
    usernames = re.findall("(?i)username[=:]\s*(\S+)", html)
    passwords = re.findall("(?i)password[=:]\s*(\S+)", html)

    if usernames:
        print("Found usernames:")
        for username in usernames:
            print(username)

    if passwords:
        print("Found passwords:")
        for password in passwords:
            print(password)

#usage
scrape_website("https://mywebsite.com")
