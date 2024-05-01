import requests
from bs4 import BeautifulSoup
# still doesn't work

# URL of the tense guide page
url = "https://www.linguno.com/study/tenseGuide/2876/"

# Send a GET request to the URL
response = requests.get(url)

# Parse the HTML content
soup = BeautifulSoup(response.content, "html.parser")

# Find the tense guide elements
tense_guide_elements = soup.find_all("div",class_="tense_guide_conjugation_from")

fr_verb  = soup.find_all("div",class_="conjugation_area_cluster_verbs_verb")
en_verb  = soup.find_all("div",class_="conjugation_area_cluster_verbs_verb_definition")

# Extract the tense guide data
tense_guide_data = []
for element in tense_guide_elements:
    tense_name = element.find("span", class_="conjugation_area_cluster_verbs_verb")
    tense_example = element.find("span", class_="tense-example").text.strip()
    tense_guide_data.append({
        "tense_name": tense_name,
        "tense_example": tense_example
    })

# Print the tense guide data
for data in tense_guide_data:
    print(f"Tense Name: {data['tense_name']}")
    print(f"Tense Example: {data['tense_example']}")
    print()