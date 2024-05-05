from selenium import webdriver
from bs4 import BeautifulSoup

# Function to scrape all URLs containing /details/
def scrape_details_urls(url):
    # Initialize Selenium webdriver
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')  # Run in headless mode (without opening a browser window)
    driver = webdriver.Chrome(options=options)
    
    # Fetch the webpage
    driver.get(url)
    # Extract the page source
    page_source = driver.page_source
    driver.quit()  # Quit the webdriver
    
    # Parse the page source with BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')
    print(soup) 
    # Find all anchor tags containing /details/ followed by any characters
    detail_links = soup.find_all('a', href=lambda href: href and '/details/' in href)
    # Extract URLs
    urls = [link['href'] for link in detail_links]
    return urls

# URL of the webpage containing the links
url = "https://archive.org/details/hp_calculator_manuals?page=9"

# Scrape all URLs containing /details/
detail_urls = scrape_details_urls(url)
for detail_url in detail_urls:
    print(detail_url)
