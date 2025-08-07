"use client";
export default function Toolbar() {
  return (
    <header className="border-b border-default px-4 py-2 flex items-center gap-4 shadow-sm" style={{backgroundColor: 'var(--background-light)'}}>
      <span className="font-semibold" style={{color: 'var(--foreground)'}}>Toolbar</span>
      {/* Pridėkite mygtukus ar meniu čia */}
    </header>
  );
}
