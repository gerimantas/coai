"use client";
import React from 'react';
import { usePathname } from 'next/navigation';
import Link from 'next/link';

const menuItems = [
  { 
    name: 'Create', 
    items: [
      { name: 'Chat', href: '/chat' },
      { name: 'Files', href: '/files' },
      { name: 'Assistants', href: '/assistants' }
    ]
  },
  {
    name: 'Manage',
    items: [
      { name: 'Projects', href: '/projects' },
      { name: 'Usage', href: '/usage' },
      { name: 'API keys', href: '/api-keys' },
      { name: 'Logs', href: '/logs' },
      { name: 'Settings', href: '/settings' }
    ]
  }
];

const Sidebar = () => {
  const pathname = usePathname();

  return (
    <aside className="flex flex-col bg-[#1a1a1a] text-white border-r border-[#2a2a2a] ml-[2%] mt-[2%] mr-[2%] rounded-lg" style={{width: '21%', height: 'calc(100vh - 4%)'}}>
      {/* Navigation */}
      <nav className="flex flex-col flex-1 px-6 py-6 space-y-8">
        {menuItems.map((section, sectionIndex) => (
          <div key={section.name}>
            <h3 className="text-sm font-medium text-gray-400 uppercase tracking-wider mb-4">
              {section.name}
            </h3>
            <div className="space-y-1">
              {section.items.map((item) => {
                const isActive = pathname === item.href;
                return (
                  <Link
                    key={item.name}
                    href={item.href}
                    className={`flex items-center gap-3 px-4 py-3 rounded-lg text-sm font-medium transition-colors ${
                      isActive 
                        ? 'bg-[#2a2a2a] text-white' 
                        : 'text-gray-300 hover:bg-[#2a2a2a] hover:text-white'
                    }`}
                  >
                    {item.name}
                  </Link>
                );
              })}
            </div>
          </div>
        ))}
      </nav>
    </aside>
  );
};

export default Sidebar;
