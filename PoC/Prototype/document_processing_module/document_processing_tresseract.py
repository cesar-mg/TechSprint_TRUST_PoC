import pytesseract
from PIL import Image
import pdf2image
import os
import traceback
import shutil

class PDFOCRProcessorTesseract:
    def __init__(self, pdf_path, output_text_file='PoC\database\silver\extracted_text.txt', language='spa'):
        self.pdf_path = pdf_path
        self.output_text_file = output_text_file
        self.language = language
        self.output_dir = 'temp_images'
        
        if not os.path.exists(self.pdf_path):
            raise FileNotFoundError(f"The file {self.pdf_path} does not exist.")
        
        os.makedirs(self.output_dir, exist_ok=True)

    def convert_pdf_to_images(self):
        """Convert PDF pages to images."""
        try:
            images = pdf2image.convert_from_path(self.pdf_path)
            for i, image in enumerate(images):
                image_path = f'{self.output_dir}/page_{i+1}.png'
                image.save(image_path, 'PNG')
            return images
        except Exception as e:
            raise RuntimeError(f"Error converting PDF to images: {str(e)}")

    def extract_text_from_images(self, images):
        """Perform OCR on each image to extract text."""
        extracted_text = []
        for image in images:
            text = pytesseract.image_to_string(image, lang=self.language)
            extracted_text.append(text)
        return extracted_text

    def save_text_to_file(self, text):
        """Save extracted text to a file."""
        try:
            with open(self.output_text_file, 'w') as f:
                for page_num, page_text in enumerate(text, start=1):
                    f.write(f'--- Page {page_num} ---\n{page_text}\n\n')
        except Exception as e:
            raise IOError(f"Error saving the text in the file: {str(e)}")

    def clean_up(self):
        """Clean up temporary images."""
        try:
            shutil.rmtree(self.output_dir)
        except Exception as e:
            raise IOError(f"Error removing temporary images: {str(e)}")

    def process_pdf(self):
        """Main method to process the PDF and extract text."""
        try:
            images = self.convert_pdf_to_images()

            extracted_text = self.extract_text_from_images(images)
            self.save_text_to_file(extracted_text)
            self.clean_up()
            print(f"Extraction completed. Text saved in: '{self.output_text_file}'.")
        except Exception as e:
            print(f"Error during the PDF processing: {str(e)}")
