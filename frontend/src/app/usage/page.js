"use client";
import PageContainer from "@/components/ui/PageContainer";
import React from 'react';

const UsagePage = () => {
  return (
    <PageContainer title="Usage" subtitle="Requests, tokens, and costs.">
      <div className="bg-[var(--background-secondary)] border border-[var(--border)] rounded-lg p-6 text-center">
        <p className="text-sm text-[var(--foreground-muted)]">Usage statistics coming soon...</p>
      </div>
    </PageContainer>
  );
};

export default UsagePage;
