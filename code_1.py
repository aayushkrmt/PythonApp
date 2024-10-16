import requests
from bs4 import BeautifulSoup
import json

url = 'https://www.geeksforgeeks.org/python-programming-language/'

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    
    data = {
        'title': soup.title.text if soup.title else 'No title found',
        'paragraphs': [],
        'headings': []
    }
    
    paragraphs = soup.find_all('p')
    for p in paragraphs:
        data['paragraphs'].append(p.text)
    
    headings = soup.find_all(['h1', 'h2', 'h3'])
    for heading in headings:
        data['headings'].append({
            'type': heading.name,
            'text': heading.text
        })
    
    json_data = json.dumps(data, indent=4)
    
    print(json_data)
else:
    print(f'Failed to retrieve the page. Status code: {response.status_code}')