import type { Metadata } from "next";
import { Inter } from "next/font/google";
import "./globals.css";

const inter = Inter({ subsets: ["latin"] });

export const metadata: Metadata = {
  title: "Credly - Shop Ledger",
  description: "Simple ledger and order management for distributors",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body className={inter.className}>
        <div className="min-h-screen bg-gray-50">
          <header className="bg-white shadow-sm">
            <div className="max-w-md mx-auto px-4 py-4">
              <h1 className="text-xl font-bold text-gray-900">Credly</h1>
            </div>
          </header>
          <main className="max-w-md mx-auto px-4 py-6">
            {children}
          </main>
        </div>
      </body>
    </html>
  );
}
