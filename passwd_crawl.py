import requests
import re

def scrape_website(url, output_file):
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Error: Failed to scrape website {url}")
        return

    html = response.text

    # Search for usernames and passwords in the HTML
    usernames = re.findall("(?i)username[=:]\s*(\S+)", html)
    passwords = re.findall("(?i)password[=:]\s*(\S+)", html)

    with open(output_file, "w") as f:
        if usernames:
            f.write("Found usernames:\n")
            for username in usernames:
                f.write(username + "\n")

        if passwords:
            f.write("Found passwords:\n")
            for password in passwords:
                f.write(password + "\n")

    print(f"Output written to file: {output_file}")

# Example usage
if __name__ == "__main__":
    url = input("Enter website URL: ")
    output_file = input("Enter output file name: ")
    scrape_website(url, output_file)
