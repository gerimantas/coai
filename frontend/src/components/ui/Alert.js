"use client";

export default function Alert({ children, type = "info" }) {
  const base = "p-4 rounded-xl font-semibold mb-2";
  const types = {
    info: "bg-blue-900 text-blue-100 border border-blue-700",
    success: "bg-green-900 text-green-100 border border-green-700",
    warning: "bg-yellow-900 text-yellow-100 border border-yellow-700",
    error: "bg-red-900 text-red-100 border border-red-700"
  };
  return (
    <div className={`${base} ${types[type]}`}>
      {children}
    </div>
  );
}
