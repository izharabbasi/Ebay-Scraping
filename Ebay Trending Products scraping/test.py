import requests
from lxml import html
import json
import csv
 
def get(item):
    try:
        return item[0]
    except IndexError:
        return ""
 
 
def write_to_csv(data):
    headers = ['title', 'url' , 'price' , 'discount']
    with open('data.csv', 'w') as f:
        writer = csv.DictWriter(f, headers)
        writer.writeheader()
        writer.writerows(data)
        
 
 
scraped = []  # empty list
 
 
ebayurl = "https://www.ebay.com/globaldeals"
 
resp = requests.get(url=ebayurl, headers={
    "User-Agent":
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"
})
# Element Tree object
tree = html.fromstring(html=resp.text)
global_deals = tree.xpath("//div[@class='col']")
 
# start of loop
for global_deal in global_deals:
    ebay_information = {
        'title': get(global_deal.xpath(".//span[@class='ebayui-ellipsis-2']/text()")),
        'url': get(global_deal.xpath(".//a[starts-with(@href,'https')]/@href")),
        'price': get(global_deal.xpath(".//div/div[@itemscope='itemscope']/span[@itemprop='price']/text()")),
        'discount': get(global_deal.xpath(".//div/div/span/span[@class='itemtile-price-bold']/text()"))
    }
    scraped.append(ebay_information)
 

 
write_to_csv(scraped)