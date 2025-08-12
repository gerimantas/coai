"use client";
import PageContainer from "@/components/ui/PageContainer";
import React from 'react';
import FileBrowser from "../../components/FileBrowser";

const FilesPage = () => {
  return (
    <PageContainer title="Files">
      <FileBrowser />
    </PageContainer>
  );
};

export default FilesPage;
