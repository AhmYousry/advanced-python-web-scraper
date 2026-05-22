from scraper.scraper import fetch_page
from scraper.parser import parse_titles
from scraper.exporter import export_csv

url = "https://news.ycombinator.com"

print(f"Fetching page: {url}")
html = fetch_page(url)

data = parse_titles(html)
print(f"Extracted {len(data)} articles")

export_csv(data, "data/output.csv")

print("Scraping completed")