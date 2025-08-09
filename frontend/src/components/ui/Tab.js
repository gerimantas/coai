"use client";

export default function Tab({ label, active, ...props }) {
  return (
    <button
      className={`px-4 py-2 rounded-t-xl font-semibold border-b-2 transition ${active ? "border-primary text-primary bg-background-light" : "border-transparent text-foreground bg-background"}`}
      {...props}
    >
      {label}
    </button>
  );
}
