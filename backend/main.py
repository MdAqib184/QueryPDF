import os
from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import fitz  # PyMuPDF
from collections import defaultdict

app = FastAPI()

# Ensure 'uploads' directory exists
os.makedirs("uploads", exist_ok=True)

# Allow CORS for frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "https://query-pdf-rouge.vercel.app/"
        ],  # Adjust this if your frontend runs elsewhere
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
    try:
        # Process and save the uploaded PDF file
        file_content = await file.read()
        with open(f"uploads/{file.filename}", "wb") as f:
            f.write(file_content)

        # Extract text from PDF and store it in memory
        extracted_text = await extract_text_from_pdf(file.filename)
        pdf_texts[file.filename] = extracted_text  # Store extracted text

        return {"message": f"File '{file.filename}' uploaded successfully!", "extracted_text": extracted_text}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"File upload failed: {str(e)}")

@app.post("/ask/")
async def ask_question(question: Question):
    # Retrieve the extracted text for the specific PDF
    pdf_content = pdf_texts.get(question.filename)
    if not pdf_content:
        raise HTTPException(status_code=404, detail="PDF not found. Please upload it first.")

    # Simple keyword-based answering logic (this can be replaced with a more sophisticated NLP model)
    if question.question.lower() in pdf_content.lower():
        answer = f"Yes, the document contains information related to '{question.question}'."
    else:
        answer = f"Sorry, I couldn't find information related to '{question.question}' in the document."

    return {"answer": answer}

async def extract_text_from_pdf(filename):
    text = ""
    with fitz.open(f"uploads/{filename}") as pdf:
        for page in pdf:
            text += page.get_text()
    return text
