"use client";
export default function Sidebar() {
  return (
    <aside className="w-56 border-r border-default min-h-screen p-4" style={{backgroundColor: 'var(--background)'}}>
      <nav>
        <ul className="space-y-2">
          <li><a href="/" className="block p-2 rounded hover:opacity-80 transition" style={{color: 'var(--foreground)', backgroundColor: 'transparent'}} onMouseEnter={e => e.target.style.backgroundColor = 'var(--background-light)'} onMouseLeave={e => e.target.style.backgroundColor = 'transparent'}>Home</a></li>
          <li><a href="/chat" className="block p-2 rounded hover:opacity-80 transition" style={{color: 'var(--foreground)', backgroundColor: 'transparent'}} onMouseEnter={e => e.target.style.backgroundColor = 'var(--background-light)'} onMouseLeave={e => e.target.style.backgroundColor = 'transparent'}>Chat</a></li>
          {/* Pridėkite papildomus puslapius ar nuorodas */}
        </ul>
      </nav>
    </aside>
  );
}
