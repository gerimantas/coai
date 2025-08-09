export default function StatusBar({ status = "Ready" }) {
  return (
    <footer className="border-t border-[var(--border)] px-8 py-2 text-xs bg-[var(--background-light)] text-[var(--foreground-muted)]">
      {status}
    </footer>
  );
}
