import PyPDF2
from docx import Document
import textract
import logging

logger = logging.getLogger(__name__)

def process_resume_file(file_path, mime_type):
    try:
        if mime_type == "application/pdf":
            return extract_pdf_text(file_path)
        elif mime_type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
            return extract_docx_text(file_path)
        else:
            raise ValueError("Unsupported file format")
    except Exception as e:
        logger.error(f"Error processing file: {str(e)}")
        raise

def extract_pdf_text(file_path):
    text = ""
    try:
        with open(file_path, "rb") as file:
            reader = PyPDF2.PdfReader(file)
            for page in reader.pages:
                text += page.extract_text() + "\n"
    except Exception as e:
        raise RuntimeError(f"PDF processing error: {str(e)}")
    return text.strip()

def extract_docx_text(file_path):
    try:
        doc = Document(file_path)
        return "\n".join([para.text for para in doc.paragraphs])
    except Exception as e:
        raise RuntimeError(f"DOCX processing error: {str(e)}")