"use client";
import { usePathname } from "next/navigation";
import Button from "./ui/Button";

export default function GlobalNav() {
  const pathname = usePathname();
  
  return (
    <nav className="fixed top-4 left-4 z-50 flex gap-3">
      <Button 
        as="a" 
        href="/chat" 
        variant={pathname === "/chat" ? "primary" : "secondary"}
        className="px-4 py-2 text-sm"
      >
        Chat
      </Button>
      <Button 
        as="a" 
        href="/files" 
        variant={pathname === "/files" ? "primary" : "secondary"}
        className="px-4 py-2 text-sm"
      >
        Files
      </Button>
      <Button 
        as="a" 
        href="/projects" 
        variant={pathname === "/projects" ? "primary" : "secondary"}
        className="px-4 py-2 text-sm"
      >
        Projects
      </Button>
      <Button 
        as="a" 
        href="/logs" 
        variant={pathname === "/logs" ? "primary" : "secondary"}
        className="px-4 py-2 text-sm"
      >
        Logs
      </Button>
      <Button 
        as="a" 
        href="/settings" 
        variant={pathname === "/settings" ? "primary" : "secondary"}
        className="px-4 py-2 text-sm"
      >
        Settings
      </Button>
    </nav>
  );
}
