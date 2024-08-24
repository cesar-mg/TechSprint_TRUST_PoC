import os
from PoC.data_mining_module.contract_processing import ContractFilter
from PoC.data_mining_module.web_scrapper_selenium_bot import WebScraperSelenium
from PoC.document_analysis_module_nlp.nlp_entity_extraction import ContractEntityExtractor
from PoC.document_analysis_module_nlp.nlp_entity_extraction_certificado_comprometer import TextDataExtractor
from PoC.document_processing_module.document_processing_tresseract import PDFOCRProcessorTesseract

class ContractProcessor:
    def __init__(self, contract_file, input_pdf, text_file, output_excel):
        """
        Initialize the ContractProcessor class with paths to the required files.
        """
        self.contract_file = contract_file
        self.input_pdf = input_pdf
        self.text_file = text_file
        self.output_excel = output_excel

    def load_and_filter_contracts(self):
        """
        Load the contracts from a CSV file and filter the data.
        """
        contract_filter = ContractFilter(self.contract_file)
        df = contract_filter.load_data()  # Load the contract data into a DataFrame
        self.filtered_df = contract_filter.filter_data(df)  # Filter the DataFrame
        self.contract_filter = contract_filter  # Store the contract filter for later use

    def run_web_scraper(self):
        """
        Run the web scraper using the filtered contract data.
        """
        # Get the necessary parameters for the web scraper
        codigo_proceso, urls = self.contract_filter.get_parameters(self.filtered_df)
        scraper = WebScraperSelenium(urls, codigo_proceso)  # Initialize the web scraper
        scraper.scrape()  # Perform the scraping
        scraper.close()  # Close the scraper

    def process_pdf(self):
        """
        Process the input PDF file using OCR (Optical Character Recognition).
        """
        pdf_processor = PDFOCRProcessorTesseract(self.input_pdf, language='spa')
        pdf_processor.process_pdf()  # Process the PDF to extract text

    def extract_and_save_entities(self):
        """
        Extract entities from the text file and save them to an Excel file.
        """
        extractor = ContractEntityExtractor()
        file_content = self._read_file(self.text_file)  # Read the content of the text file
        df_entities_and_amounts = extractor.extract_entities_and_amounts(file_content)  # Extract entities
        df_entities_and_amounts.to_excel(self.output_excel, index=False)  # Save the results to an Excel file
        print(f"Data has been written to {self.output_excel}")

    def extract_and_insert_data(self):
        """
        Extract specific data from the text file and insert it into the database.
        """
        extractor = TextDataExtractor()
        file_content = self._read_file(self.text_file)  # Read the content of the text file
        amount, person = extractor.extract_amount_and_person(file_content)  # Extract the amount and person
        extractor.insert_data(amount, person)  # Insert the extracted data into the database
        self._print_extracted_data(extractor)  # Print the data from the database
        extractor.close_connection()  # Close the database connection

    def _read_file(self, file_path):
        """
        Private method to read the content of a file.
        """
        try:
            with open(file_path, 'r') as file:
                return file.read()  # Return the content of the file
        except FileNotFoundError as e:
            print(f"Error: {file_path} not found.")
            raise e

    def _print_extracted_data(self, extractor):
        """
        Private method to print the extracted data from the database.
        """
        data = extractor.fetch_all_data()  # Fetch all data from the database
        for row in data:
            print(row)  # Print each row of data

    def run(self):
        """
        Main method to run the entire contract processing workflow.
        """
        self.load_and_filter_contracts()  # Step 1: Load and filter contracts
        self.run_web_scraper()  # Step 2: Run the web scraper
        self.process_pdf()  # Step 3: Process the PDF
        self.extract_and_save_entities()  # Step 4: Extract entities and save to Excel
        self.extract_and_insert_data()  # Step 5: Extract data and insert into the database

if __name__ == "__main__":
    # Define file paths
    contract_file = os.path.join('PoC', 'database', 'bronze', 'Contracts.csv')
    input_pdf = os.path.join('PoC', "database", "bronze", "SENEYDA EULALIA ABREY CUOTA.pdf")
    text_file = os.path.join('PoC', "database", "silver", "extracted_text.txt")
    output_excel = os.path.join("database", "gold", "entities_and_amounts.xlsx")

    # Create an instance of ContractProcessor and run the process
    processor = ContractProcessor(contract_file, input_pdf, text_file, output_excel)
    processor.run()  # Run the contract processing workflow
