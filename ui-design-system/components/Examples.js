// ================================
// COAI UI Design System Examples
// ================================

import Input from './Input';
import ChatInput from './ChatInput';
import PageContainer from './PageContainer';
import Sidebar from './Sidebar';

// ================================
// 1. INPUT COMPONENT EXAMPLES
// ================================

// Basic Input
<Input 
  placeholder="Search files..."
  value={searchTerm}
  onChange={(e) => setSearchTerm(e.target.value)}
/>

// Large textarea with auto-resize
<Input 
  type="textarea" 
  autoResize={true}
  placeholder="Enter your message..."
  value={content}
  onChange={(e) => setContent(e.target.value)}
/>

// Variants
<Input variant="default" />    // Standard input
<Input variant="filled" />     // Filled background
<Input variant="outline" />    // Outline only

// Sizes
<Input size="sm" />   // Small
<Input size="md" />   // Medium (default)
<Input size="lg" />   // Large

// ================================
// 2. CHAT INPUT EXAMPLES
// ================================

// Basic Chat Input
<ChatInput
  value={message}
  onChange={(e) => setMessage(e.target.value)}
  onSubmit={handleSubmit}
  placeholder="Ask anything..."
  disabled={isLoading}
  loading={isLoading}
/>

// Chat Input with file attachments
<ChatInput
  value={message}
  onChange={(e) => setMessage(e.target.value)}
  onSubmit={handleSubmit}
  attachedFiles={files}
  onFilesChange={setFiles}
  placeholder="Attach files and ask questions..."
/>

// ================================
// 3. PAGE CONTAINER EXAMPLES
// ================================

// Basic page layout
<PageContainer title="Settings" subtitle="Configure your preferences">
  <div>Your page content here</div>
</PageContainer>

// Page without subtitle
<PageContainer title="Dashboard">
  <div>Dashboard content</div>
</PageContainer>

// Page without header
<PageContainer>
  <div>Raw content without header</div>
</PageContainer>

// ================================
// 4. LAYOUT USAGE EXAMPLES
// ================================

// In your main layout file (layout.js or _app.js)
import RootLayout from './layouts/RootLayout';

export default function MyApp({ children }) {
  return (
    <RootLayout>
      {children}
    </RootLayout>
  );
}

// ================================
// 5. STYLING EXAMPLES
// ================================

// Using CSS variables in custom components
const MyComponent = () => (
  <div style={{
    padding: 'var(--spacing-lg)',
    backgroundColor: 'var(--card)',
    border: '1px solid var(--border)',
    borderRadius: 'var(--radius-lg)',
    color: 'var(--foreground)'
  }}>
    Custom styled component
  </div>
);

// Using CSS classes
const AnotherComponent = () => (
  <div className="card">
    Card component using predefined CSS class
  </div>
);

// ================================
// 6. FORM EXAMPLES
// ================================

// Login form
<PageContainer title="Login" subtitle="Access your account">
  <form onSubmit={handleLogin}>
    <div style={{ display: 'flex', flexDirection: 'column', gap: 'var(--spacing-md)' }}>
      <Input
        type="email"
        placeholder="Email address"
        value={email}
        onChange={(e) => setEmail(e.target.value)}
        required
      />
      <Input
        type="password"
        placeholder="Password"
        value={password}
        onChange={(e) => setPassword(e.target.value)}
        required
      />
      <button type="submit" className="btn-primary">
        Sign In
      </button>
    </div>
  </form>
</PageContainer>

// ================================
// 7. CHAT INTERFACE EXAMPLE
// ================================

<PageContainer title="AI Assistant" subtitle="Chat with your AI helper">
  {/* Messages */}
  <div className="messages-container">
    {messages.map((msg, idx) => (
      <div key={idx} className={msg.role === 'user' ? 'message-user' : 'message-ai'}>
        {msg.text}
      </div>
    ))}
  </div>
  
  {/* Chat Input */}
  <ChatInput
    value={input}
    onChange={(e) => setInput(e.target.value)}
    onSubmit={handleSendMessage}
    attachedFiles={attachedFiles}
    onFilesChange={setAttachedFiles}
    placeholder="Type your message..."
    loading={isLoading}
  />
</PageContainer>

export default function Examples() {
  return (
    <div>
      <h1>These are examples of how to use the components!</h1>
    </div>
  );
}
