"use client";
import { useEffect, useState } from "react";

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
		<div className="min-h-screen bg-[#0f0f0f] text-white">
			<div className="mt-[2%] mr-[2%] px-6 py-6">
				<h1 className="text-lg font-medium mb-6">Task Progress</h1>
				<div className="bg-[#1a1a1a] border border-[#2a2a2a] rounded-lg p-6">
					<ul className="space-y-2">
						{TASKS.map((task) => (
							<li
								key={task.id}
								className="flex items-center justify-between px-4 py-2 rounded-lg border border-[#2a2a2a] bg-[#222]"
							>
								<span className="text-base text-white font-normal">
									{task.name}
								</span>
								<span
									className={`text-sm px-3 py-1 rounded font-medium ${
										progress[task.id] === "Completed"
											? "bg-green-700 text-white"
											: progress[task.id] === "In Progress"
											? "bg-yellow-700 text-white"
											: "bg-gray-700 text-gray-300"
									}`}
								>
									{progress[task.id] || "Not Started"}
								</span>
							</li>
						))}
					</ul>
				</div>
			</div>
		</div>
	);
}
