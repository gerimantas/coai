"use client";

export default function Home() {
  return (
    <div className="min-h-screen bg-[#0f0f0f] text-white">
      <div className="mt-[2%] mr-[2%] px-6 py-6">
        <div className="text-center">
          <h1 className="text-lg font-medium mb-4">Welcome to COAI</h1>
          <p className="text-sm text-gray-400 mb-6">
            Collaborative AI Assistant Interface
          </p>
          
          <div className="bg-[#1a1a1a] border border-[#2a2a2a] rounded-lg p-6">
            <h2 className="text-base font-medium mb-4">Getting Started</h2>
            <p className="text-sm text-gray-400 mb-6">
              Use the navigation menu on the left to access different features:
            </p>
            <div className="grid grid-cols-1 md:grid-cols-2 gap-4 text-left">
              <div>
                <h3 className="text-sm font-medium text-white mb-2">Create</h3>
                <p className="text-xs text-gray-400">
                  Start conversations, generate content, and work with AI assistants
                </p>
              </div>
              <div>
                <h3 className="text-sm font-medium text-white mb-2">Manage</h3>
                <p className="text-xs text-gray-400">
                  Monitor usage, manage API keys, and review system logs
                </p>
              </div>
            </div>
          </div>

          <div className="mt-12">
            <p className="text-gray-500 text-sm">
              COAI v1.0 - Collaborative AI Assistant Interface
            </p>
          </div>
        </div>
      </div>
    </div>
  );
}
