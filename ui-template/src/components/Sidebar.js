"use client";
export default function Sidebar() {
  return (
    <aside className="w-56 bg-gray-50 border-r min-h-screen p-4">
      <nav>
        <ul className="space-y-2">
          <li><a href="#" className="block p-2 rounded hover:bg-gray-200">Home</a></li>
          {/* Pridėkite papildomus puslapius ar nuorodas */}
        </ul>
      </nav>
    </aside>
  );
}
