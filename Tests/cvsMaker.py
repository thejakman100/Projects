import requests
from bs4 import BeautifulSoup
import pandas as pd


html = requests.get('https://www.nytimes.com/interactive/2017/06/23/opinion/trumps-lies.html')
# print(html.text[0:500])
soup = BeautifulSoup(html.text, 'html.parser')
results = soup.find_all('span', attrs={'class': 'short-desc'})
len(results)
first_result = results[0]
records = []
for result in results:
    date = result.find('strong').text[0:-1] + ', 2017'
    lie = result.contents[1][0:-1]
    expl = result.find('a').text[1:-1]
    url = result.find('a')['href']
    records.append((date, lie, expl, url))
df = pd.DataFrame(records, columns=['date', 'lie', 'expl', 'url'])
df['date'] = pd.to_datetime(df['date'])
print(df.head())
print(df.tail())
df.to_csv('C:/Users/theja/Desktop/trump_lies.csv', index=False, encoding='utf-8')
