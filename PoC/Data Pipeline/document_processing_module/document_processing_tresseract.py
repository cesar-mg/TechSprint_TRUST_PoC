import pytesseract
from PIL import Image
import pdf2image
import os
import shutil

class PDFOCRProcessorTesseract:
    def __init__(self, pdf_path, output_folder, language='spa'):
        self.pdf_path = pdf_path
        self.language = language
        self.output_dir = 'temp_images'

        # Extract the PDF name (without extension) and create the output folder path
        pdf_name = os.path.splitext(os.path.basename(pdf_path))[0]
        self.output_text_file = os.path.join(output_folder, f"{pdf_name}.txt")
        
        if not os.path.exists(self.pdf_path):
            raise FileNotFoundError(f"The file {self.pdf_path} does not exist.")
        
        os.makedirs(self.output_dir, exist_ok=True)
        os.makedirs(output_folder, exist_ok=True)

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


def process_all_pdfs_in_folder(root_folder='PoC/Data Pipeline/database/bronze', output_folder='PoC/Data Pipeline/database/silver'):
    """Process all PDF files in each subfolder of the specified root folder."""
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    for subdir, _, files in os.walk(root_folder):
        for file in files:
            if file.endswith('.pdf'):
                pdf_path = os.path.join(subdir, file)
                
                # Maintain the original folder structure within the silver folder
                relative_folder = os.path.relpath(subdir, root_folder)
                output_subdir = os.path.join(output_folder, relative_folder)
                
                if not os.path.exists(output_subdir):
                    os.makedirs(output_subdir)

                # Output text file has the same name as the PDF file, but with a .txt extension
                output_text_file = os.path.join(output_subdir, f"{os.path.splitext(file)[0]}.txt")

                print(f"Processing {pdf_path}...")
                processor = PDFOCRProcessorTesseract(pdf_path, output_subdir)
                processor.process_pdf()




process_all_pdfs_in_folder(root_folder='PoC/Data Pipeline/database/bronze', output_folder='PoC/Data Pipeline/database/silver')
