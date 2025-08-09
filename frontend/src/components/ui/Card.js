"use client";

export default function Card({ children, className = "" }) {
  return (
    <div className={`bg-[var(--card)] text-[var(--foreground)] border-2 border-[var(--border)] rounded-lg shadow-lg p-6 max-w-sm mx-auto ${className}`}>
      {children}
    </div>
  );
}
