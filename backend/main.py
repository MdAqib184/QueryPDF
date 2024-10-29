import os
from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

# Ensure 'uploads' directory exists
os.makedirs("uploads", exist_ok=True)

# Allow CORS for frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Remove trailing slash
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Question(BaseModel):
    question: str

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
        
        return {"message": f"File '{file.filename}' uploaded successfully!"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"File upload failed: {str(e)}")

@app.post("/ask/")
async def ask_question(question: Question):
    # Mock answer - replace this with your NLP logic
    answer = f"This is a mock answer to the question: '{question.question}'"
    return {"answer": answer}
