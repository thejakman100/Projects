from bs4 import BeautifulSoup
import requests


def symbol(a):
    term = a
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}
    html = 'https://www.google.com/search?q={0}+stock&rlz=1C1CHZL_enUS713US713&oq={0}+stock&aqs=chrome..69i57j69i64l2.3631j0j7&sourceid=chrome&ie=UTF-8'.format(
        term)
    html2 = requests.get(html, headers=headers)
    soup = BeautifulSoup(html2.text, 'html.parser')
    results = soup.find_all('span', attrs={'class': 'HfMth'})
    if len(results) == 0:
        return False
    if 'NYSE: ' in results[0].text is False:
        return False
    if 'NASDAQ: ' in results[0].text is False:
        return False
    z = results[0].text
    exchange = []
    subtract = 8
    nyseQuestion = False
    nyse = ['N', 'Y', 'S', 'E']
    for x in range(len(z)):
        exchange.append(z[x])
        if exchange == nyse:
            nyseQuestion = True
            break
    if nyseQuestion is True:
        subtract = 6
    b = results[0].text[subtract:13]
    return b
