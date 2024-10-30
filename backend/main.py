import os
import tempfile
import logging
from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import fitz  # PyMuPDF
from collections import defaultdict

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

# Ensure 'uploads' directory exists
os.makedirs("uploads", exist_ok=True)

# Allow CORS for frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://query-pdf-rouge.vercel.app/"  # Vercel deployed frontend URL
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Store extracted text in memory (for demonstration purposes)
pdf_texts = defaultdict(str)

class Question(BaseModel):
    question: str
    filename: str

@app.get("/")
async def root():
    return {"message": "Hello, FastAPI is up and running!"}

@app.post("/upload/")
async def upload_pdf(file: UploadFile = File(...)):
    if not file.filename.endswith('.pdf'):
        raise HTTPException(status_code=400, detail="Invalid file type. Only PDF files are allowed.")

    try:
        # Use a temporary file to store the uploaded PDF
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
            tmp_file.write(await file.read())
            tmp_filename = tmp_file.name

        # Extract text from PDF and store it in memory
        extracted_text = await extract_text_from_pdf(tmp_filename)
        pdf_texts[file.filename] = extracted_text  # Store extracted text

        logger.info(f"File '{file.filename}' uploaded and text extracted successfully.")
        return {"message": f"File '{file.filename}' uploaded successfully!", "extracted_text": extracted_text}
    except Exception as e:
        logger.error(f"Error uploading file: {str(e)}")
        raise HTTPException(status_code=500, detail=f"File upload failed: {str(e)}")

@app.post("/ask/")
async def ask_question(question: Question):
    # Retrieve the extracted text for the specific PDF
    pdf_content = pdf_texts.get(question.filename)
    if not pdf_content:
        raise HTTPException(status_code=404, detail="PDF not found. Please upload it first.")

    # Simple keyword-based answering logic
    if question.question.lower() in pdf_content.lower():
        answer = f"Yes, the document contains information related to '{question.question}'."
    else:
        answer = f"Sorry, I couldn't find information related to '{question.question}' in the document."

    return {"answer": answer}

async def extract_text_from_pdf(filename):
    text = ""
    with fitz.open(filename) as pdf:
        for page in pdf:
            text += page.get_text()
    return text

# Run the application with: uvicorn main:app --host 0.0.0.0 --port 10000
