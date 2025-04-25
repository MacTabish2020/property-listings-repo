from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

options = Options()
options.headless = False  # Set to True if you don't want the browser to pop up
options.add_argument('--disable-blink-features=AutomationControlled')

driver = webdriver.Chrome(options=options)

url = "https://www.99acres.com/search/property/buy/chennai-central?city=35&preference=S&area_unit=1&res_com=Rdriver.get(url)"

# Wait for listings to load fully
time.sleep(5)  # Optional: use WebDriverWait for better control

# Get the full rendered HTML
html = driver.page_source

# Save it to a file
with open("99acres_listings.html", "w", encoding="utf-8") as f:
    f.write(html)

driver.quit()
print("Saved HTML content successfully.")

