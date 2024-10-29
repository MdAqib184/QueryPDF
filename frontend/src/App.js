// src/App.js
import React, { useState } from 'react';
import Header from './components/Header';
import ChatWindow from './components/ChatWindow';
import MessageInput from './components/MessageInput';

function App() {
    const [messages, setMessages] = useState([]);
    const [uploadedFileName, setUploadedFileName] = useState(null); // Track the uploaded file name

    // API base URL for FastAPI backend
    const API_BASE_URL = "http://127.0.0.1:8000";

    const handleFileUpload = async (file) => {
        try {
            const formData = new FormData();
            formData.append("file", file);

            const response = await fetch(`${API_BASE_URL}/upload/`, {
                method: "POST",
                body: formData,
            });

            if (!response.ok) {
                console.error("Response status:", response.status, response.statusText);
                throw new Error("File upload failed");
            }

            const data = await response.json();
            console.log("File uploaded successfully:", data.message);
            alert("File uploaded successfully!");
            setUploadedFileName(file.name); // Set the uploaded file name for future questions
        } catch (error) {
            console.error("Error uploading file:", error.message);
            alert("Error uploading file. Please try again.");
        }
    };

    const handleSendMessage = async (text) => {
        try {
            const answer = await fetchAnswer(text);
            setMessages(prevMessages => [
                ...prevMessages,
                { text, isUser: true },
                { text: answer, isUser: false }
            ]);
        } catch (error) {
            console.error("Error getting answer:", error);
            alert("Error retrieving answer. Please try again.");
        }
    };

    const fetchAnswer = async (question) => {
        if (!uploadedFileName) {
            alert("Please upload a PDF file before asking a question.");
            return "No file uploaded.";
        }

        try {
            const response = await fetch(`${API_BASE_URL}/ask/`, {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({
                    question, // Use the actual question from user input
                    filename: uploadedFileName // Use the uploaded file name
                })
            });

            if (!response.ok) {
                console.error("Response status:", response.status, response.statusText);
                throw new Error("Error fetching answer");
            }

            const data = await response.json();
            return data.answer;
        } catch (error) {
            console.error("Error in fetchAnswer:", error.message);
            return "Sorry, there was an error processing your question.";
        }
    };

    return (
        <div className="flex flex-col h-screen">
            <Header onFileUpload={handleFileUpload} />
            <ChatWindow messages={messages} />
            <MessageInput onSendMessage={handleSendMessage} />
        </div>
    );
}

export default App;
