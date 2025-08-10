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
    <PageContainer>
      <h1 className="text-lg font-medium mb-6">Test UI Components</h1>
      <div className="mb-6 flex gap-4 flex-wrap">
        <Button variant="primary">Primary Button</Button>
        <Button variant="secondary">Secondary Button</Button>
        <Button variant="danger">Danger Button</Button>
      </div>
      <div className="mb-6 flex gap-4 flex-wrap">
        <Card>
          <h2 className="text-base font-semibold mb-2">Card Title</h2>
          <p className="text-sm text-gray-400">This is a card component with some content.</p>
        </Card>
      </div>
      <div className="mb-6 flex gap-4 flex-wrap">
        <Alert type="success">This is a success alert!</Alert>
        <Alert type="error">This is an error alert!</Alert>
        <Alert type="info">This is an info alert!</Alert>
        <Alert type="warning">This is a warning alert!</Alert>
      </div>
      <div className="mb-6 flex gap-4 flex-wrap">
        <Tab label="Active Tab" active={true} />
        <Tab label="Inactive Tab" active={false} />
      </div>
      <div className="mb-6">
        <Loader />
      </div>
      <div className="mb-6">
        <StatusBar status="Ready" />
      </div>
    </PageContainer>
  );
}
