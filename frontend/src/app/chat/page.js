"use client";
import { useState } from "react";
import PageContainer from "@/components/ui/PageContainer";
import ChatInput from "@/components/ui/ChatInput";

export default function ChatPage() {
  const [input, setInput] = useState("");
  const [messages, setMessages] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");
  const [project, setProject] = useState("demo-project");
  const [file, setFile] = useState("main.py");
  const [attachedFiles, setAttachedFiles] = useState([]);

  async function sendMessage(e) {
    e.preventDefault();
    if (!input.trim()) return;
    
    setLoading(true);
    setError("");
    
    try {
      const res = await fetch("/api/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message: input, project, file })
      });
      const data = await res.json();
      
      if (!res.ok) {
        throw new Error(data.message || 'Failed to send message');
      }
      
      setMessages((msgs) => [...msgs, 
        { role: "user", text: input }, 
        { role: "ai", text: data.reply }
      ]);
      setInput("");
    } catch (err) {
      setError(err.message || "Error sending message");
    } finally {
      setLoading(false);
    }
  }

  function handleKeyDown(e) {
    if (e.key === "Enter" && !e.shiftKey) {
      e.preventDefault();
      sendMessage(e);
    }
  }

  return (
    <PageContainer title="Chat" subtitle="Talk with the assistant. Press Enter to send, Shift+Enter for newline.">
      {/* Messages Area - flex-1 to take available space */}
      <div className="flex-1 flex flex-col">
        <div className="max-w-4xl mx-auto w-full flex-1">
          <div 
            className="max-h-[60vh] overflow-y-auto"
            style={{ 
              display: 'flex',
              flexDirection: 'column',
              gap: 'var(--spacing-sm)',
              marginBottom: 'var(--spacing-lg)'
            }}
          >
            {messages.map((msg, idx) => (
              <div 
                key={idx} 
                className={`p-3 rounded-lg border border-[var(--border)] leading-relaxed max-w-[75ch] ${
                  msg.role === "user" ? "bg-[var(--primary)] text-white ml-auto" : "bg-[var(--background-secondary)] text-[var(--foreground)]"
                }`}
              >
                <span className="font-semibold mr-2">{msg.role === "user" ? "You:" : "AI:"}</span>
                {msg.text}
              </div>
            ))}
          </div>

          {/* Error Display */}
          {error && (
            <div 
              className="p-3 bg-red-900/20 border border-red-500/30 rounded-lg text-red-400 text-sm"
              style={{ marginBottom: 'var(--spacing-md)' }}
            >
              {error}
            </div>
          )}
        </div>
      </div>

      {/* Input Form - at bottom of modal */}
      <div className="border-t border-[var(--border)] pt-4">
        <ChatInput
          value={input}
          onChange={(e) => setInput(e.target.value)}
          onKeyDown={handleKeyDown}
          onSubmit={sendMessage}
          placeholder="Ask anything about your project..."
          disabled={loading}
          loading={loading}
          attachedFiles={attachedFiles}
          onFilesChange={setAttachedFiles}
        />
      </div>
    </PageContainer>
  );
}
