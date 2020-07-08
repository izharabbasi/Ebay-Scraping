import requests
from lxml import html
import json
import csv

def write_to_json(product):
    with open('product.json' , 'w') as f:
        f.write(json.dumps(product))


def write_to_csv(product):
    headers = ['title', 'sold_last_hour' , 'rating', 'condition' , 'price' , 'shipping']
    with open('product.csv','w') as f:
        writer = csv.DictWriter(f, headers)
        writer.writeheader()
        writer.writerow(product)


resp = requests.get(url='https://www.ebay.com/itm/50-PCS-3-Ply-Disposable-Face-Mask-Non-Medical-Surgical-Earloop-Mouth-Cover/174284210785?_trkparms=5079%3A0', headers={
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36 Edg/83.0.478.58'

})
tree = html.fromstring(html=resp.text)

title = tree.xpath("//div[@id='LeftSummaryPanel']/descendant::h1/text()")[0]
sold_last_hour = tree.xpath("//div[@id='LeftSummaryPanel']/descendant::span[2]/text()")[0]
num_sold = ''.join(list(filter(lambda x: x.isdigit(),sold_last_hour)))
rating = tree.xpath("//div[@id='LeftSummaryPanel']/descendant::span[4]/text()")[0]
rating_number = '.'.join(list(filter(lambda x: x.isdigit(), rating)))
condition = tree.xpath("//div[@id='mainContent']/descendant::div[@class='u-flL condText  ']/text()")[0]
price = tree.xpath("//div[@id='mainContent']/descendant::div[@id='vi-mskumap-none']/span[1]/text()")[0]
shipping = tree.xpath("//div[@id='mainContent']/descendant::span[@class='vi-geo-na shp-sub-text']/text()")[0].strip()


product_infomation = {
    'title': title,
    'sold_last_hour':num_sold,
    'rating':rating_number,
    'condition': condition,
    'price' : price,
    'shipping':shipping

}

print(product_infomation)
write_to_json(product_infomation)
write_to_csv(product_infomation)