import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "Mini-SIEM — SOC-style Log Monitoring & Incident Response",
  description:
    "Mini SIEM built with Python + Streamlit. Log ingestion, detection rules, alerting, and incident response workflow.",
};

export default function RootLayout({
  children,
}: Readonly<{ children: React.ReactNode }>) {
  return (
    <html lang="en">
      <body className="min-h-screen bg-black text-white antialiased">
        {children}
      </body>
    </html>
  );
}
