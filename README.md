# Web Scraper Project

A professional-grade web scraping pipeline built with Selenium and BeautifulSoup for extracting data from static and JavaScript-rendered websites.

## 🎯 Overview

This project demonstrates a hybrid web scraping approach that combines:
- **Selenium WebDriver** for browser automation and JavaScript-rendered content
- **BeautifulSoup** for high-speed HTML parsing
- **Pandas** for data processing and CSV export

The project includes two scrapers:
1. **Wikipedia Scraper** - Extracts tabular data from Wikipedia pages
2. **Quotes Scraper** - Scrapes JavaScript-rendered quotes from quotes.toscrape.com

---

## 🔧 Prerequisites

Before you begin, ensure you have the following installed:

### Required Software

1. **Python 3.8 or higher**
   - Download from: https://www.python.org/downloads/
   - Verify installation:
```bash
     python --version
```

2. **Google Chrome Browser**
   - Download from: https://www.google.com/chrome/
   - Note: ChromeDriver is automatically managed by Selenium 4.6+

3. **Git** (for cloning the repository)
   - Download from: https://git-scm.com/downloads
   - Verify installation:
```bash
     git --version
```

### Optional but Recommended

- **Visual Studio Code** or any IDE
- **Windows Terminal** or **Command Prompt**

---

## 📦 Installation

Follow these steps to set up the project on your local machine:

### Step 1: Clone the Repository
```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/web_scraper_project.git

# Navigate to the project directory
cd web_scraper_project
```

### Step 2: Create a Virtual Environment

**Windows:**
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
venv\Scripts\activate
```

**Mac/Linux:**
```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate
```

You should see `(venv)` in your terminal prompt.

### Step 3: Install Dependencies
```bash
# Upgrade pip (optional but recommended)
python -m pip install --upgrade pip

# Install required packages
pip install -r requirements.txt
```

**Expected packages:**
- `selenium==4.27.1` - Browser automation
- `beautifulsoup4==4.12.3` - HTML parsing
- `pandas==2.2.3` - Data manipulation
- `requests==2.32.3` - HTTP requests (for testing)

### Step 4: Verify Installation
```bash
# Check if packages are installed
pip list
```

You should see all the packages listed above.

### Step 5: Create Required Directories

The script will auto-create these, but you can create them manually:
```bash
mkdir data
mkdir data\raw
mkdir data\processed
mkdir logs
```

---

## 📁 Project Structure
```
web_scraper_project/
│
├── data/                       # Data storage
│   ├── raw/                   # Unprocessed scraper output
│   └── processed/             # Clean CSV files ready for analysis
│       ├── wiki_population.csv
│       └── quotes.csv
│
├── logs/                       # Log files (future use)
│
├── src/                        # Source code
│   ├── __init__.py            # Package initializer
│   ├── engine.py              # Selenium WebDriver setup and navigation
│   ├── parser.py              # BeautifulSoup parsing functions
│   └── utils.py               # Helper functions (timestamps, file I/O)
│
├── main.py                     # Interactive menu launcher
├── main_wikipedia.py           # Wikipedia scraper
├── main_quotes.py              # Quotes scraper (JS-rendered)
│
├── .gitignore                  # Git ignore rules
├── requirements.txt            # Python dependencies
└── README.md                   # 
```

---

## ⚙️ Configuration

### Change Target URLs

**For Wikipedia scraper** (`main_wikipedia.py`):
```python
# Line 6: Change to any Wikipedia page with tables
WIKIPEDIA_URL = "https://en.wikipedia.org/wiki/List_of_countries_by_GDP_(nominal)"
```

**For Quotes scraper** (`main_quotes.py`):
```python
# Line 5: Change page range
for page in range(1, 11):  # Scrape pages 1-10
```

### Disable Headless Mode (See Browser)

Edit `src/engine.py`, line 11:
```python
# Comment out this line to see the browser
# options.add_argument("--headless")
```

### Change Output Paths

Edit in respective `main_*.py` files:
```python
# Example: Change output location
save_csv(all_data, "data/processed/my_custom_name.csv")
```

---

## 📊 Output

### CSV Files

All scraped data is saved as CSV files with timestamps:

**Wikipedia Output** (`data/processed/wiki_population.csv`):
```csv
Rank,Country / Dependency,Population,% of world,Date,Source,scraped_at
1,India,"1,450,935,791",17.8%,1 Jan 2024,Official estimate,2024-01-29T10:30:45.123456
2,China,"1,419,321,278",17.4%,31 Dec 2023,National estimate,2024-01-29T10:30:45.123456
...
```

**Quotes Output** (`data/processed/quotes.csv`):
```csv
text,author,tags,scraped_at
"The world as we have created it...",Albert Einstein,"change, deep-thinking, thinking, world",2024-01-29T10:35:22.654321
"It is our choices...",J.K. Rowling,"abilities, choices",2024-01-29T10:35:22.654321
...
```