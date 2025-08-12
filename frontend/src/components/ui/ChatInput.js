import { forwardRef, useEffect, useRef, useState } from 'react';

// Specialized Chat Input component with Claude-style design
const ChatInput = forwardRef(({ 
  value,
  onChange,
  onKeyDown,
  onSubmit,
  placeholder = "Provide instructions...",
  disabled = false,
  loading = false,
  attachedFiles = [],
  onFilesChange,
  className = "",
  ...props 
}, ref) => {
  
  const internalRef = useRef(null);
  const textareaRef = ref || internalRef;
  const [selectedAgent, setSelectedAgent] = useState("Claude Sonnet 4");

  // Agent options
  const agents = [
    "Claude Sonnet 4",
    "GPT-4",
    "Gemini Pro",
    "Local AI"
  ];

  // Auto-resize functionality
  const adjustHeight = (element) => {
    if (element) {
      element.style.height = 'auto';
      const minHeight = 80;
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
    if (onChange) {
      onChange(e);
    }
  };

  // Adjust height when value changes
  useEffect(() => {
    if (textareaRef.current) {
      setTimeout(() => {
        adjustHeight(textareaRef.current);
      }, 0);
    }
  }, [value]);

  // Handle file attachment
  const handleAddFiles = () => {
    const input = document.createElement('input');
    input.type = 'file';
    input.multiple = true;
    input.accept = '.txt,.md,.py,.js,.json,.css,.html,.xml,.yaml,.yml,.pdf,.doc,.docx';
    input.onchange = (e) => {
      const files = Array.from(e.target.files);
      if (onFilesChange) {
        onFilesChange([...attachedFiles, ...files]);
      }
    };
    input.click();
  };

  // Handle paste from clipboard
  const handlePaste = async () => {
    try {
      const text = await navigator.clipboard.readText();
      if (text && onChange) {
        const syntheticEvent = {
          target: { value: value + (value ? '\n' : '') + text }
        };
        onChange(syntheticEvent);
      }
    } catch (err) {
      console.error('Failed to read clipboard:', err);
    }
  };

  // Handle file removal
  const removeFile = (index) => {
    if (onFilesChange) {
      onFilesChange(attachedFiles.filter((_, i) => i !== index));
    }
  };

  return (
    <div className={`chat-input-container ${className}`}>
      {/* Attachment Row */}
      <div className="flex items-center gap-2 mb-3">
        <button
          type="button"
          onClick={handleAddFiles}
          className="p-2 rounded-lg bg-[var(--background-secondary)] border border-[var(--border)] hover:bg-[var(--border)] transition-colors text-[var(--foreground)]"
          title="Attach files"
        >
          <span className="text-base font-medium">+</span>
        </button>
        
        {/* Attached files display */}
        <div className="flex flex-wrap gap-2 flex-1">
          {attachedFiles.map((file, idx) => (
            <div 
              key={idx}
              className="px-3 py-1 bg-[var(--card)] border border-[var(--border)] rounded-lg text-sm flex items-center gap-2 text-[var(--foreground)]"
            >
              <span>{file.name}</span>
              <button
                type="button"
                onClick={() => removeFile(idx)}
                className="text-[var(--foreground-muted)] hover:text-red-400 transition-colors"
              >
                ×
              </button>
            </div>
          ))}
        </div>
      </div>

      {/* Main Input Area */}
      <div className="bg-[var(--card)] border border-[var(--primary)] rounded-xl p-4">
        <textarea
          ref={textareaRef}
          value={value}
          onChange={handleInput}
          onKeyDown={onKeyDown}
          placeholder={placeholder}
          disabled={disabled}
          className="w-full bg-transparent text-[var(--foreground)] placeholder:text-[var(--foreground-muted)] resize-none outline-none border-none"
          style={{
            minHeight: '80px',
            maxHeight: '200px',
            lineHeight: '1.5',
            fontFamily: 'inherit',
            fontSize: '14px'
          }}
          {...props}
        />
      </div>

      {/* Bottom Controls */}
      <div className="flex items-center justify-between mt-3">
        {/* Agent Selector */}
        <select
          value={selectedAgent}
          onChange={(e) => setSelectedAgent(e.target.value)}
          className="px-3 py-2 bg-[var(--background-secondary)] border border-[var(--border)] rounded-lg text-[var(--foreground)] text-sm outline-none focus:border-[var(--primary)] transition-colors"
        >
          {agents.map(agent => (
            <option key={agent} value={agent}>{agent}</option>
          ))}
        </select>

        {/* Action Buttons */}
        <div className="flex items-center gap-2">
          <button
            type="button"
            onClick={handlePaste}
            className="px-3 py-2 rounded-lg bg-[var(--background-secondary)] border border-[var(--border)] hover:bg-[var(--border)] transition-colors text-[var(--foreground)] text-sm"
            title="Paste from clipboard"
          >
            Paste
          </button>
          
          <button
            type="button"
            className="p-2 rounded-lg bg-[var(--background-secondary)] border border-[var(--border)] hover:bg-[var(--border)] transition-colors text-[var(--foreground)]"
            title="Settings"
          >
            <span className="text-base">⋯</span>
          </button>
          
          <button
            type="button"
            className="p-2 rounded-lg bg-[var(--background-secondary)] border border-[var(--border)] hover:bg-[var(--border)] transition-colors text-[var(--foreground)]"
            title="Voice input"
          >
            <span className="text-base">●</span>
          </button>
          
          <button
            type="submit"
            onClick={onSubmit}
            disabled={disabled || loading || !value?.trim()}
            className="px-4 py-2 rounded-lg bg-[var(--primary)] text-white hover:bg-[var(--primary-hover)] disabled:opacity-50 disabled:cursor-not-allowed transition-colors font-medium"
          >
            {loading ? "..." : ">>"}
          </button>
        </div>
      </div>
    </div>
  );
});

ChatInput.displayName = 'ChatInput';

export default ChatInput;
