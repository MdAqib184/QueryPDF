import fitz  # PyMuPDF

async def extract_text_from_pdf(filename):
    text = ""
    with fitz.open(f"uploads/{filename}") as pdf:
        for page in pdf:
            text += page.get_text()
    print("Extracted text:", text)
    return text
