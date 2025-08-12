"use client";
import React, { useEffect, useState } from "react";
import PageContainer from "@/components/ui/PageContainer";

const RULES_API = "/api/agent_rules";

const RulesEditor = () => {
  const [rules, setRules] = useState("");
  const [loading, setLoading] = useState(true);
  const [saving, setSaving] = useState(false);
  const [error, setError] = useState(null);
  const [success, setSuccess] = useState(false);
  const [reloadStatus, setReloadStatus] = useState("");

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
        // Reload rules in backend
        const reloadRes = await fetch("/api/rules/reload", { method: "POST" });
        if (reloadRes.ok) {
          setReloadStatus("Rules reloaded successfully.");
        } else {
          setReloadStatus("Failed to reload rules.");
        }
      } else {
        setError("Failed to save rules");
      }
    } catch {
      setError("Failed to save rules");
    }
    setSaving(false);
  };

  return (
    <PageContainer title="Agent Rules" subtitle="Edit and reload rules for agents.">
      <div className="max-w-3xl mx-auto">
        <h2 className="text-base font-medium mb-4">Edit Agent Rules</h2>
        {loading ? (
          <p className="text-sm text-[var(--foreground-muted)]">Loading rules...</p>
        ) : error ? (
          <p className="text-sm text-red-400">{error}</p>
        ) : (
          <textarea
            className="w-full min-h-40 p-3 rounded-lg border border-[var(--border)] bg-[var(--background-secondary)] text-[var(--foreground)] mb-4 resize-y"
            value={rules}
            onChange={(e) => setRules(e.target.value)}
            disabled={saving}
          />
        )}
        <button
          className="px-4 py-2 rounded-md border border-blue-500 text-blue-400 hover:bg-blue-500/10 text-sm font-medium"
          onClick={handleSave}
          disabled={saving}
        >
          {saving ? "Saving..." : "Save Rules"}
        </button>
        {success && (
          <p className="text-green-400 text-xs mt-2">Rules saved successfully.</p>
        )}
        {reloadStatus && (
          <p className="text-blue-400 text-xs mt-2">{reloadStatus}</p>
        )}
      </div>
    </PageContainer>
  );
};

export default RulesEditor;
