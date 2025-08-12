"use client";
import PageContainer from "@/components/ui/PageContainer";
import React from 'react';

const LogsPage = () => {
  return (
    <PageContainer title="Logs" subtitle="System and application events.">
      <div className="bg-[var(--background-secondary)] border border-[var(--border)] rounded-lg p-6 text-center">
        <p className="text-sm text-[var(--foreground-muted)]">System logs coming soon...</p>
      </div>
    </PageContainer>
  );
};

export default LogsPage;
