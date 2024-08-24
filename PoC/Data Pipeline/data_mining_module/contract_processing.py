import pandas as pd
from web_scrapper_selenium_bot import WebScraperSelenium
class ContractFilter:
    def __init__(self, file_path):
        """
        Initializes the ContractFilter with the path to the CSV file.
        
        :param file_path: Path to the contracts CSV file.
        """
        self.file_path = file_path
    
    def load_data(self):
        """
        Loads the CSV data into a pandas DataFrame.
        
        :return: DataFrame containing the CSV data.
        """
        try:
            df = pd.read_csv(self.file_path)
            return df
        except FileNotFoundError:
            print(f"Error: The file {self.file_path} was not found.")
            raise
        except pd.errors.EmptyDataError:
            print("Error: The file is empty.")
            raise
        except pd.errors.ParserError:
            print("Error: There was an error parsing the file.")
            raise
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            raise
    
    def filter_data(self, df):
        """
        Filters the DataFrame to include only rows where OBJETO_CONTRATO is 'Bienes' or 'Servicios'.
        
        :param df: DataFrame containing the contracts data.
        :return: Filtered DataFrame.
        """
        try:
            filtered_df = df[df['OBJETO_CONTRATO'] == 'Bienes' | df['OBJETO_CONTRATO'] == 'Servicios']
            return filtered_df
        except KeyError:
            print("Error: The specified column 'OBJETO_CONTRATO' does not exist in the DataFrame.")
            raise
        except Exception as e:
            print(f"An unexpected error occurred while filtering data: {e}")
            raise
    
    def get_parameters(self, df):
        """
        Extracts the 'CODIGO_PROCESO' and 'URL' columns from the filtered DataFrame.
        
        :param df: Filtered DataFrame.
        :return: Tuple containing lists of CODIGO_PROCESO and URLs.
        """
        try:
            codigo_proceso = df['CODIGO_PROCESO'].tolist()
            urls = df['URL'].tolist()
            return codigo_proceso, urls
        except KeyError as e:
            print(f"Error: Missing expected column in the DataFrame: {e}")
            raise
        except Exception as e:
            print(f"An unexpected error occurred while extracting parameters: {e}")
            raise
        