
"use client";

import React from "react";

export default function Button({ children, variant = "primary", as = "button", className = "", ...props }) {
  const base = "px-6 py-3 rounded-lg font-medium border transition-all duration-200 focus:outline-none focus:ring-2 focus:ring-blue-500 disabled:opacity-50 shadow-sm hover:shadow-md";
  const variants = {
    primary: "bg-blue-600 text-white border-blue-600 hover:bg-blue-700 hover:border-blue-700 active:bg-blue-800",
    secondary: "bg-gray-700 text-gray-100 border-gray-600 hover:bg-gray-600 hover:border-gray-500 active:bg-gray-500",
    danger: "bg-red-600 text-white border-red-600 hover:bg-red-700 hover:border-red-700 active:bg-red-800"
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
