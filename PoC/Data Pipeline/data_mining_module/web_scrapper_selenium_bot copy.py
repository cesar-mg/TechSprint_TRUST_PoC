from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

class WebScraperSelenium:
    def __init__(self, urls, download_folder='downloads'):
        self.urls = urls
        self.download_folder = download_folder
        if not os.path.exists(self.download_folder):
            os.makedirs(self.download_folder)

        options = webdriver.ChromeOptions()
        prefs = {"download.default_directory": os.path.abspath(self.download_folder)}
        options.add_experimental_option("prefs", prefs)

        self.driver = webdriver.Chrome(options=options)

    def scrape(self):
        """Creates a bot to execute the WebScrapping."""
        for url in self.urls:
            try:
                self.driver.get(url)
                time.sleep(5)  


                download_links = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_all_elements_located((By.XPATH, "//a[starts-with(@id, 'lnkDownloadLinkP3Gen')]"))
                )


                for link in download_links:
                    time.sleep(3)
                    link.click()
                    time.sleep(2)  

                print(f'Download completed for {url}')
            except Exception as e:
                print(f'Error processing {url}: {e}')

    def close(self):
        self.driver.quit()


