import requests
import pandas as pd
from bs4 import BeautifulSoup

URL = "https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}

response = requests.get(URL, headers=headers)
print("Status code:", response.status_code)
print("Length of page:", len(response.text))

response = requests.get(URL, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")
table = soup.find("table", class_="wikitable")

def scrape_wikipedia_table():
    response = requests.get(URL)
    soup = BeautifulSoup(response.text, "html.parser")

    # Find the first sortable wikitable
    table = soup.find("table", class_="wikitable")

    headers = [th.text.strip() for th in table.find_all("th")]

    rows = []
    for tr in table.find_all("tr")[1:]:
        cells = [td.text.strip() for td in tr.find_all("td")]
        if cells:
            rows.append(cells)

    df = pd.DataFrame(rows, columns=headers)
    df.to_csv("data/processed/wiki_population.csv", index=False)

    print("Wikipedia table scraped successfully!")

if __name__ == "__main__":
    scrape_wikipedia_table()
