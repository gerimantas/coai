export default function StatusBar({ status = "Ready" }) {
  return (
  <footer className="border-t border-[var(--border)] px-4 sm:px-8 py-2 text-xs bg-[var(--background-secondary)] text-[var(--foreground-muted)]">
      {status}
    </footer>
  );
}
