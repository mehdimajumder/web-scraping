import requests
from bs4 import BeautifulSoup
import csv

# Function to fetch and parse a single page of the website
def fetch_page(page_number):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    url = f"ENTER URL{page_number}"
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return BeautifulSoup(response.text, 'html.parser')
    else:
        print(f"Failed to fetch page {page_number} with status code: {response.status_code}")
        return None

# Function to extract Data from a single page
def extract_codes(soup):
    # Replace 'your-css-selector-here' with the actual CSS selector
    codes = soup.find_all("CSS_SELECTOR_HERE")
    return [code.text.strip() for code in codes]

# Main function to scrape all codes
def scrape_codes():
    all_codes = []
    for i in range(0, 0):
        soup = fetch_page(i)
        if soup:
            codes = extract_codes(soup)
            all_codes.extend(codes)
            print(f"Extracted codes from page {i}")
    return all_codes

# Save the codes to a CSV file
def save_codes(codes):
    with open('ENTER_FILE_NAME.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        for code in codes:
            writer.writerow([code])

# Run the scraping
codes = scrape_codes()
save_codes(codes)
