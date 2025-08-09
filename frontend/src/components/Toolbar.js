"use client";
import Button from "./ui/Button";

export default function Toolbar() {
  return (
    <header className="border-b border-[var(--border)] px-8 py-4 bg-[var(--background-light)]">
      <div className="flex items-center justify-between">
        <span className="text-sm text-[var(--foreground-muted)]">COAI Development Environment</span>
        <Button variant="primary" className="text-sm px-4 py-1">Demo</Button>
      </div>
    </header>
  );
}
