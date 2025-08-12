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
			{ name: 'Assistants', href: '/assistants' },
			{ name: 'Test UI Components', href: '/testui' }
		]
	},
	{
		name: 'Manage',
		items: [
			{ name: 'Projects', href: '/projects' },
			{ name: 'Agent Rules', href: '/rules' },
			{ name: 'Usage', href: '/usage' },
			{ name: 'API keys', href: '/api-keys' },
			{ name: 'Logs', href: '/logs' },
			{ name: 'Settings', href: '/settings' },
			{ name: 'Task Progress', href: '/progress' }
		]
	}
];

const Sidebar = () => {
	const pathname = usePathname();

	return (
		<aside
			className="flex flex-col w-64 flex-shrink-0 bg-[var(--background-secondary)] border-r border-t border-[var(--border)] text-[var(--foreground)]"
			style={{ 
				position: 'sticky', 
				top: 0, 
				height: 'calc(100vh - 2 * var(--layout-outer-padding))',
				paddingRight: 'var(--spacing-sm)',
				marginTop: 'var(--layout-padding)'
			}}
		>
			{/* Navigation */}
			<nav 
				className="flex flex-col flex-1 px-4 overflow-y-auto"
				style={{
					paddingTop: 'var(--spacing-lg)',
					paddingBottom: 'var(--spacing-lg)',
					gap: 'var(--spacing-xl)'
				}}
			>
				{menuItems.map((section, sectionIndex) => (
					<div key={section.name}>
						<h3 
							className="text-sm font-medium text-gray-400 uppercase tracking-wider"
							style={{ marginBottom: 'var(--spacing-md)' }}
						>
							{section.name}
						</h3>
						<div style={{ display: 'flex', flexDirection: 'column', gap: 'var(--spacing-xs)' }}>
							{section.items.map((item) => {
								const isActive = pathname === item.href;
								return (
									<Link
										key={item.name}
										href={item.href}
										className={`flex items-center gap-3 rounded-lg text-sm font-medium transition-colors ${
											isActive
												? 'bg-[var(--background-tertiary)] text-white'
												: 'text-[var(--foreground-secondary)] hover:bg-[var(--background-tertiary)] hover:text-white'
										}`}
										style={{ padding: 'var(--spacing-sm) var(--spacing-sm)' }}
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
