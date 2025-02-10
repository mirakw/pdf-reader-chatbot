import fitz  # PyMuPDF

def extract_text_from_pdf(pdf_file):
    """
    Extracts plain text from the uploaded PDF file using PyMuPDF.

    Args:
        pdf_file: The uploaded PDF file from the Streamlit uploader.

    Returns:
        str: Extracted plain text from the entire PDF.
    """
    doc = fitz.open(stream=pdf_file.read(), filetype="pdf")
    text = ""

    for page_num in range(len(doc)):
        page = doc[page_num]
        text += page.get_text("text")

    return text.strip()
