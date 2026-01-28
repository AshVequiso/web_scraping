def display_menu():
    print("\n" + "="*60)
    print("WEB SCRAPER PROJECT - Select a scraper to run:")
    print("="*60)
    print("1. Wikipedia Scraper (Static Content)")
    print("   - Scrapes country population data from Wikipedia")
    print("   - Output: data/processed/wiki_population.csv")
    print()
    print("2. Quotes Scraper (JavaScript-Rendered Content)")
    print("   - Scrapes quotes from quotes.toscrape.com/js")
    print("   - Output: data/processed/quotes.csv")
    print()
    print("3. Run Both Scrapers")
    print()
    print("0. Exit")
    print("="*60)

def main():
    while True:
        display_menu()
        choice = input("\nEnter your choice (0-3): ").strip()
        
        if choice == "1":
            print("\n Running Wikipedia Scraper...\n")
            import main_wikipedia
            main_wikipedia.main()
            
        elif choice == "2":
            print("\n Running Quotes Scraper...\n")
            import main_quotes
            main_quotes.main()
            
        elif choice == "3":
            print("\n Running Wikipedia Scraper...\n")
            import main_wikipedia
            main_wikipedia.main()
            
            print("\n Running Quotes Scraper...\n")
            import main_quotes
            main_quotes.main()
            
        elif choice == "0":
            print("\n✓ Exiting. Goodbye!")
            break
            
        else:
            print("\n❌ Invalid choice. Please enter 0, 1, 2, or 3.")
        
        # Ask if user wants to run another scraper
        if choice in ["1", "2", "3"]:
            continue_choice = input("\n\nRun another scraper? (y/n): ").strip().lower()
            if continue_choice != 'y':
                print("\n✓ Exiting. Goodbye!")
                break

if __name__ == "__main__":
    main()