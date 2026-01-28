from bs4 import BeautifulSoup
import pandas as pd

def parse_wikipedia_table(html, table_index=0):

    soup = BeautifulSoup(html, "html.parser")
    
    # Find all tables with class 'wikitable'
    tables = soup.find_all("table", class_="wikitable")
    
    if not tables:
        print("No wikitable found on this page")
        return []
    
    if table_index >= len(tables):
        print(f"Table index {table_index} out of range. Found {len(tables)} tables.")
        table_index = 0
    
    table = tables[table_index]
    
    # Extract headers
    headers = [th.text.strip() for th in table.find_all("th")]
    
    # Extract rows
    rows = []
    for tr in table.find_all("tr")[1:]:  # Skip header row
        cells = [td.text.strip() for td in tr.find_all("td")]
        if cells:
            # Convert list to dictionary with headers as keys
            row_dict = {}
            for i, cell in enumerate(cells):
                header = headers[i] if i < len(headers) else f"Column_{i}"
                row_dict[header] = cell
            rows.append(row_dict)
    
    return rows

def parse_all_wikipedia_tables(html):
    soup = BeautifulSoup(html, "html.parser")
    tables = soup.find_all("table", class_="wikitable")
    
    print(f"Found {len(tables)} wikitable(s) on the page")
    
    all_data = []
    for idx, table in enumerate(tables):
        table_data = parse_wikipedia_table(html, table_index=idx)
        # Add table number to each row
        for row in table_data:
            row["table_number"] = idx
        all_data.extend(table_data)
    
    return all_data

def parse_quotes(html):
    soup = BeautifulSoup(html, "html.parser")
    
    quotes = []
    
    # Find all quote containers
    quote_divs = soup.find_all("div", class_="quote")
    
    if not quote_divs:
        print("Warning: No quotes found on this page")
        return []
    
    for quote_div in quote_divs:
        # Extract quote text
        text_elem = quote_div.find("span", class_="text")
        text = text_elem.get_text(strip=True) if text_elem else ""
        
        # Extract author
        author_elem = quote_div.find("small", class_="author")
        author = author_elem.get_text(strip=True) if author_elem else ""
        
        # Extract tags
        tag_elems = quote_div.find_all("a", class_="tag")
        tags = [tag.get_text(strip=True) for tag in tag_elems]
        
        quotes.append({
            "text": text,
            "author": author,
            "tags": ", ".join(tags)  # Join tags as comma-separated string
        })
    
    return quotes