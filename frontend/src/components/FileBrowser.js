"use client";
import React, { useEffect, useState } from "react";



function TreeNode({ node, onFileClick, level = 0, selectedPath }) {
  const [open, setOpen] = useState(false);
  const [children, setChildren] = useState(null);
  const [loading, setLoading] = useState(false);

  if (!node) return null;
  if (node.type === "dir") {
    const handleExpand = () => {
      setOpen((o) => !o);
      if (!children && !loading) {
        setLoading(true);
        fetch(`http://localhost:5000/api/files/list?path=${encodeURIComponent(node.path || node.name || "")}`)
          .then((res) => res.json())
          .then((data) => setChildren(data.children || []))
          .finally(() => setLoading(false));
      }
    };
    return (
      <div style={{ marginLeft: level * 16 }}>
        <span
          style={{ cursor: "pointer", fontWeight: "bold" }}
          onClick={handleExpand}
        >
          {open ? "📂" : "📁"} {node.name}
        </span>
        {open && (
          <div>
            {loading && <div>Įkeliama...</div>}
            {children && children.map((child) => (
              <TreeNode key={child.name + (child.path || "") } node={{...child, path: (child.path || ((node.path ? node.path + "/" : "") + child.name))}} onFileClick={onFileClick} level={level + 1} selectedPath={selectedPath} />
            ))}
          </div>
        )}
      </div>
    );
  }
  const isSelected = selectedPath && selectedPath === node.path;
  return (
    <div style={{ marginLeft: level * 16 }}>
      <button
        className={`text-left w-full px-1 py-1.5 rounded ${isSelected ? 'bg-[var(--background-tertiary)] text-[var(--foreground)]' : 'text-blue-400 hover:text-blue-300'}`}
        style={{ background: 'none', border: 'none', cursor: 'pointer' }}
        onClick={() => onFileClick(node.path)}
      >
        📄 {node.name}
      </button>
    </div>
  );
}

export default function FileBrowser() {
  const [tree, setTree] = useState(null);
  const [selectedFile, setSelectedFile] = useState("");
  const [fileContent, setFileContent] = useState("");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  useEffect(() => {
    fetch("http://localhost:5000/api/files/list")
      .then((res) => res.json())
      .then((data) => setTree(data.tree))
      .catch(() => setError("Nepavyko gauti failų medžio"));
  }, []);

  const MAX_SIZE = 100 * 1024; // 100 KB
  const handleFileClick = (filename) => {
    setSelectedFile(filename);
    setLoading(true);
    setError("");
    // Normalizuojame kelią: pakeičiame \ į / ir pašaliname 'coai/' pradžioje
    let normalized = filename.replace(/\\/g, "/");
    if (normalized.startsWith("coai/")) {
      normalized = normalized.slice(5);
    }
    fetch(`http://localhost:5000/api/files/${encodeURIComponent(normalized)}`)
      .then((res) => {
        if (!res.ok) throw new Error("Failo skaitymo klaida");
        return res.json();
      })
      .then((data) => {
        if (data.content && data.content.length > MAX_SIZE) {
          setFileContent(data.content.slice(0, MAX_SIZE) + "\n--- Failas per didelis, rodomi tik pirmi 100 KB ---");
        } else {
          setFileContent(data.content);
        }
      })
      .catch(() => setError("Nepavyko perskaityti failo"))
      .finally(() => setLoading(false));
  };

  return (
    <div className="grid grid-cols-1 md:grid-cols-12 gap-6">
      <div className="md:col-span-4">
        <h2 className="text-sm font-semibold text-[var(--foreground)] mb-2">Failų medis</h2>
        <div className="max-h-[60vh] overflow-y-auto border border-[var(--border)] rounded-lg p-2 bg-[var(--background-secondary)]">
          {tree ? (
            <TreeNode node={tree} onFileClick={handleFileClick} selectedPath={selectedFile} />
          ) : (
            <div>Įkeliama...</div>
          )}
        </div>
        {error && <div className="text-red-400 mt-2 text-sm">{error}</div>}
      </div>
      <div className="md:col-span-8">
        <div className="flex items-center justify-between mb-2">
          <h2 className="text-sm font-semibold text-[var(--foreground)]">Failo turinys</h2>
          {selectedFile && (
            <span className="text-xs text-[var(--foreground-muted)] truncate max-w-[60%]">{selectedFile}</span>
          )}
        </div>
        {/* Controls */}
        <div className="flex items-center gap-2 mb-2">
          <button className="px-2 py-1 text-xs rounded bg-gray-700 hover:bg-gray-600 text-white" onClick={() => {
            const pre = document.getElementById('file-content-pre');
            if (pre) pre.classList.toggle('whitespace-pre-wrap');
          }}>Wrap</button>
          <button className="px-2 py-1 text-xs rounded bg-gray-700 hover:bg-gray-600 text-white" onClick={() => {
            navigator.clipboard.writeText(fileContent || "");
          }}>Copy</button>
        </div>
        {loading ? (
          <div>Įkeliama...</div>
        ) : error ? (
          <div className="text-red-400">{error}</div>
        ) : selectedFile ? (
          fileContent && fileContent.trim() !== "" ? (
            <pre id="file-content-pre" className="bg-[var(--background-secondary)] text-[var(--foreground)] border border-[var(--border)] rounded-lg p-4 min-h-[200px] max-h-[60vh] overflow-auto font-mono text-sm whitespace-pre-wrap">
              {fileContent}
            </pre>
          ) : (
            <div className="text-[var(--foreground-muted)]">(Tuščias failas)</div>
          )
        ) : (
          <div className="text-[var(--foreground-muted)]">(Nepasirinktas failas)</div>
        )}
      </div>
    </div>
  );
}
