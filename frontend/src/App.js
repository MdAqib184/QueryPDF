// src/App.js
import React, { useState } from 'react';
import Header from './components/Header';
import ChatWindow from './components/ChatWindow';
import MessageInput from './components/MessageInput';

function App() {
    const [messages, setMessages] = useState([]);

    const handleFileUpload = (file) => {
        // Here, replace with API call to upload file and store its metadata
        console.log("File uploaded:", file);
    };

    const handleSendMessage = async (text) => {
        setMessages([...messages, { text, isUser: true }]);

        // Mock API call to get the answer based on the text input
        const answer = await fetchAnswer(text);
        setMessages([...messages, { text, isUser: true }, { text: answer, isUser: false }]);
    };

    const fetchAnswer = async (question) => {
        // Replace with API call to your FastAPI backend
        return `This is a mock answer to the question: "${question}"`;
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
