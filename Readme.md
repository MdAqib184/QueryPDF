# QueryPDF

QueryPDF is a full-stack application that enables users to upload PDF documents and ask questions based on the content of these documents. It utilizes a FastAPI backend for handling PDF uploads and question-answering capabilities, while the frontend is built with React and deployed on Vercel. The backend leverages LangChain and LlamaIndex to handle natural language processing.

## Table of Contents
- [Features](#features)
- [Project Structure](#project-structure)
- [Setup Instructions](#setup-instructions)
  - [Backend Setup (FastAPI + LangChain + LlamaIndex)](#backend-setup-fastapi--langchain--llamaindex)
  - [Frontend Setup (React)](#frontend-setup-react)
- [Usage](#usage)
- [Technologies Used](#technologies-used)

## Features
- Upload a PDF document to the backend for processing.
- Ask questions based on the content of the uploaded document.
- Receive answers by analyzing the document’s text.

## Project Structure
assn │ ├───backend │ ├── main.py # Backend FastAPI server │ ├── requirements.txt # Backend dependencies │ └── ... # Other backend files │ └───frontend ├── src │ ├── App.js # Main React component │ └── ... # Other frontend files └── package.json # Frontend dependencies


## Setup Instructions

### Prerequisites
- Python 3.8+
- Node.js and npm
- Vercel account for frontend deployment
- Render account for backend deployment

### Backend Setup (FastAPI + LangChain + LlamaIndex)
1. Open backend directory: `cd assn/backend`
2. Create virtual environment: `python -m venv venv`
3. Activate virtual environment:
   - On Windows: `.\venv\Scripts\activate`
   - On macOS/Linux: `source venv/bin/activate`
4. Install dependencies: `pip install -r requirements.txt`
5. Run backend server: `uvicorn main:app --host 0.0.0.0 --port 10000`
6. Deployment: Deploy the backend on Render or your preferred cloud provider.

### Frontend Setup (React)
1. Open frontend directory: `cd assn/frontend`
2. Install dependencies: `npm install`
3. Update API base URL:
   - Open `src/App.js`.
   - Update the `API_BASE_URL` variable with your deployed backend URL: 
     ```javascript
     const API_BASE_URL = "https://your-backend-url.onrender.com";
     ```
4. Run frontend locally: `npm start`
5. Deployment: Deploy the frontend on Vercel.

## Usage
1. **Upload a PDF File:** Go to the deployed frontend URL and upload a PDF file.
2. **Ask a Question:** After the PDF is uploaded, enter a question in the input box related to the document’s content.
3. **Receive an Answer:** The backend processes the question and provides a response based on the document's content.

## Technologies Used
- **Frontend:** React, Vercel (deployment)
- **Backend:** FastAPI, Render (deployment), LangChain, LlamaIndex, PyMuPDF.
