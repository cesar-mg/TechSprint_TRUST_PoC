import requests
from bs4 import BeautifulSoup
import os

class WebScraper:
    def __init__(self, urls, download_folder='downloads'):
        self.urls = urls
        self.download_folder = download_folder
        if not os.path.exists(self.download_folder):
            os.makedirs(self.download_folder)

    def download_file(self, url, file_name):
        """Download each file found in the WebPage."""
        response = requests.get(url, stream=True)
        if response.status_code == 200:
            file_path = os.path.join(self.download_folder, file_name)
            with open(file_path, 'wb') as file:
                for chunk in response.iter_content(1024):
                    file.write(chunk)
            print(f'Downloaded: {file_name}')
        else:
            print(f'Failed to download {file_name} from {url}')
    
    def get_download_links(self, soup):
        links = soup.find_all('a', href=True)
       
        
        return [link['href'] for link in links if link['href'].endswith(('pdf', 'zip', 'docx'))]

    def scrape(self):
        """Identifies the routes to the files to be downloaded."""
        for url in self.urls:
            try:
                response = requests.get(url)
                if response.status_code == 200:
                    soup = BeautifulSoup(response.text, 'html.parser')
                    download_links = self.get_download_links(soup)
                    print(download_links)
                    for link in download_links:
                        file_name = link.split('/')[-1]
                        full_url = link if link.startswith('http') else os.path.join(url, link)
                        self.download_file(full_url, file_name)
                else:
                    print(f'Failed to retrieve {url}')
            except Exception as e:
                print(f'Error scraping {url}: {e}')

import pandas as pd

df = pd.DataFrame({
    'urls': [
        'https://comunidad.comprasdominicana.gob.do//Public/Tendering/OpportunityDetail/Index?noticeUID=DO1.NTC.13691061']
})

scraper = WebScraper(df['urls'].tolist())
scraper.scrape()
