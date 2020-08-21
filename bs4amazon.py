import requests
from bs4 import BeautifulSoup
import json
import sys
import tkinter as tk
import time
from tkinter import filedialog,Text

url_arg = sys.argv[1:]
url1 = 'https://www.amazon.com/Panasonic-Headphones-RP-HJE120-K-Ergonomic-Comfort-Fit/dp/B003EM8008/ref=sr_1_3?crid=G28TBIQR3E2S&keywords=earbud+headphones&qid=1575925820&sprefix=ear%2Caps%2C258&sr=8-3'

url_better = str(url_arg)
url = url_better.replace(']','').replace('[','').replace('\'','')


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

page = requests.get(url, headers=headers)

soup1 = BeautifulSoup(page.content, "html.parser")

soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

print(soup2.prettify())

p_title = soup2.find(id="productTitle").get_text().strip()
p_price_str = ""
p_price = 0

try:
    p_price_str = soup2.find(id="priceblock_ourprice").get_text()
    p_price = float(p_price_str[1:5])
except:
    p_price_str = soup2.find(id="price_inside_buybox").get_text()
    p_price = float(p_price_str[1:5])

p_seller = soup2.find(id="bylineInfo").get_text()

jsonObject = {'productTitle': p_title, 'productPrice': p_price, 'productSeller': p_seller}
print(json.dumps(jsonObject, indent=2))

with open('products_json.txt', 'a') as jsonobj:
    jsonobj.write(str(jsonObject) + '\n')


'''
root = tk.Tk()
canvas = tk.Canvas(root,height=500,width=500,bg="#263D42")
canvas.pack()

inputField = tk.Entry(root,width=50)
inputField.pack()

root.mainloop()

time.sleep(10)
crawl_page(inputField.get())



import json
import xlsxwriter

d = json.dumps(jsonObject)

workbook = xlsxwriter.Workbook('data.xlsx')
worksheet = workbook.add_worksheet()

row = 0
col = 0

for key in d.keys():
    row += 1
    worksheet.write(row, col, json.dumps(key))
    for item in d[key]:
        worksheet.write(row, col + 1, json.dumps(item))
        row += 1

workbook.close()
'''

