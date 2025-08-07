# Next.js Universal UI Template

This template is designed for a quick start of a modern Next.js (React 19) application with a universal component base, Tailwind CSS, and Radix UI.

## Features
- Next.js 15 (app directory)
- React 19
- Tailwind CSS
- Radix UI
- Core UI components (Toolbar, Sidebar, Button, Card, etc.)
- Ready for additional pages and tabs

## Structure
- `src/app/` – Next.js pages and layout
- `src/components/` – UI components
- `public/` – static files

## Usage
1. Copy this template to a new project
2. Install dependencies: `npm install`
3. Start the dev server: `npm run dev`
4. Add your own pages, API, or logic

## Example File Structure

```
ui-template/
├── .env.local              # Environment variables (not committed)
├── .gitignore              # Git ignore rules
├── README.md               # Project documentation
├── package.json            # Project dependencies and scripts
├── next.config.mjs         # Next.js configuration
├── postcss.config.mjs      # PostCSS configuration for Tailwind
├── tailwind.config.js      # Tailwind CSS configuration
├── jsconfig.json           # JS/TS path aliases
├── public/                 # Static assets (favicon, images, etc.)
│   └── favicon.ico
├── src/
│   ├── app/                # Next.js app directory (pages, layout)
│   │   ├── layout.js       # Root layout for all pages
│   │   ├── page.js         # Main page (entry point)
│   │   └── globals.css     # Global styles (Tailwind)
│   ├── components/         # Reusable UI components
│   │   ├── MainContent.js  # Main content area
│   │   ├── Toolbar.js      # Top toolbar
│   │   ├── Sidebar.js      # Side navigation
│   │   ├── StatusBar.js    # Bottom status bar
│   │   ├── Card.js         # Card UI element
│   │   └── Button.js       # Universal button
│   └── styles/             # (Optional) Additional CSS files
└── (test, lint, CI files as needed)
```
