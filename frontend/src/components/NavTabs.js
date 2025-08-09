"use client";
import Link from "next/link";
import { usePathname } from "next/navigation";

const tabs = [
  { href: "/", label: "Home" },
  { href: "/chat", label: "Chat" },
  { href: "/files", label: "Files" },
  { href: "/projects", label: "Projects" },
  { href: "/logs", label: "Logs" },
  { href: "/settings", label: "Settings" },
];

export default function NavTabs() {
  const pathname = usePathname();
  return (
    <nav className="flex flex-wrap gap-4">
      {tabs.map((t) => {
        const active = pathname === t.href;
        const base = "px-5 py-2.5 rounded-lg text-sm font-semibold border-2 transition-all duration-200 shadow-sm hover:shadow-md";
        const cls = active
          ? "bg-[var(--primary)] text-white border-[var(--primary)] shadow-lg"
          : "bg-[var(--background-light)] text-[var(--foreground)] border-[var(--border)] hover:bg-[var(--background)] hover:border-[var(--primary)]";
        return (
          <Link key={t.href} href={t.href} className={`${base} ${cls}`}>
            {t.label}
          </Link>
        );
      })}
    </nav>
  );
}
