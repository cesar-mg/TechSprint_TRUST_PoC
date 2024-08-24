import os
import shutil
import keras_ocr
import pdf2image
import traceback
import numpy as np
class PDFOCRProcessor:
    def __init__(self, pdf_path, output_text_file='extracted_text.txt'):
        self.pdf_path = pdf_path
        self.output_text_file = output_text_file
        self.pipeline = keras_ocr.pipeline.Pipeline()
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
            raise RuntimeError(f"Error conterting the images: {str(e)}")

   

    def extract_text_from_images(self, images):
        """Perform OCR on each image to extract text."""
        extracted_text = []
        for image in images:
            image = np.array(image)
            print(type(image))
            prediction_groups = self.pipeline.recognize([image])
            page_text = " ".join([prediction[0] for prediction in prediction_groups[0]])
            extracted_text.append(page_text)
        return extracted_text


    def save_text_to_file(self, text):
        """Save extracted text to a file."""
        try:
            with open(self.output_text_file, 'w') as f:
                for page_num, page_text in enumerate(text, start=1):
                    f.write(f'--- Page {page_num} ---\n{page_text}\n\n')
        except Exception as e:
            raise IOError(f"Error saving the text to the files: {str(e)}")

    def clean_up(self):
        """Clean up temporary images."""
        try:
            shutil.rmtree(self.output_dir)
        except Exception as e:
            raise IOError(f"Error removing the temporary images: {str(e)}")

    def process_pdf(self):
        """Main method to process the PDF and extract text."""
        try:
            images = self.convert_pdf_to_images()
            extracted_text = self.extract_text_from_images(images)
            self.save_text_to_file(extracted_text)
            self.clean_up()
            print(f"Extraction completed. Text saved in '{self.output_text_file}'.")
        except Exception as e:
            print(f"An error raised during the processing: {str(e)}")
            traceback.print_exc() 


# Uso de la clase
if __name__ == "__main__":
    pdf_processor = PDFOCRProcessor('downloads\Convocatoria General.pdf')
    pdf_processor.process_pdf()
