import React from 'react';
import ChatBubble from './ChatBubble';

export default function ChatWindow({ messages }) {
    return (
        <div className="flex-1 overflow-y-auto p-6 bg-gray-50">
            {messages.map((msg, idx) => (
                <ChatBubble key={idx} message={msg.text} isUser={msg.isUser} />
            ))}
        </div>
    );
}
