import React from 'react';

const Badge = ({ children, variant = "default", className = "", ...props }) => {
  const baseClasses = "inline-flex items-center rounded-md px-2 py-1 text-xs font-medium ring-1 ring-inset";
  
  const variantClasses = {
    default: "bg-blue-50 text-blue-700 ring-blue-700/10",
    secondary: "bg-gray-50 text-gray-600 ring-gray-500/10",
    outline: "bg-transparent text-gray-900 ring-gray-300",
    success: "bg-green-50 text-green-700 ring-green-600/20",
    warning: "bg-yellow-50 text-yellow-800 ring-yellow-600/20",
    error: "bg-red-50 text-red-700 ring-red-600/10"
  };

  const classes = `${baseClasses} ${variantClasses[variant] || variantClasses.default} ${className}`;

  return (
    <span className={classes} {...props}>
      {children}
    </span>
  );
};

export { Badge };
export default Badge;
