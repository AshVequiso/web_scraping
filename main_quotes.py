from src.engine import create_driver, load_page_quotes
from src.parser import parse_quotes
from src.utils import add_timestamp, save_csv
from selenium.common.exceptions import TimeoutException

BASE_URL = "https://quotes.toscrape.com/js/page/{}/"

def main():
    driver = create_driver()
    all_quotes = []
    
    try:
        # Scrape multiple pages
        for page in range(1, 6):  # Pages 1-5 (about 50 quotes)
            print(f"Loading page {page}...")
            load_page_quotes(driver, BASE_URL.format(page))
            
            # Get the rendered HTML after JavaScript executes
            html = driver.page_source
            
            # Parse the quotes
            quotes = parse_quotes(html)
            all_quotes.extend(quotes)
            print(f"  Extracted {len(quotes)} quotes from page {page}")
        
        print(f"\n✓ Total quotes extracted: {len(all_quotes)}")
        
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
    if all_quotes:
        all_quotes = add_timestamp(all_quotes)
        save_csv(all_quotes, "data/processed/quotes.csv")
        print(f"✓ Data saved to data/processed/quotes.csv")
        print(f"✓ Total rows: {len(all_quotes)}")
    else:
        print("✗ No data extracted")

if __name__ == "__main__":
    main()