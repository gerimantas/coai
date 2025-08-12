/** @type {import('tailwindcss').Config} */
module.exports = {
  darkMode: 'class',
  content: [
    "./src/**/*.{js,ts,jsx,tsx}",
    "./src/app/**/*.{js,ts,jsx,tsx}",
    "./src/components/**/*.{js,ts,jsx,tsx}"
  ],
  theme: {
    extend: {
      colors: {
        background: {
          DEFAULT: '#18181b', // gray-900
          light: '#27272a',   // gray-800
        },
        foreground: {
          DEFAULT: '#f4f4f5', // gray-100
          muted: '#a1a1aa',   // gray-400
        },
        primary: {
          DEFAULT: '#2563eb', // blue-600
          dark: '#1e40af',   // blue-800
        },
        border: '#27272a',
        card: '#23232b',
        // COAI Design System Colors
        'coai-primary': 'var(--primary)',
        'coai-success': 'var(--success)',
        'coai-warning': 'var(--warning)',
        'coai-error': 'var(--error)',
        'coai-info': 'var(--info)',
      },
      spacing: {
        // COAI Design System Spacing
        'coai-xs': 'var(--spacing-xs)',
        'coai-sm': 'var(--spacing-sm)',
        'coai-md': 'var(--spacing-md)',
        'coai-lg': 'var(--spacing-lg)',
        'coai-xl': 'var(--spacing-xl)',
        'coai-2xl': 'var(--spacing-2xl)',
        'coai-3xl': 'var(--spacing-3xl)',
      },
      borderRadius: {
        xl: '1rem',
        // COAI Design System Radius
        'coai-sm': 'var(--radius-sm)',
        'coai-md': 'var(--radius-md)',
        'coai-lg': 'var(--radius-lg)',
        'coai-xl': 'var(--radius-xl)',
        'coai-2xl': 'var(--radius-2xl)',
      },
      boxShadow: {
        card: '0 2px 8px 0 rgba(0,0,0,0.15)',
      },
    },
  },
  plugins: [],
};
