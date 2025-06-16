import requests
from bs4 import BeautifulSoup

def scrape():

    url = "https://www.cyride.com/schedules/summer-schedule/sunday/6-brown-south"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
    response = requests.get(url, headers = headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    print(soup)

if __name__ == '__main__':
    scrape()