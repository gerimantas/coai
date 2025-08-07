"use client";
import Toolbar from "./Toolbar";
import Sidebar from "./Sidebar";
import StatusBar from "./StatusBar";
import Card from "./Card";

export default function MainContent() {
  return (
    <div className="flex min-h-screen" style={{backgroundColor: 'var(--background)', color: 'var(--foreground)'}}>
      <Sidebar />
      <div className="flex-1 flex flex-col">
        <Toolbar />
        <main className="flex-1 p-6">
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
