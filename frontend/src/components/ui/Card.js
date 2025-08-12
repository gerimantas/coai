"use client";

export default function Card({ children, className = "" }) {
  return (
  <div className={`bg-[var(--card)] text-[var(--foreground)] border border-[var(--border)] rounded-xl shadow p-5 ${className}`}>
      {children}
    </div>
  );
}
