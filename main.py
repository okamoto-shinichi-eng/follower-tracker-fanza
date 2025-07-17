import datetime
import csv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import re

def extract_followers(page_source):
    match = re.search(r'(\d[\d,]*) Followers', page_source)
    return match.group(1).replace(",", "") if match else "N/A"

def scrape_follower_count():
    url = "https://x.com/fanzagames_jhg"
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(options=options)

    try:
        driver.get(url)
        driver.implicitly_wait(10)
        followers = extract_followers(driver.page_source)
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        with open("logs/followers.csv", "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([timestamp, followers])
        print(f"{timestamp}: {followers} followers")

    finally:
        driver.quit()

if __name__ == "__main__":
    scrape_follower_count()
