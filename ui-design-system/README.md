# COAI UI Design System

A complete, production-ready UI design system for Next.js applications with dark theme support, consistent spacing, and reusable components.

## Features

✅ **Dark Theme Ready** - Complete CSS variables system  
✅ **Consistent Spacing** - Unified spacing scale from xs to 3xl  
✅ **Responsive Layout** - Flexible sidebar + main content layout  
✅ **Reusable Components** - Input, ChatInput, PageContainer, Sidebar  
✅ **Auto-resize Inputs** - Smart textarea with scroll support  
✅ **Professional Styling** - Subtle borders, shadows, and transitions  

## Quick Start

### 1. Copy Files to Your Project

```bash
# Copy all files from ui-design-system to your Next.js project
cp -r ui-design-system/* your-nextjs-project/src/
```

### 2. File Structure After Copy

```
src/
├── app/
│   ├── globals.css          # Complete design system CSS
│   └── layout.js            # Root layout with sidebar
├── components/
│   ├── ui/
│   │   ├── Input.js         # Universal input component
│   │   ├── ChatInput.js     # AI chat specialized input
│   │   ├── PageContainer.js # Page wrapper component
│   │   └── StatusBar.js     # Bottom status bar
│   └── Sidebar.js           # Navigation sidebar
```

### 3. Install Dependencies

```bash
npm install next react react-dom
# If using Tailwind CSS:
npm install tailwindcss postcss autoprefixer
```

### 4. Update Your Root Layout

Replace your `app/layout.js` with the provided layout file, or integrate the layout structure:

```javascript
import "./globals.css";
import Sidebar from "@/components/Sidebar";
import StatusBar from "@/components/ui/StatusBar";

export default function RootLayout({ children }) {
  return (
    <html lang="en" className="dark">
      <body className="min-h-screen bg-[var(--background)] text-[var(--foreground)]">
        {/* Layout structure provided */}
      </body>
    </html>
  );
}
```

### 5. Use Components in Your Pages

```javascript
import PageContainer from "@/components/ui/PageContainer";
import Input from "@/components/ui/Input";
import ChatInput from "@/components/ui/ChatInput";

export default function MyPage() {
  return (
    <PageContainer title="My Page" subtitle="Page description">
      <Input 
        type="text" 
        placeholder="Universal input..." 
      />
      
      <ChatInput 
        placeholder="AI chat input..."
        value={input}
        onChange={(e) => setInput(e.target.value)}
      />
    </PageContainer>
  );
}
```

## Components Documentation

### PageContainer
Consistent page wrapper with title, subtitle, and proper spacing.

```javascript
<PageContainer title="Page Title" subtitle="Optional subtitle">
  {/* Your content */}
</PageContainer>
```

### Input (Universal)
Auto-resizing input component with multiple variants and sizes.

```javascript
<Input 
  type="textarea"           // text, textarea, email, password
  variant="filled"          // default, filled, outline
  size="md"                // sm, md, lg
  autoResize={true}        // For textarea auto-height
  placeholder="Enter text..."
/>
```

### ChatInput (AI Specialized)
Advanced chat input with file attachments, agent selector, and action buttons.

```javascript
<ChatInput 
  value={input}
  onChange={(e) => setInput(e.target.value)}
  onSubmit={handleSubmit}
  attachedFiles={files}
  onFilesChange={setFiles}
  placeholder="Ask anything..."
/>
```

### Sidebar
Navigation sidebar with sections and active state management.

```javascript
// Automatically included in layout.js
// Customize menu items in components/Sidebar.js
```

## Design System Variables

All components use CSS variables for consistent theming:

### Colors
```css
--background: #0a0a0a          /* Main background */
--background-secondary: #111   /* Secondary background */
--foreground: #fff             /* Main text */
--primary: #3b82f6             /* Brand blue */
--border: #888888              /* Component borders */
--card: #1a1a1a               /* Card backgrounds */
```

### Spacing Scale
```css
--spacing-xs: 0.5rem    /* 8px */
--spacing-sm: 0.75rem   /* 12px */
--spacing-md: 1rem      /* 16px */
--spacing-lg: 1.5rem    /* 24px */
--spacing-xl: 2rem      /* 32px */
--spacing-2xl: 2.5rem   /* 40px */
--spacing-3xl: 3rem     /* 48px */
```

### Layout Variables
```css
--layout-padding: var(--spacing-lg)      /* 24px */
--layout-outer-padding: var(--spacing-md) /* 16px */
--sidebar-gap: var(--spacing-md)         /* 16px */
```

## Customization

### Changing Colors
Edit CSS variables in `globals.css`:

```css
:root {
  --primary: #your-brand-color;
  --background: #your-bg-color;
  /* ... other variables */}
```

### Adding New Components
Follow the existing component patterns:

1. Use CSS variables for styling
2. Include proper TypeScript/PropTypes
3. Support disabled/loading states
4. Include focus and hover states

### Responsive Behavior
The layout automatically adapts:
- Sidebar: Fixed width on desktop
- Main content: Flexible with max-width constraints
- Components: Scale with CSS variables

## Browser Support

- ✅ Chrome 90+
- ✅ Firefox 88+  
- ✅ Safari 14+
- ✅ Edge 90+

## License

MIT License - feel free to use in any project.

## Support

This design system was extracted from the COAI project. For questions or improvements, refer to the original implementation.

---

**Happy coding! 🚀**
