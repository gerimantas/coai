"use client";

export default function Alert({ children, type = "info", variant = "default" }) {
  // Support both type and variant props for backwards compatibility
  const alertType = variant !== "default" ? variant : type;
  
  const base = "p-4 rounded-xl font-semibold mb-2";
  const types = {
    info: "bg-blue-900 text-blue-100 border border-blue-700",
    success: "bg-green-900 text-green-100 border border-green-700",
    warning: "bg-yellow-900 text-yellow-100 border border-yellow-700",
    error: "bg-red-900 text-red-100 border border-red-700",
    destructive: "bg-red-900 text-red-100 border border-red-700",
    default: "bg-blue-900 text-blue-100 border border-blue-700"
  };
  return (
    <div className={`${base} ${types[alertType]}`}>
      {children}
    </div>
  );
}

// Named exports for compatibility
export { Alert };

export const AlertDescription = ({ children, className = '', ...props }) => {
  return (
    <div className={`text-sm ${className}`} {...props}>
      {children}
    </div>
  )
}
