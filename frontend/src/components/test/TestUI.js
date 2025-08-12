"use client";
import Button from '../ui/Button';
import Card from '../ui/Card';
import StatusBar from '../ui/StatusBar';
import Loader from '../ui/Loader';
import Alert from '../ui/Alert';
import Tab from '../ui/Tab';

export default function TestUI() {
  return (
    <div className="p-8 space-y-6 bg-background min-h-screen text-foreground">
  <h2 className="text-lg font-medium mb-4">UI Components Demo</h2>
      <Card>
        <div className="space-x-2 mb-2">
          <Button>Primary</Button>
          <Button variant="secondary">Secondary</Button>
          <Button variant="danger">Danger</Button>
        </div>
        <div className="space-x-2 mb-2">
          <Tab label="Tab 1" active />
          <Tab label="Tab 2" />
        </div>
        <Loader />
        <Alert type="info">Info alert</Alert>
        <Alert type="success">Success alert</Alert>
        <Alert type="warning">Warning alert</Alert>
        <Alert type="error">Error alert</Alert>
      </Card>
      <StatusBar status="Demo mode" />
    </div>
  );
}
