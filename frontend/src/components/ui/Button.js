
"use client";

import React from "react";

export default function Button({ children, variant = "primary", as = "button", className = "", ...props }) {
  const base = "px-4 py-2 rounded-md font-medium border transition-colors duration-150 focus:outline-none focus:ring-1 focus:ring-blue-500 disabled:opacity-50";
  const variants = {
    primary: "bg-transparent text-blue-400 border-blue-500 hover:bg-blue-500/10",
    secondary: "bg-transparent text-[var(--foreground)] border-[var(--border)] hover:bg-white/5",
    danger: "bg-transparent text-red-400 border-red-600 hover:bg-red-600/10"
  };
  const Comp = as;
  const extraProps = {};
  if (Comp === "a") {
    extraProps.role = "button";
    extraProps.tabIndex = 0;
    extraProps.className = `inline-flex items-center justify-center ${base} ${variants[variant]} ${className}`;
  }
  return (
    <Comp
      className={Comp === "a" ? extraProps.className : `inline-flex items-center justify-center ${base} ${variants[variant]} ${className}`}
      {...props}
      {...extraProps}
    >
      {children}
    </Comp>
  );
}
