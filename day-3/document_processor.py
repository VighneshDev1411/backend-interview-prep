import PyPDF2
import pandas as pd
from pathlib import Path

class DocumentProcessor:
    @staticmethod
    def extract_text_from_pdf(file_path: str) -> str:
        """Extract text from PDF file"""
        try:
            text = ""

            # Open PDF file
            with open(file_path, 'rb') as file:
                """
                Open file in read-binary mode ('rb')
                PDF files are binary, not text 
                """
                # Create PDF reader object 
                pdf_reader = PyPDF2.PdfReader(file)
                # Create PdfReader object to read the PDF

                # Get number of pages
                num_pages = len(pdf_reader.pages)

                for page_num in range(num_pages):
                    page = pdf_reader.pages[page_num]
                    text += page.extract_text()
                
                """
                Loop through each page
                Extract text from page
                concatenate all text together
                """
            return text.strip() # Remove leading / trailing whitespace , return extracted text
        
        
        except Exception as e:

            raise Exception(f"Error extracting PDF textL {str(e)}")
        
    @staticmethod
    def parse_csv(file_path: str) -> dict:
        """Parse CSV file and return data"""
        try: 
            # Read CSV File
            df = pd.read_csv(file_path) # df = DataFrame(pandas data structure)
            # Reads csv into table format

            # Convert to dictionary format
            data = {
                "rows": len(df),
                "columns": df.columns.tolist(),
                "data": df.to_dict(orient="records")
                # Convert dataframe to list of dictionaries 
                # Each row becomes a dictionary 
            }
            
            return data
        
        except Exception as e:
            raise Exception(f"Error parsing CSV: {str(e)}")