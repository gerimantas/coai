"use client";
import PageContainer from "@/components/ui/PageContainer";
import React from 'react';

const AssistantsPage = () => {
  const assistants = [
    {
      id: 'asst_DULbwnhTvSZbrISwNRd7oPvo',
      name: 'Untitled assistant',
      time: '10:02 PM',
      date: 'Last month, Jul 26'
    },
    {
      id: 'asst_1EixGymuukayxIy6eQJwEAjI',
      name: 'copilot',
      time: '7:52 PM',
      date: 'Last month, Jul 21'
    }
  ];

  return (
  <PageContainer title="Assistants" subtitle="Recent assistants and sessions.">
      <div className="space-y-4">
        {assistants.map((assistant, index) => (
          <div key={assistant.id}>
            {/* Date separator */}
      <div className="text-xs text-[var(--foreground-muted)] mb-2 font-medium">
              {assistant.date}
            </div>
            {/* Assistant card */}
      <div className="bg-[var(--background-secondary)] border border-[var(--border)] rounded-lg p-4 hover:bg-[var(--background-tertiary)] transition-colors cursor-pointer">
              <div className="flex items-center justify-between">
                <div className="flex-1">
          <h3 className="text-sm font-medium text-[var(--foreground)] mb-1">
                    {assistant.name}
                  </h3>
          <p className="text-xs text-[var(--foreground-muted)] font-mono">
                    {assistant.time}
                  </p>
                </div>
              </div>
            </div>
          </div>
        ))}
      </div>
    </PageContainer>
  );
};

export default AssistantsPage;
