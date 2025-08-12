"use client";
import React, { useEffect, useState } from "react";
import PageContainer from "@/components/ui/PageContainer";

const ProjectsPage = () => {
  const [projects, setProjects] = useState([]);
  const [selected, setSelected] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [details, setDetails] = useState(null);
  const [status, setStatus] = useState(null);

  useEffect(() => {
    fetch("/api/projects")
      .then((res) => res.json())
      .then((data) => {
        setProjects(data.projects || []);
        setLoading(false);
      })
      .catch((err) => {
        setError("Failed to load projects");
        setLoading(false);
      });
  }, []);

  useEffect(() => {
    if (selected) {
      fetch(`/api/project-details?name=${encodeURIComponent(selected)}`)
        .then((res) => res.json())
        .then((data) => {
          setDetails({
            name: selected,
            description: data.config?.description || "No description.",
            created: data.config?.created || "Unknown",
            status: data.config?.status || "unknown",
            rules: data.rules || "No rules.",
            plan: data.plan || "No plan.",
          });
          setStatus(data.config?.status || "unknown");
        })
        .catch(() => {
          setDetails({
            name: selected,
            description: "Failed to load details.",
            created: "Unknown",
            status: "unknown",
            rules: "",
            plan: "",
          });
          setStatus("unknown");
        });
    } else {
      setDetails(null);
      setStatus(null);
    }
  }, [selected]);

  const handleSelect = (name) => {
    setSelected(name);
  };

  const handleOpen = () => {
    alert(`Open project: ${selected}`);
  };
  const handleDelete = () => {
    alert(`Delete project: ${selected}`);
  };
  const handleEdit = () => {
    alert(`Edit config for: ${selected}`);
  };
  const handleFiles = () => {
    alert(`Show files for: ${selected}`);
  };
  const handleExport = () => {
    alert(`Export project: ${selected}`);
  };
  const handleImport = () => {
    alert(`Import project`);
  };
  const handleMigrate = async () => {
    const src = prompt("Enter source directory to migrate:");
    if (!src || !selected) return;
    try {
      const res = await fetch("/api/migrate_project", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ src, name: selected }),
      });
      const data = await res.json();
      if (data.success) {
        alert(`Migration successful! New project at: ${data.dest}`);
      } else {
        alert(`Migration failed: ${data.error}`);
      }
    } catch (e) {
      alert(`Migration error: ${e.message}`);
    }
  };

  return (
  <PageContainer title="Projects" subtitle="Select a project to view details and actions.">
      {loading ? (
        <p className="text-sm text-gray-400">Loading projects...</p>
      ) : error ? (
        <p className="text-sm text-red-400">{error}</p>
      ) : projects.length === 0 ? (
        <p className="text-sm text-gray-400">No projects found.</p>
      ) : (
        <ul className="space-y-2 max-h-[50vh] overflow-y-auto pr-1">
          {projects.map((name) => (
            <li key={name}>
              <button
                className={`w-full text-left px-4 py-2 rounded-lg border border-[var(--border)] ${selected === name ? "bg-[var(--background-tertiary)]" : "bg-[var(--background-secondary)]"}`}
                onClick={() => handleSelect(name)}
              >
                {name}
              </button>
            </li>
          ))}
        </ul>
      )}
      {selected && details && (
        <>
          <div className="mt-6 p-4 rounded-lg border border-[var(--border)] bg-[var(--background-secondary)]">
            <p className="text-sm mb-2">Selected project: <span className="font-medium">{details.name}</span></p>
            <p className="text-xs text-[var(--foreground-muted)] mb-2">{details.description}</p>
            <p className="text-xs text-[var(--foreground-muted)] mb-2">Created: {details.created}</p>
            <p className="text-xs text-[var(--foreground-muted)] mb-2">Status: <span className="px-2 py-0.5 rounded border border-green-700 text-green-200 bg-green-800/30">{status}</span></p>
          </div>
          <div className="flex flex-wrap gap-2 mt-4 p-4 rounded-lg border border-[var(--border)] bg-[var(--background-secondary)]">
            <button className="px-3 py-1 rounded border border-blue-500 text-blue-400 hover:bg-blue-500/10 text-xs" onClick={handleOpen}>Open</button>
            <button className="px-3 py-1 rounded text-xs bg-red-700 hover:bg-red-800" onClick={handleDelete}>Delete</button>
            <button className="px-3 py-1 rounded text-xs bg-gray-700 hover:bg-gray-600" onClick={handleEdit}>Edit Config</button>
            <button className="px-3 py-1 rounded text-xs bg-gray-700 hover:bg-gray-600" onClick={handleFiles}>Files</button>
            <button className="px-3 py-1 rounded text-xs bg-teal-700 hover:bg-teal-800" onClick={handleExport}>Export</button>
            <button className="px-3 py-1 rounded text-xs bg-teal-700 hover:bg-teal-800" onClick={handleImport}>Import</button>
            <button className="px-3 py-1 rounded text-xs bg-purple-700 hover:bg-purple-800" onClick={handleMigrate}>Migrate</button>
          </div>
        </>
      )}
    </PageContainer>
  );
};

export default ProjectsPage;
