from src.engine import create_driver, load_page
from src.parser import parse_wikipedia_table, parse_all_wikipedia_tables
from src.utils import add_timestamp, save_csv
from selenium.common.exceptions import TimeoutException

# Wikipedia URL - List of countries by population
WIKIPEDIA_URL = "https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population"

def main():
    driver = create_driver()
    all_data = []
    
    try:
        print(f"Loading Wikipedia page: {WIKIPEDIA_URL}")
        load_page(driver, WIKIPEDIA_URL)
        
        # Get the page source
        html = driver.page_source
        print(f"Page loaded. HTML length: {len(html)}")
        
        # Extract the first table
        table_data = parse_wikipedia_table(html, table_index=0)
        
        all_data.extend(table_data)
        print(f"Successfully extracted {len(table_data)} rows from Wikipedia table")
        
    except TimeoutException:
        print("ERROR: Page load timeout occurred")
    except Exception as e:
        print(f"ERROR occurred: {type(e).__name__}: {e}")
        import traceback
        traceback.print_exc()
    finally:
        driver.quit()
        print("Browser closed")
    
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
