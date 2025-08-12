import "../styles/globals.css";
import Sidebar from "../components/Sidebar";

export default function RootLayout({ children }) {
  return (
    <html lang="en" className="dark">
      <body 
        className="min-h-screen bg-[var(--background)] text-[var(--foreground)]"
        style={{ padding: 'var(--layout-outer-padding)' }}
      >
        <div 
          className="flex overflow-hidden" 
          style={{ 
            gap: 'var(--sidebar-gap)',
            minHeight: 'calc(100vh - 2 * var(--layout-outer-padding))'
          }}
        >
          <Sidebar />
          <main 
            className="flex-1 flex flex-col"
            style={{ minHeight: 'calc(100vh - 2 * var(--layout-outer-padding))' }}
          >
            {/* Scrollable content area with improved spacing */}
            <div className="flex-1 overflow-y-auto" style={{ 
              padding: 'var(--layout-padding) var(--spacing-xl) var(--layout-padding) var(--spacing-lg)'
            }}>
              <div className="max-w-6xl mx-auto w-full" style={{ 
                display: 'flex',
                flexDirection: 'column',
                gap: 'var(--component-gap)'
              }}>
                {children}
              </div>
            </div>
          </main>
        </div>
      </body>
    </html>
  );
}
