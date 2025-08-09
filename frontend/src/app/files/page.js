"use client";
import React from 'react';
import FileBrowser from "../../components/FileBrowser";

const FilesPage = () => {
  return (
    <div className="min-h-screen bg-[#0f0f0f] text-white">
      <div className="mt-[2%] mr-[2%] px-6 py-6">
        <h1 className="text-lg font-medium mb-6">Files</h1>
        <FileBrowser />
      </div>
    </div>
  );
};

export default FilesPage;
