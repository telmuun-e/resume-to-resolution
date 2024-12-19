import docx2txt
from io import BytesIO
from pypdf import PdfReader
import markdown
import pdfkit


class FileHandler:
    @staticmethod
    def extract_text_from_pdf(pdf_file: bytes) -> str:
        reader = PdfReader(BytesIO(pdf_file))
        text = ""
        for page in reader.pages:
            text += page.extract_text()
            # print(page.extract_text(), "\n\n")
        return text
    

    @staticmethod
    def extract_text_from_word(word_file: bytes) -> str:
        return docx2txt.process(BytesIO(word_file))
    

    @staticmethod
    def create_pdf(text: str) -> bytes:
        html = "<meta charset='UTF-8'>" + markdown.markdown(text)
        buffer = pdfkit.from_string(html)
        return buffer