import requests
from bs4 import BeautifulSoup
import json

url = 'https://www.geeksforgeeks.org/python-programming-language/'

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Find the "Similar Reads" section by its heading
    similar_reads_section = soup.find('div', {'class': 'similar-reads'})  # Adjust selector as needed
    similar_reads = []
    
    if similar_reads_section:
        # Extract all links under the "Similar Reads" section
        links = similar_reads_section.find_all('a')
        for link in links:
            similar_reads.append({
                'title': link.text.strip(),
                'url': link['href']
            })
    
    data = {
        'similar_reads': similar_reads
    }
    
    json_data = json.dumps(data, indent=4)
    print(json_data)
    
else:
    print(f'Failed to retrieve the page. Status code: {response.status_code}')
