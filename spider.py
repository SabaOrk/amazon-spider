import requests
import bs4
import json

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

url = 'https://www.amazon.com/DualShock-Wireless-Controller-PlayStation-Magma-4/dp/B01MD19OI2?pf_rd_p=190167bc-8caf-4fc0-8d35-69c23fc562c8&pd_rd_wg=0AJPx&pf_rd_r=BR06WNJDT18CCNS31SPW&ref_=pd_gw_unk&pd_rd_w=a6zNN&pd_rd_r=b09485d0-e782-4a5c-a3fc-12f010254eef&th=1'

response = requests.get(url, headers=headers)

print(response.text)

soup = bs4.BeautifulSoup(response.content, features="lxml")

title = soup.select("#productTitle")[0].get_text().strip()

categories = []
for li in soup.select("#wayfinding-breadcrumbs_container ul.a-unordered-list")[0].findAll("li"):
    categories.append(li.get_text().strip())

features = []

for li in soup.select("#feature-bullets ul.a-unordered-list")[0].findAll('li'):
    features.append(li.get_text().strip())

price = soup.select("#priceblock_saleprice")[0].get_text()

review_count = int(soup.select("#acrCustomerReviewText")[0].get_text().split()[0])

jsonObject = {'title': title, 'categories': categories, 'features': features, 'price': price, 'review_count': review_count}
print(json.dumps(jsonObject, indent=2))