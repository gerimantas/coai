// Page wrapper component with consistent layout
export default function PageContainer({ children, title, subtitle }) {
  return (
    <section 
      className="bg-[var(--card)] border border-[var(--border)] rounded-xl shadow-md h-full"
      style={{ 
        padding: 'var(--spacing-lg)',
        marginBottom: 'var(--spacing-lg)',
        display: 'flex',
        flexDirection: 'column'
      }}
    >
      {title && (
        <header style={{ marginBottom: 'var(--spacing-lg)' }}>
          <h1 
            className="text-xl font-semibold text-[var(--foreground)] tracking-tight"
            style={{ marginBottom: 'var(--spacing-xs)' }}
          >
            {title}
          </h1>
          {subtitle && (
            <p className="text-sm text-[var(--foreground-muted)]">{subtitle}</p>
          )}
        </header>
      )}
      <div style={{ 
        display: 'flex',
        flexDirection: 'column',
        gap: 'var(--spacing-md)',
        flex: 1
      }}>
        {children}
      </div>
    </section>
  );
}
