from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
import pandas as pd

class WebScraperSelenium:
    def __init__(self, df, download_folder='PoC/Data Pipeline/database/bronze'):
        self.df = df[['URL_CONTRATO','CODIGO_CONTRATO']]
        self.download_folder = download_folder
        if not os.path.exists(self.download_folder):
            os.makedirs(self.download_folder)
        
    def setup_driver(self, download_path):
        """Set up the Chrome driver with the specified download path."""
        options = webdriver.ChromeOptions()
        prefs = {"download.default_directory": os.path.abspath(download_path)}
        options.add_experimental_option("prefs", prefs)
        
        driver = webdriver.Chrome(options=options)
        return driver

    def scrape(self):
        """Creates a bot to execute the WebScrapping."""
        for index, row in self.df.iterrows():
            url = row['URL_CONTRATO']
            contract_code = row['CODIGO_CONTRATO']

            # Create a folder for the specific contract code
            contract_folder = os.path.join(self.download_folder, contract_code)
            if not os.path.exists(contract_folder):
                os.makedirs(contract_folder)

            # Initialize the driver with the specific download folder
            driver = self.setup_driver(contract_folder)

            try:
                driver.get(url)
                time.sleep(5)  

                download_links = WebDriverWait(driver, 10).until(
                    EC.presence_of_all_elements_located((By.XPATH, "//a[starts-with(@id, 'lnkDownloadLinkP3Gen') or starts-with(@id, 'lnkDownloadDocument')]"))
                )

                for link in download_links:
                    time.sleep(3)
                    link.click()
                    time.sleep(2)  

                print(f'Download completed for {url} into {contract_folder}')
            except Exception as e:
                print(f'Error processing {url} for contract {contract_code}: {e}')
            finally:
                driver.quit()

    def close(self):
        pass  # No longer needed since the driver is closed after each contract

# Example usage with DataFrame
# Tests
import pandas as pd

# Path to your CSV file
csv_file_path = 'PoC/Data Pipeline/database/bronze/Contracts.csv'  # Replace with the actual path to your CSV file

# Read the DataFrame from the CSV file
df = pd.read_csv(csv_file_path)

# Initialize the WebScraperSelenium with the DataFrame
scraper = WebScraperSelenium(df)

# Perform the web scraping process
scraper.scrape()

# The driver is automatically closed after each scrape, no need to manually close
