import "./globals.css";

export const metadata = {
  title: "UI Template",
  description: "Universal Next.js UI template",
};

export default function RootLayout({ children }) {
  return (
    <html lang="en" className="dark">
      <body>
        {children}
      </body>
    </html>
  );
}
