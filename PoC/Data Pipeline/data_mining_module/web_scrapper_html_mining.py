import requests
from bs4 import BeautifulSoup
import os
import pandas as pd

class WebScraper:
    def __init__(self, df, download_folder='downloads'):
        self.df = df
        self.download_folder = download_folder
        if not os.path.exists(self.download_folder):
            os.makedirs(self.download_folder)

    def download_file(self, url, file_name, contract_code):
        """Download each file found on the WebPage and save it under the contract-specific folder."""
        # Create a folder for the specific contract code
        contract_folder = os.path.join(self.download_folder, contract_code)
        if not os.path.exists(contract_folder):
            os.makedirs(contract_folder)

        response = requests.get(url, stream=True)
        if response.status_code == 200:
            file_path = os.path.join(contract_folder, file_name)
            with open(file_path, 'wb') as file:
                for chunk in response.iter_content(1024):
                    file.write(chunk)
            print(f'Downloaded: {file_name} into {contract_folder}')
        else:
            print(f'Failed to download {file_name} from {url}')
    
    def get_download_links(self, soup):
        links = soup.find_all('a', href=True)
        return [link['href'] for link in links if link['href'].endswith(('pdf', 'zip', 'docx'))]

    def scrape(self):
        """Identifies the routes to the files to be downloaded."""
        for index, row in self.df.iterrows():
            url = row['URL_CONTRATO']
            contract_code = row['CONTRACT_CODE']
            try:
                response = requests.get(url)
                if response.status_code == 200:
                    soup = BeautifulSoup(response.text, 'html.parser')
                    download_links = self.get_download_links(soup)
                    print(f'Download links for {contract_code}: {download_links}')
                    for link in download_links:
                        file_name = link.split('/')[-1]
                        full_url = link if link.startswith('http') else os.path.join(url, link)
                        self.download_file(full_url, file_name, contract_code)
                else:
                    print(f'Failed to retrieve {url}')
            except Exception as e:
                print(f'Error scraping {url} for contract {contract_code}: {e}')


scraper = WebScraper(df)
scraper.scrape()
