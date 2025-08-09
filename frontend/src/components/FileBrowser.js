"use client";
import React, { useEffect, useState } from "react";



function TreeNode({ node, onFileClick, level = 0 }) {
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
              <TreeNode key={child.name + (child.path || "") } node={{...child, path: (child.path || ((node.path ? node.path + "/" : "") + child.name))}} onFileClick={onFileClick} level={level + 1} />
            ))}
          </div>
        )}
      </div>
    );
  }
  return (
    <div style={{ marginLeft: level * 16 }}>
      <button
        style={{ background: "none", border: "none", color: "#0070f3", cursor: "pointer" }}
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

  const handleFileClick = (filename) => {
    setSelectedFile(filename);
    setLoading(true);
    setError("");
    fetch(`http://localhost:5000/api/files/${encodeURIComponent(filename)}`)
      .then((res) => {
        if (!res.ok) throw new Error("Failo skaitymo klaida");
        return res.json();
      })
      .then((data) => setFileContent(data.content))
      .catch(() => setError("Nepavyko perskaityti failo"))
      .finally(() => setLoading(false));
  };

  return (
    <div style={{ display: "flex", gap: "2rem" }}>
      <div style={{ minWidth: 300 }}>
        <h2>Failų medis</h2>
        <div style={{ maxHeight: 400, overflowY: "auto", border: "1px solid #ccc", padding: 8 }}>
          {tree ? (
            <TreeNode node={tree} onFileClick={handleFileClick} />
          ) : (
            <div>Įkeliama...</div>
          )}
        </div>
        {error && <div style={{ color: "red" }}>{error}</div>}
      </div>
      <div style={{ flex: 1 }}>
        <h2>Failo turinys</h2>
        {loading ? (
          <div>Įkeliama...</div>
        ) : (
          <pre style={{ background: "#222", color: "#eee", padding: 16, minHeight: 300 }}>
            {fileContent || (selectedFile ? "(Tuščias failas)" : "Pasirinkite failą iš medžio")}
          </pre>
        )}
      </div>
    </div>
  );
}
