"use client";
import React from 'react';

const AssistantsPage = () => {
  const assistants = [
    {
      id: 'asst_DULbwnhTvSZbrISwNRd7oPvo',
      name: 'Untitled assistant',
      time: '10:02 PM',
      date: 'Last month, Jul 26'
    },
    {
      id: 'asst_1EixGymuukayxIy6eQJwEAjI',
      name: 'copilot',
      time: '7:52 PM',
      date: 'Last month, Jul 21'
    }
  ];

  return (
    <div className="min-h-screen bg-[#0f0f0f] text-white">
      <div className="mt-[2%] mr-[2%] px-6 py-6">
        <h1 className="text-lg font-medium mb-6">Assistants</h1>
        
        <div className="space-y-4">
          {assistants.map((assistant, index) => (
            <div key={assistant.id}>
              {/* Date separator */}
              <div className="text-xs text-gray-400 mb-2 font-medium">
                {assistant.date}
              </div>
              
              {/* Assistant card */}
              <div className="bg-[#1a1a1a] border border-[#2a2a2a] rounded-lg p-4 hover:bg-[#1f1f1f] transition-colors cursor-pointer">
                <div className="flex items-center justify-between">
                  <div className="flex-1">
                    <h3 className="text-sm font-medium text-white mb-1">
                      {assistant.name}
                    </h3>
                    <p className="text-xs text-gray-400 font-mono">
                      {assistant.id}
                    </p>
                  </div>
                  <div className="text-xs text-gray-400">
                    {assistant.time}
                  </div>
                </div>
              </div>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
};

export default AssistantsPage;
