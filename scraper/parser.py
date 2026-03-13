from bs4 import BeautifulSoup

def parse_titles(html):
    soup = BeautifulSoup(html, "html.parser")

    titles = []

    for item in soup.select(".titleline a"):
        titles.append({
            "title": item.text,
            "link": item["href"]
        })

    return titles