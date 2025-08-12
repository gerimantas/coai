"use client";
import PageContainer from "@/components/ui/PageContainer";
import React from 'react';

const SettingsPage = () => {
  return (
    <PageContainer title="Settings" subtitle="Configuration and preferences.">
      <div className="bg-[var(--background-secondary)] border border-[var(--border)] rounded-lg p-6 text-center">
        <p className="text-sm text-[var(--foreground-muted)]">Settings configuration coming soon...</p>
      </div>
    </PageContainer>
  );
};

export default SettingsPage;
