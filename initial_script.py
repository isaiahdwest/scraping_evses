# Scraping clippercreek data


import requests
from bs4 import BeautifulSoup

full_url = "https://store.clippercreek.com/commercial?_ga=2.59037869.1294860290.1646013353-245234298.1646013353"


base_url = "https://store.clippercreek.com/"

headers = {
    'user_agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.83 Safari/537.1'
    }
productLinks = []

def get_content(url = None):
    r = requests.get(url)

    soup = BeautifulSoup(r.content, 'lxml')

    return soup

def productName(content = None):
    heading = content.select('h1')[0].text.strip()
    return heading

    
for x in range(1,4):
    url = f'https://store.clippercreek.com/commercial?page={x}'
    soup = get_content(url)


    product_list = soup.find_all('div', class_ = 'product-thumb')

    # print(product_list)


    for item in product_list:
        for link in item.find_all('a', href = True):
            productLinks.append(link['href'])

### go through each product

prod_specs = {}
for link in productLinks[0:2]:
    print(link)
    soup = get_content(link)
    
    prod_specs[productName(soup)] = {'Desc':[], 'Specs':[], 'Price':[]}
    
