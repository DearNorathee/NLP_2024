# https://www.verbix.com/webverbix/portuguese/tomar

# still have error with selenium
# seems like using import requests could not get the table component

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

language = "portuguese"
verb = "tomar"
browser_path = r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"


# Setup Selenium WebDriver using Service
# service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome()

url02 = f"https://www.verbix.com/webverbix/go.php?&D1=2&T1={verb}"

url = f"https://www.verbix.com/webverbix/{language}/{verb}"
driver.get(url)
# Fetch the webpage
response = requests.get(url)
response.raise_for_status()  # Checks if the request was successful

driver.get(url)

element = driver.find_element_by_class_name("tense_guide_more_verbs")
element.click()

# Get the page source after the click event
html = driver.page_source
# Parse the HTML content
soup = BeautifulSoup(response.text, 'html.parser')

# Find all tables
tables = soup.find_all('table')

# Process each table
for i, table in enumerate(tables):
    # Assuming you want to print each row of the table
    print(f"Table {i + 1}:")
    for row in table.find_all('tr'):
        row_data = [td.get_text(strip=True) for td in row.find_all(['td', 'th'])]
        print(row_data)