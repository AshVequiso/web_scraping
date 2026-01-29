import requests
from src.parser import get_wikipedia_table, parse_all_wikipedia_tables
from src.utils import add_timestamp, save_csv

# Wikipedia URL - List of countries by population
WIKIPEDIA_URL = "https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population"

def main():
    all_data = []
    
    try:
        print(f"Loading Wikipedia page: {WIKIPEDIA_URL}")
        
        # Use requests instead of Selenium for static content
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
        response = requests.get(WIKIPEDIA_URL, headers=headers)
        response.raise_for_status()  # Raise error for bad status codes
        
        html = response.text
        print(f"Page loaded. HTML length: {len(html)}")
        
        # Extract the first table (HTML parsed only once)
        table_data = get_wikipedia_table(html, table_index=0)
        
        # Or extract all tables (HTML parsed only once):
        # table_data = parse_all_wikipedia_tables(html)
        
        all_data.extend(table_data)
        print(f"Successfully extracted {len(table_data)} rows from Wikipedia table")
        
    except requests.exceptions.RequestException as e:
        print(f"ERROR: Request failed - {e}")
    except Exception as e:
        print(f"ERROR occurred: {type(e).__name__}: {e}")
        import traceback
        traceback.print_exc()
    
    # Save the data
    if all_data:
        all_data = add_timestamp(all_data)
        save_csv(all_data, "data/processed/wiki_population.csv")
        print(f"✓ Data saved to data/processed/wiki_population.csv")
        print(f"✓ Total rows: {len(all_data)}")
    else:
        print("✗ No data extracted - check errors above")

if __name__ == "__main__":
    main()