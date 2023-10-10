import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.amazon.in/s?k=iphone&crid=DGPEIGA9VYOO&sprefix=iphone%2Caps%2C205&ref=nb_sb_noss_1"
headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36'
    }

data = {'title': [], 'price': []}

r = requests.get(url, headers=headers)

soup = BeautifulSoup(r.text, 'html.parser')
print(soup.prettify())

# spans = soup.find(class_="a-size-medium")
# print(spans)

# spans = soup.select("div.sg-col-inner")
# print(spans)  # ye bht sare div de raha hai 

spans = soup.select("span.a-size-medium.a-color-base.a-text-normal")
prices = soup.select("span.a-price")
for span in spans:
    print(span.string)
    data["title"].append(span.string)

for price in prices:
    if not("a-text-price" in price.get("class")):
        print(price.find("span").get_text())
        data["price"].append(price.find("span").get_text())
        if len(data["price"])==len(data["title"]):
            break

df = pd.DataFrame.from_dict(data)
# df.to_csv("data.csv", index=False)
df.to_excel("data.xlsx", index=False)