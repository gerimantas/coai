"use client";

function Card({ children, className = "" }) {
  return (
    <div className={`bg-[var(--card)] text-[var(--foreground)] border border-[var(--border)] rounded-xl shadow p-5 ${className}`}>
      {children}
    </div>
  );
}

function CardHeader({ children, className = "" }) {
  return (
    <div className={`mb-4 ${className}`}>
      {children}
    </div>
  );
}

function CardTitle({ children, className = "" }) {
  return (
    <h3 className={`text-lg font-semibold ${className}`}>
      {children}
    </h3>
  );
}

function CardDescription({ children, className = "" }) {
  return (
    <p className={`text-sm text-[var(--foreground-muted)] mt-1 ${className}`}>
      {children}
    </p>
  );
}

function CardContent({ children, className = "" }) {
  return (
    <div className={`${className}`}>
      {children}
    </div>
  );
}

export { Card, CardHeader, CardTitle, CardDescription, CardContent };
export default Card;
