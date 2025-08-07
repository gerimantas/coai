import "./globals.css";

export const metadata = {
  title: "UI Template",
  description: "Universal Next.js UI template",
};

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <body className="bg-gray-100 text-gray-900">
        {children}
      </body>
    </html>
  );
}
