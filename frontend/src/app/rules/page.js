"use client";
import React, { useEffect, useState } from "react";

const RULES_API = "/api/agent_rules";

const RulesEditor = () => {
  const [rules, setRules] = useState("");
  const [loading, setLoading] = useState(true);
  const [saving, setSaving] = useState(false);
  const [error, setError] = useState(null);
  const [success, setSuccess] = useState(false);

  useEffect(() => {
    fetch(RULES_API)
      .then((res) => res.json())
      .then((data) => {
        setRules(data.rules || "");
        setLoading(false);
      })
      .catch(() => {
        setError("Failed to load rules");
        setLoading(false);
      });
  }, []);

  const handleSave = async () => {
    setSaving(true);
    setSuccess(false);
    setError(null);
    try {
      const res = await fetch(RULES_API, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ rules }),
      });
      if (res.ok) {
        setSuccess(true);
      } else {
        setError("Failed to save rules");
      }
    } catch {
      setError("Failed to save rules");
    }
    setSaving(false);
  };

  return (
    <div className="min-h-screen bg-[#0f0f0f] text-white px-8 py-8">
      <h1 className="text-lg font-medium mb-6">Agent Rules Editor</h1>
      {loading ? (
        <p className="text-sm text-gray-400">Loading...</p>
      ) : (
        <>
          <textarea
            className="w-full h-64 bg-[#222] text-yellow-200 font-mono p-4 rounded-lg border border-[#8b0000] focus:outline-none focus:ring-2 focus:ring-[#8b0000]"
            value={rules}
            onChange={(e) => setRules(e.target.value)}
            spellCheck={false}
            style={{ fontSize: "1rem" }}
          />
          <div className="mt-4 flex gap-2">
            <button
              className="px-4 py-2 rounded bg-[#8b0000] text-yellow-200 font-bold"
              onClick={handleSave}
              disabled={saving}
            >
              {saving ? "Saving..." : "Save"}
            </button>
            {success && <span className="text-green-400">Saved!</span>}
            {error && <span className="text-red-400">{error}</span>}
          </div>
        </>
      )}
    </div>
  );
};

export default RulesEditor;
