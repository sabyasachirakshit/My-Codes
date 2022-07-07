from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

driver = webdriver.Chrome()

product=[]
s=[]
m=[]
t=[]
w=[]
th=[]
f=[]
sat=[]
price=[]
rating=[]
day=[]
destination=[]
driver.get("https://www.goibibo.com/trains/kolkata-howrah-junction-hwh/")

content = driver.page_source
soup = BeautifulSoup(content)
for a in soup.findAll('a',href=True, attrs={'class':'table-head'}):
    product=a.find('td', attrs={'class':'train-name train-name-clamp'})
    price=a.find('td', attrs={'class':'train-name train-name-truncate'})
    destination=a.find('td', attrs={'class':'train-name train-name-truncate'})
    rating = a.find('p', attrs={'class': 'train-no'})
    day=a.find('p', attrs={'class':'daySchedule'})
product.append(product.text)
price.append(price.text)
destination.append(destination.text)
rating.append(rating.txt)
day.append(day.txt)

df = pd.DataFrame({'Product Name':product,'Price':price,'Destination':destination,'Rating':rating,'Day':day})
df.to_csv('dataset_railway.csv', index=False, encoding='utf-8')