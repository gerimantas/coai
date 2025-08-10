"use client";
import React, { useEffect, useState } from "react";

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
      // Simulate fetching project details
      setDetails({
        name: selected,
        description: "Demo project description.",
        created: "2025-08-10",
        status: "active",
      });
      setStatus("active");
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
  const handleMigrate = () => {
    alert(`Migrate project: ${selected}`);
  };

  return (
    <div className="min-h-screen bg-[#0f0f0f] text-white">
      <div className="mt-[2%] mr-[2%] px-6 py-6">
        <h1 className="text-lg font-medium mb-6">Projects</h1>
        <div className="bg-[#1a1a1a] border border-[#2a2a2a] rounded-lg p-6">
          {loading ? (
            <p className="text-sm text-gray-400">Loading projects...</p>
          ) : error ? (
            <p className="text-sm text-red-400">{error}</p>
          ) : projects.length === 0 ? (
            <p className="text-sm text-gray-400">No projects found.</p>
          ) : (
            <ul className="space-y-2">
              {projects.map((name) => (
                <li key={name}>
                  <button
                    className={`w-full text-left px-4 py-2 rounded-lg border border-[#2a2a2a] ${selected === name ? "bg-blue-700" : "bg-[#222]"}`}
                    onClick={() => handleSelect(name)}
                  >
                    {name}
                  </button>
                </li>
              ))}
            </ul>
          )}
          {selected && details && (
            <div className="mt-6 p-4 bg-[#222] rounded-lg border border-[#2a2a2a]">
              <p className="text-sm mb-2">Selected project: <span className="font-bold">{details.name}</span></p>
              <p className="text-xs text-gray-400 mb-2">{details.description}</p>
              <p className="text-xs text-gray-400 mb-2">Created: {details.created}</p>
              <p className="text-xs text-gray-400 mb-2">Status: <span className="font-bold text-green-400">{status}</span></p>
              <div className="flex flex-wrap gap-2 mt-4">
                <button className="bg-blue-700 px-3 py-1 rounded text-xs" onClick={handleOpen}>Open</button>
                <button className="bg-red-700 px-3 py-1 rounded text-xs" onClick={handleDelete}>Delete</button>
                <button className="bg-yellow-700 px-3 py-1 rounded text-xs" onClick={handleEdit}>Edit Config</button>
                <button className="bg-gray-700 px-3 py-1 rounded text-xs" onClick={handleFiles}>Files</button>
                <button className="bg-green-700 px-3 py-1 rounded text-xs" onClick={handleExport}>Export</button>
                <button className="bg-purple-700 px-3 py-1 rounded text-xs" onClick={handleImport}>Import</button>
                <button className="bg-pink-700 px-3 py-1 rounded text-xs" onClick={handleMigrate}>Migrate</button>
              </div>
            </div>
          )}
        </div>
      </div>
    </div>
  );
};

export default ProjectsPage;
