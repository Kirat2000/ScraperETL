from bs4 import BeautifulSoup
import requests
import csv
import pandas as pd

url="https://www.flipkart.com/search?q=body%20oil&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"
response = requests.get(url)
htmlcontent = response.content
soup = BeautifulSoup(htmlcontent,"html.parser")

#print(soup.prettify)

products=[]
prices=[]
ratings=[]
weights=[]

product=soup.find('a',attrs={'class':'s1Q9rs'})

for a in soup.find_all('div', attrs={'class':'_4ddWXP'}):
  name=a.find('a',attrs={'class':'s1Q9rs'})
  price=a.find('div',attrs={'class':'_30jeq3'})
  rating=a.find('div',attrs={'class':'_3LWZlK'})
  weight=a.find('div',attrs={'class':'_3Djpdu'})
  products.append(name.text)
  try:
    prices.append(price.text)
    ratings.append(rating.text)
    weights.append(weight.text)
  except AttributeError:
    prices.append('NA')
    ratings.append('NA')
    weights.append('NA')
    

print(products)
print(prices)
print(ratings)
print(weights)


a = {'Product Name':products,'Ratings':ratings,'Prices':prices, 'Quantity':weights}
df = pd.DataFrame.from_dict(a, orient='index')
df.to_csv('bodyoil.csv')
