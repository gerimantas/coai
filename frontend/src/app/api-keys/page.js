"use client";
import PageContainer from "@/components/ui/PageContainer";
import React from 'react';

const ApiKeysPage = () => {
  return (
    <PageContainer title="API keys" subtitle="Manage credentials for external services.">
      <div className="bg-[var(--background-secondary)] border border-[var(--border)] rounded-lg p-6 text-center">
        <p className="text-sm text-[var(--foreground-muted)]">API key management coming soon...</p>
      </div>
    </PageContainer>
  );
};

export default ApiKeysPage;
