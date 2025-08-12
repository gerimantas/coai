"use client";
import PageContainer from "@/components/ui/PageContainer";

export default function Home() {
  return (
    <PageContainer title="Welcome to COAI" subtitle="Collaborative AI Assistant Interface">
      <div className="text-center">
        <h1 className="text-lg font-medium" style={{ marginBottom: 'var(--spacing-lg)' }}></h1>
        <div 
          className="bg-[var(--background-secondary)] border border-[var(--border)] rounded-lg"
          style={{ padding: 'var(--spacing-lg)' }}
        >
          <h2 
            className="text-base font-medium"
            style={{ marginBottom: 'var(--spacing-md)' }}
          >
            Getting Started
          </h2>
          <p 
            className="text-sm text-[var(--foreground-muted)]"
            style={{ marginBottom: 'var(--spacing-lg)' }}
          >
            Use the navigation menu on the left to access different features:
          </p>
          <div 
            className="grid grid-cols-1 md:grid-cols-2 text-left"
            style={{ gap: 'var(--spacing-md)' }}
          >
            <div>
              <h3 
                className="text-sm font-medium text-[var(--foreground)]"
                style={{ marginBottom: 'var(--spacing-sm)' }}
              >
                Create
              </h3>
              <p className="text-xs text-[var(--foreground-muted)]">
                Start conversations, generate content, and work with AI assistants
              </p>
            </div>
            <div>
              <h3 
                className="text-sm font-medium text-[var(--foreground)]"
                style={{ marginBottom: 'var(--spacing-sm)' }}
              >
                Manage
              </h3>
              <p className="text-xs text-[var(--foreground-muted)]">
                Monitor usage, manage API keys, and review system logs
              </p>
            </div>
          </div>
        </div>
        <div style={{ marginTop: 'var(--spacing-3xl)' }}>
          <p className="text-[var(--foreground-muted)] text-sm">
            COAI v1.0 - Collaborative AI Assistant Interface
          </p>
        </div>
      </div>
    </PageContainer>
  );
}
