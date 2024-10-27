import React from 'react';

export default function ChatBubble({ message, isUser }) {
    return (
        <div className="flex mb-4">
            <div
                className={`p-4 max-w-lg rounded-lg shadow-md ${isUser ? 'bg-blue-100 text-gray-900' : 'bg-green-100 text-gray-900'}`}
                style={{ alignSelf: 'flex-start' }}
            >
                <p className="font-medium">{message}</p>
            </div>
        </div>
    );
}
