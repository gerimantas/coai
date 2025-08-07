/** @type {import('tailwindcss').Config} */
module.exports = {
  darkMode: 'class',
  content: [
    "./src/**/*.{js,ts,jsx,tsx}",
    "./src/styles/**/*.{css,scss}"
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
      },
      borderRadius: {
        xl: '1rem',
      },
      boxShadow: {
        card: '0 2px 8px 0 rgba(0,0,0,0.15)',
      },
    },
  },
  plugins: [],
};
