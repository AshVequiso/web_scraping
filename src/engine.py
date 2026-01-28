from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def create_driver():
    options = Options()
    options.add_argument(
        "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    )
    options.add_argument("--headless")  # Remove to see browser
    options.add_argument("--disable-blink-features=AutomationControlled")
    return webdriver.Chrome(options=options)

def load_page(driver, url):
    driver.get(url)
    
    # Wait for Wikipedia main content
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "content"))
    )
    
    # Wait specifically for tables
    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "wikitable"))
        )
        print("Wikitable found and loaded")
    except Exception as e:
        print(f"Warning: No wikitable found - {e}")

def load_page_quotes(driver, url):
    driver.get(url)
    
    # Wait for the quotes to be rendered by JavaScript
    # This is the KEY difference - without Selenium, you wouldn't see any quotes!
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "quote"))
    )
    
    # Optional: Wait a bit longer to ensure all quotes are loaded
    WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "quote"))
    )