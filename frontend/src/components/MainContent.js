"use client";
import Toolbar from "./Toolbar";
import Sidebar from "./Sidebar";
import StatusBar from "./StatusBar";
import Card from "./Card";

export default function MainContent() {
  // Dummy project info for MVP
  const projectInfo = {
    name: "COAI MVP",
    path: "C:/ai_projects/coai",
    planFile: "coai_plan copy.md",
    status: "Vykdomas MVP etapas"
  };
  return (
    <div className="flex min-h-screen" style={{backgroundColor: 'var(--background)', color: 'var(--foreground)'}}>
      <Sidebar />
      <div className="flex-1 flex flex-col">
        <Toolbar />
        <main className="flex-1 p-6">
          {/* Aktyvaus projekto informacija */}
          <div className="mb-4 p-4 rounded-lg border border-gray-700 bg-gray-900 text-gray-100 shadow">
            <div className="font-bold text-lg mb-1">Aktyvus projektas: {projectInfo.name}</div>
            <div className="text-sm">Kelias: <span className="font-mono">{projectInfo.path}</span></div>
            <div className="text-sm">Planų failas: <span className="font-mono">{projectInfo.planFile}</span></div>
            <div className="text-sm">Statusas: <span className="font-semibold text-green-400">{projectInfo.status}</span></div>
          </div>
          <h1 className="text-2xl font-bold mb-4" style={{color: 'var(--foreground)'}}>Welcome to the UI Template</h1>
          <Card>
            <p>This is a universal Next.js UI template. Replace this content with your app.</p>
          </Card>
        </main>
        <StatusBar />
      </div>
    </div>
  );
}
