"use client";
export default function Card({ children }) {
  return (
    <div className="bg-white rounded-lg shadow p-4 mb-4 border">
      {children}
    </div>
  );
}
