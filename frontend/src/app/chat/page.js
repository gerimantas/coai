"use client";
import { useState } from "react";

export default function ChatPage() {
  const [input, setInput] = useState("");
  const [messages, setMessages] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");
  const [project, setProject] = useState("demo-project");
  const [file, setFile] = useState("main.py");

  async function sendMessage(e) {
    e.preventDefault();
    setLoading(true);
    setError("");
    try {
      const res = await fetch("http://localhost:5000/api/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message: input, project, file })
      });
      const data = await res.json();
      setMessages((msgs) => [...msgs, { role: "user", text: input }, { role: "ai", text: data.reply }]);
      setInput("");
    } catch (err) {
      setError("Klaida siunčiant žinutę");
    } finally {
      setLoading(false);
    }
  }

  function handleKeyDown(e) {
    if (e.key === "Enter" && !e.shiftKey) {
      sendMessage(e);
    }
  }

  return (
    <div className="min-h-screen flex items-center justify-center py-8 px-8 sm:px-12 lg:px-16" style={{backgroundColor: 'var(--background)'}}>
      <div className="w-full shadow-2xl p-6 flex flex-col modal-container" style={{minHeight: '80vh', maxWidth: '600px'}}>
        <h1 className="text-3xl font-extrabold mb-6 text-center tracking-tight" style={{color: 'var(--foreground)'}}>Chat (MVP)</h1>
        
        {/* Controls */}
        <div className="flex flex-col sm:flex-row gap-4 mb-6">
          <select 
            value={project} 
            onChange={e => setProject(e.target.value)} 
            className="select-default"
          >
            <option value="demo-project">demo-project</option>
            <option value="kitas-projektas">kitas-projektas</option>
          </select>
          <select 
            value={file} 
            onChange={e => setFile(e.target.value)} 
            className="select-default"
          >
            <option value="main.py">main.py</option>
            <option value="app.js">app.js</option>
          </select>
        </div>

        {/* Messages Area */}
        <div className="flex-1 flex flex-col space-y-4 p-6 min-h-[300px] max-h-[400px] overflow-y-auto mb-6 messages-container">
          {messages.length === 0 && <div className="text-center" style={{color: 'var(--foreground-muted)'}}>Žinučių dar nėra.</div>}
          {messages.map((msg, i) => (
            <div key={i} className={msg.role === "user" ? "flex justify-end" : "flex justify-start"}>
              <div className={`px-5 py-3 max-w-[70%] shadow ${msg.role === "user" ? "message-user" : "message-ai"}`}>
                <span className="block text-xs mb-1 opacity-70">{msg.role === "user" ? "Jūs" : "AI"}</span>
                {msg.text}
              </div>
            </div>
          ))}
        </div>

        {/* Input Form */}
        <form onSubmit={sendMessage} className="flex flex-col gap-4">
          {loading && <div className="text-center animate-pulse" style={{color: 'var(--primary)'}}>Siunčiama...</div>}
          {error && <div className="text-red-500 text-center">{error}</div>}
          <div className="flex gap-3">
            <input
              className="flex-1 input-default text-base"
              value={input}
              onChange={e => setInput(e.target.value)}
              onKeyDown={handleKeyDown}
              placeholder="Įveskite žinutę..."
              disabled={loading}
              autoFocus
            />
            <button 
              type="submit" 
              className="btn-primary" 
              style={{minWidth: '100px'}} 
              disabled={loading || !input}
            >
              Siųsti
            </button>
          </div>
        </form>
      </div>
    </div>
  );
}
