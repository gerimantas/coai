# Tailwind Dark Theme Template

This template provides a ready-to-use dark theme color palette and reusable component styles for any Tailwind CSS project. You can easily copy these files and settings into your own Next.js, React, or other Tailwind-based project.

## Features
- Customizable dark color palette (background, foreground, primary, border, card)
- Global styles for body, card, button, and border
- Utility classes for consistent component styling
- Easy to extend or override

## How to Use

1. **Copy Files**
   - Copy `tailwind.config.js` to your project root.
   - Copy `src/styles/globals.css` to your styles directory (or merge with your global CSS).

2. **Configure Tailwind**
   - Make sure your Tailwind setup points to the correct content paths (see `tailwind.config.js`).
   - Import `globals.css` in your main layout or entry file (e.g., `import './styles/globals.css'`).

3. **Use Utility Classes**
   - Use classes like `bg-background`, `text-foreground`, `card`, `btn-primary`, `border-default` in your components.
   - Example:
     ```jsx
     <div className="card">Dark themed card content</div>
     <button className="btn-primary">Primary Action</button>
     <div className="border-default">Bordered box</div>
     ```

4. **Enable Dark Mode (Optional)**
   - Add `dark` class to `<html>` or `<body>` to enable dark mode (if using Tailwind's `darkMode: 'class'`).

5. **Customize**
   - Edit `tailwind.config.js` to change colors, border radius, or shadows as needed.

---
This template is framework-agnostic and works with any Tailwind CSS project.
