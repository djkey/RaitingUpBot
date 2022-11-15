import requests
from bs4 import BeautifulSoup
import json

resp = requests.get('https://nakrutka.com/services.php')
# html = ''
with open('service.html', 'w', encoding='utf-8') as f:
    f.write(resp.text)
soup = BeautifulSoup(resp.text, 'lxml')
table = soup.find('tbody')

row = table.find_all('tr')

services = []
index = 0
for collum in row:
    # service = {}
    index += 1
    collum = collum.find_all('td')
    service = {
        "number": collum[0].text,
        "Description and statistics": collum[1].text.replace('\n', ' ').replace('\t', ''),
        "min-max order": collum[2].text,
        "rate per 1000": collum[3].text}
    services.append(service)
print(services)

with open('service.json', 'w', encoding='utf-8') as f:
    # f.write(json.dumps(services))
    json.dump(services, f, indent=4, ensure_ascii=False,)
