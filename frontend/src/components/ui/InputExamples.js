// COAI Input Examples and Usage Guide

// Basic Input
<Input 
  type="text" 
  placeholder="Enter text..."
  value={value}
  onChange={(e) => setValue(e.target.value)}
/>

// Auto-resizing Textarea (like Chat)
<Input 
  type="textarea"
  autoResize={true}
  placeholder="Type your message..."
  value={message}
  onChange={(e) => setMessage(e.target.value)}
  style={{ minHeight: '80px', maxHeight: '200px' }}
/>

// Different variants
<Input variant="default" />    // Standard input
<Input variant="filled" />     // Filled background
<Input variant="outline" />    // Outline only

// Different sizes
<Input size="sm" />   // Small
<Input size="md" />   // Medium (default)
<Input size="lg" />   // Large

// Form Examples for other pages:

// Search Input (Files page)
<Input 
  type="text"
  placeholder="Search files..."
  variant="outline"
  size="sm"
/>

// Settings Input
<Input 
  type="text"
  placeholder="API Key"
  variant="filled"
  size="md"
/>

// Project Name Input
<Input 
  type="text"
  placeholder="Project name..."
  variant="default"
  size="lg"
/>

// Multi-line Description
<Input 
  type="textarea"
  placeholder="Project description..."
  autoResize={false}
  rows={4}
/>

export default function InputExamples() {
  return null; // This is just a reference file
}
