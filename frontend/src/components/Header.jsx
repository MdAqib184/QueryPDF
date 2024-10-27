// src/components/Header.js
import React, { useState } from 'react';
import { IoAddCircleOutline } from "react-icons/io5";
import { GrDocument } from "react-icons/gr";

export default function Header({ onFileUpload }) {
    const [fileName, setFileName] = useState(null);

    const handleFileChange = (e) => {
        const file = e.target.files[0];
        if (file) {
            setFileName(file.name);
            onFileUpload(file);
        }
    };

    return (
        <header className="flex items-center justify-between p-4 px-10 bg-white border shadow-lg">
            <div className="flex items-center space-x-2">
                <img src="/htt.png" alt="Logo" className="h-10 w-18" />
            </div>
            <div className="flex items-center space-x-4">
                <div className="flex items-center space-x-2">
                    {fileName ? (
                        <span className="flex items-center text-green-600">
                            <GrDocument size={20} className="mr-1" />
                            {fileName}
                        </span>
                    ) : (
                        <span></span>
                    )}
                </div>
                <input 
                    type="file" 
                    accept="application/pdf" 
                    id="upload" 
                    className="hidden" 
                    onChange={handleFileChange} 
                />
                <button 
                    onClick={() => document.getElementById('upload').click()}
                    className="flex items-center px-4 py-2 text-black border border-black rounded-lg"
                >
                    <IoAddCircleOutline size={20} className="mr-2" />
                    <span className="text-black font-bold">Upload PDF</span>
                </button>
            </div>
        </header>
    );
}
