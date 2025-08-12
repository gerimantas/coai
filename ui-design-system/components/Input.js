import { forwardRef, useEffect, useRef } from 'react';

// Universal Input component for COAI
const Input = forwardRef(({ 
  type = "text", 
  variant = "default",
  size = "md",
  autoResize = false,
  className = "",
  style = {},
  value,
  ...props 
}, ref) => {
  
  const internalRef = useRef(null);
  const textareaRef = ref || internalRef;
  
  const variants = {
    default: "bg-[var(--background-secondary)] border-[var(--primary)] text-[var(--foreground)]",
    filled: "bg-[var(--card)] border-[var(--primary)] text-[var(--foreground)]",
    outline: "bg-transparent border-[var(--primary)] text-[var(--foreground)]"
  };

  const sizes = {
    sm: "px-3 py-2 text-sm",
    md: "px-4 py-3 text-base", 
    lg: "px-5 py-4 text-lg"
  };

  const baseStyles = `
    w-full rounded-lg border transition-all duration-200
    placeholder:text-[var(--foreground-muted)]
    focus:outline-none focus:border-[var(--primary)] focus:ring-2 focus:ring-[var(--primary)]/20
    hover:border-[var(--primary)]/60
    disabled:opacity-50 disabled:cursor-not-allowed
  `;

  const textareaStyles = autoResize ? `
    resize-none overflow-y-auto min-h-[60px] max-h-[200px]
  ` : `
    resize-y min-h-[80px] overflow-y-auto
  `;

  const combinedClassName = `
    ${baseStyles}
    ${variants[variant]}
    ${sizes[size]}
    ${type === 'textarea' ? textareaStyles : ''}
    ${type === 'textarea' ? 'chat-textarea' : 'coai-input'}
    ${className}
  `.trim();

  const combinedStyle = {
    ...style,
    lineHeight: 'var(--line-height-normal)',
    fontFamily: 'inherit'
  };

  // Auto-resize functionality for textarea
  const adjustHeight = (element) => {
    if (autoResize && type === 'textarea' && element) {
      // Reset height to get correct scrollHeight
      element.style.height = 'auto';
      // Calculate new height with limits
      const minHeight = 60;
      const maxHeight = 200;
      const scrollHeight = element.scrollHeight;
      const newHeight = Math.max(minHeight, Math.min(scrollHeight, maxHeight));
      element.style.height = newHeight + 'px';
      
      // Show scrollbar if content exceeds max height
      if (scrollHeight > maxHeight) {
        element.style.overflowY = 'auto';
      } else {
        element.style.overflowY = 'hidden';
      }
    }
  };

  const handleInput = (e) => {
    adjustHeight(e.target);
    if (props.onChange) {
      props.onChange(e);
    }
  };

  // Adjust height when value changes or component mounts
  useEffect(() => {
    if (autoResize && type === 'textarea' && textareaRef.current) {
      // Small delay to ensure DOM is ready
      setTimeout(() => {
        adjustHeight(textareaRef.current);
      }, 0);
    }
  }, [value, autoResize, type]);

  if (type === 'textarea') {
    return (
      <textarea
        ref={textareaRef}
        className={combinedClassName}
        style={combinedStyle}
        value={value}
        onChange={handleInput}
        {...props}
      />
    );
  }

  return (
    <input
      ref={textareaRef}
      type={type}
      className={combinedClassName}
      style={combinedStyle}
      value={value}
      onChange={props.onChange}
      {...props}
    />
  );
});

Input.displayName = 'Input';

export default Input;
