"use client";
import PageContainer from "@/components/ui/PageContainer";
import Button from "@/components/ui/Button";
import Card from "@/components/ui/Card";
import Alert from "@/components/ui/Alert";
import StatusBar from "@/components/ui/StatusBar";
import Loader from "@/components/ui/Loader";
import Tab from "@/components/ui/Tab";

export default function TestUIPage() {
  return (
    <PageContainer title="Test UI Components" subtitle="Showcase of reusable components and states.">
      <div 
        className="flex flex-wrap"
        style={{ gap: 'var(--spacing-sm)' }}
      >
        <Button variant="primary">Primary Button</Button>
        <Button variant="secondary">Secondary Button</Button>
        <Button variant="danger">Danger Button</Button>
      </div>
      
      <div className="flex gap-4 flex-wrap">
        <Card>
          <h2 
            className="text-base font-semibold text-[var(--foreground)]"
            style={{ marginBottom: 'var(--spacing-sm)' }}
          >
            Card Title
          </h2>
          <p className="text-sm text-gray-400">This is a card component with some content.</p>
        </Card>
      </div>
      
      <div 
        style={{ 
          display: 'flex',
          flexDirection: 'column',
          gap: 'var(--spacing-sm)'
        }}
      >
        <Alert type="success">This is a success alert!</Alert>
        <Alert type="error">This is an error alert!</Alert>
        <Alert type="info">This is an info alert!</Alert>
        <Alert type="warning">This is a warning alert!</Alert>
      </div>
      
      <div 
        className="flex flex-wrap"
        style={{ gap: 'var(--spacing-sm)' }}
      >
        <Tab label="Active Tab" active={true} />
        <Tab label="Inactive Tab" active={false} />
      </div>
      
      <div style={{ padding: 'var(--spacing-md) 0' }}>
        <Loader />
      </div>
      
      <div>
        <StatusBar status="Ready" />
      </div>
    </PageContainer>
  );
}
