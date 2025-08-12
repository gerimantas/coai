"use client";
import { useEffect, useState } from "react";
import PageContainer from "@/components/ui/PageContainer";

const TASKS = [
	{ id: "12.2", name: "Step progress tracking" },
	{ id: "12.3", name: "UI progress filters" },
	{ id: "12.4", name: "Integration with plan copy/markers" },
	{ id: "12.5", name: "Multi-step plan tests" },
	{ id: "13.1", name: "Track API calls, tokens, costs" },
	{ id: "13.2", name: "UI usage views" },
	{ id: "13.3", name: "Budget limits" },
	{ id: "13.4", name: "UI alerts on thresholds" },
	{ id: "13.5", name: "Usage & alerts tests" },
	{ id: "14.1", name: "Error logs with context" },
	{ id: "14.2", name: "UI filtering by date/project/type" },
	{ id: "14.3", name: "Frequent issues analysis" },
	{ id: "14.4", name: "Export reports to CSV/JSON" },
	{ id: "14.5", name: "Log/filters/export tests" },
	{ id: "15.1", name: "Integration tests for multi-project" },
	{ id: "15.2", name: "Performance/load tests" },
	{ id: "15.3", name: "Security tests" },
	{ id: "15.4", name: "CI automation" }
];

export default function ProgressPage() {
	const [progress, setProgress] = useState({});
	const [loading, setLoading] = useState(true);

	useEffect(() => {
		fetch("/api/progress")
			.then((res) => res.json())
			.then((data) => {
				setProgress(data);
				setLoading(false);
			});
	}, []);

	return (
		<PageContainer title="Task Progress" subtitle="Overview of planned tasks and their current status.">
			<div className="max-h-[60vh] overflow-y-auto pr-1">
				<div className="grid grid-cols-[1fr_auto] gap-4 px-4 py-2 text-xs uppercase tracking-wide text-[var(--foreground-muted)] sticky top-0 bg-[var(--card)] border-b border-[var(--border)]">
					<span>Task</span>
					<span>Status</span>
				</div>
				<ul className="space-y-2">
				{TASKS.map((task) => (
					<li
						key={task.id}
								className="flex items-center justify-between gap-4 px-4 py-2 rounded-lg border border-[var(--border)] bg-[var(--background-secondary)] odd:bg-[var(--background-light)] hover:bg-[var(--background-tertiary)] min-h-[40px]"
					>
							<span className="text-sm text-[var(--foreground)]">
							{task.name}
						</span>
						<span
							className={`text-xs md:text-sm px-3 py-1 rounded font-medium border ${
								progress[task.id] === "Completed"
									? "bg-green-700/40 text-green-100 border-green-700"
									: progress[task.id] === "In Progress"
									? "bg-yellow-700/40 text-yellow-100 border-yellow-700"
									: "bg-gray-700/40 text-gray-200 border-gray-700"
							}`}
						>
							{progress[task.id] || "Not Started"}
						</span>
					</li>
				))}
				</ul>
			</div>
		</PageContainer>
	);
}
