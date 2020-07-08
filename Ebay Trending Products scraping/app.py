import requests
from lxml import html
import re
import json

resp = requests.get(url='https://www.ebay.com/deals/trending/all', headers = {
    'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36 Edg/83.0.478.58'
})

def write_json(Data):
    with open('data.json','w') as f:
        f.write(json.dumps(Data))


tree = html.fromstring(html=resp.text)

product_main = tree.xpath("//div[@class='spoke-itemgrid-container']/descendant::div[@class='col']")[0]
product_list = []

for product in product_main:
    title = product_main.xpath(".//div[@class='dne-itemtile-detail']/a/h3/span/span/text()")[0]
    price = product_main.xpath(".//div[@class='dne-itemtile-detail']/a/div/div/span/text()")[0]





    item = {
    'title' : title,
    'price': price

    }
    product_list.append(item)

print(item)
write_json(product_list)


