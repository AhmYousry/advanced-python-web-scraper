import requests

def fetch_page(url):
    response = requests.get(url)

    if response.status_code != 200:
        raise Exception("Failed to fetch page")

    return response.text