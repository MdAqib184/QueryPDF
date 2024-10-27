// src/components/MessageInput.js
import React, { useState } from 'react';
import { LuSendHorizonal } from "react-icons/lu";

export default function MessageInput({ onSendMessage }) {
    const [input, setInput] = useState('');

    const handleSubmit = (e) => {
        e.preventDefault();
        if (input.trim()) {
            onSendMessage(input);
            setInput('');
        }
    };

    return (
        <div className="px-10 py-5">
            <form onSubmit={handleSubmit} className="flex p-4 border-t border-gray-50 relative">
                <input
                    type="text"
                    placeholder="Send a message..."
                    value={input}
                    onChange={(e) => setInput(e.target.value)}
                    className="flex-1 p-3 pr-10 border rounded-lg bg-gray-100 border-gray-300 focus:border-gray-300 focus:outline-none shadow-md"
                />
                <button 
                    type="submit" 
                    className="absolute right-6 top-1/2 transform -translate-y-1/2"
                >
                    <LuSendHorizonal
                        className={input ? "text-black" : "text-gray-300"} 
                        size={25}
                    />
                </button>
            </form>
        </div>
    );
}
