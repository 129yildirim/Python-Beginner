import requests
from bs4 import BeautifulSoup


def trade_spider(max_pages):
    page = 11
    while page <= max_pages:
        url = 'https://tortuga-ceviri.com/manga/berserk/berserk-' + str(page) + '/'
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, features="html.parser")
        for link in soup.find_all('a'):
            href = link.get('href')
            print(href)
        page = page + 1


def trade_spider2():
    url = 'https://www.reddit.com/t/ethics_and_philosophy/'
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, features="html.parser")
    for link in soup.find_all('a', {'class':'SQnoC3ObvgnGjWt90zD9Z _2INHSNB8V5eaWp4P0rY_mE'}):
        href = link.get('href')
        print(href)
    


trade_spider(11)
#trade_spider2()


        

