"""
COAI Usage Analytics and Tracking System
Tracks API calls, token usage, costs, and performance metrics
"""

import os
import json
import time
from datetime import datetime, date
from typing import Dict, Any, List, Optional
from dataclasses import dataclass, asdict
import threading
from pathlib import Path

@dataclass
class UsageEntry:
    """Single usage tracking entry"""
    timestamp: str
    request_id: str
    agent_type: str
    project: str
    file: str
    message_length: int
    response_length: int
    tokens_used: int
    prompt_tokens: int
    completion_tokens: int
    model: str
    cost_estimate: float
    response_time: float
    status: str
    real_ai: bool
    error: Optional[str] = None

@dataclass
class DailySummary:
    """Daily usage summary"""
    date: str
    total_requests: int
    successful_requests: int
    failed_requests: int
    total_tokens: int
    total_cost: float
    avg_response_time: float
    projects_used: List[str]
    most_used_agent: str
    real_ai_requests: int

class UsageTracker:
    """
    Comprehensive usage tracking for COAI system
    """
    
    def __init__(self):
        self.usage_dir = self._setup_usage_directory()
        self.current_session = []
        self.lock = threading.Lock()
        self._load_today_data()
    
    def _setup_usage_directory(self) -> Path:
        """Setup usage tracking directory structure"""
        base_dir = Path(__file__).parent.parent / '.coai' / 'usage'
        base_dir.mkdir(parents=True, exist_ok=True)
        
        # Create subdirectories
        (base_dir / 'daily').mkdir(exist_ok=True)
        (base_dir / 'monthly').mkdir(exist_ok=True)
        (base_dir / 'sessions').mkdir(exist_ok=True)
        
        return base_dir
    
    def _load_today_data(self):
        """Load today's usage data"""
        today = date.today().isoformat()
        today_file = self.usage_dir / 'daily' / f'{today}.json'
        
        if today_file.exists():
            try:
                with open(today_file, 'r') as f:
                    data = json.load(f)
                    self.current_session = [UsageEntry(**entry) for entry in data.get('entries', [])]
            except Exception as e:
                print(f"Warning: Could not load today's usage data: {e}")
                self.current_session = []
        else:
            self.current_session = []
    
    def track_request(
        self,
        request_id: str,
        agent_type: str,
        project: str,
        file: str,
        message: str,
        response: str,
        tokens_data: Dict[str, Any],
        response_time: float,
        status: str,
        real_ai: bool,
        error: str = None
    ) -> UsageEntry:
        """Track a single API request"""
        
        # Calculate cost estimate (basic OpenAI pricing)
        cost_estimate = self._calculate_cost(tokens_data, agent_type, real_ai)
        
        # Create usage entry
        entry = UsageEntry(
            timestamp=datetime.now().isoformat(),
            request_id=request_id,
            agent_type=agent_type,
            project=project,
            file=file,
            message_length=len(message),
            response_length=len(response),
            tokens_used=tokens_data.get('total_tokens', 0),
            prompt_tokens=tokens_data.get('prompt_tokens', 0),
            completion_tokens=tokens_data.get('completion_tokens', 0),
            model=tokens_data.get('model', 'unknown'),
            cost_estimate=cost_estimate,
            response_time=response_time,
            status=status,
            real_ai=real_ai,
            error=error
        )
        
        # Thread-safe addition
        with self.lock:
            self.current_session.append(entry)
            self._save_today_data()
        
        return entry
    
    def _calculate_cost(self, tokens_data: Dict[str, Any], agent_type: str, real_ai: bool) -> float:
        """Calculate estimated cost for the request"""
        
        if not real_ai or agent_type != 'openai':
            return 0.0  # Mock responses are free
        
        model = tokens_data.get('model', 'gpt-3.5-turbo')
        prompt_tokens = tokens_data.get('prompt_tokens', 0)
        completion_tokens = tokens_data.get('completion_tokens', 0)
        
        # Basic OpenAI pricing (as of 2024 - approximate)
        if 'gpt-4' in model.lower():
            prompt_cost = prompt_tokens * 0.00003  # $0.03 per 1K tokens
            completion_cost = completion_tokens * 0.00006  # $0.06 per 1K tokens
        elif 'gpt-3.5-turbo' in model.lower():
            prompt_cost = prompt_tokens * 0.0000015  # $0.0015 per 1K tokens
            completion_cost = completion_tokens * 0.000002  # $0.002 per 1K tokens
        else:
            # Default pricing
            prompt_cost = prompt_tokens * 0.000001
            completion_cost = completion_tokens * 0.000001
        
        return prompt_cost + completion_cost
    
    def _save_today_data(self):
        """Save today's usage data to file"""
        today = date.today().isoformat()
        today_file = self.usage_dir / 'daily' / f'{today}.json'
        
        # Create daily summary
        summary = self._generate_daily_summary()
        
        data = {
            'date': today,
            'summary': asdict(summary),
            'entries': [asdict(entry) for entry in self.current_session]
        }
        
        try:
            with open(today_file, 'w') as f:
                json.dump(data, f, indent=2)
        except Exception as e:
            print(f"Warning: Could not save usage data: {e}")
    
    def _generate_daily_summary(self) -> DailySummary:
        """Generate summary for current day"""
        
        if not self.current_session:
            return DailySummary(
                date=date.today().isoformat(),
                total_requests=0,
                successful_requests=0,
                failed_requests=0,
                total_tokens=0,
                total_cost=0.0,
                avg_response_time=0.0,
                projects_used=[],
                most_used_agent="none",
                real_ai_requests=0
            )
        
        successful = [e for e in self.current_session if e.status == 'success']
        failed = [e for e in self.current_session if e.status != 'success']
        real_ai_entries = [e for e in self.current_session if e.real_ai]
        
        # Calculate metrics
        total_tokens = sum(e.tokens_used for e in self.current_session)
        total_cost = sum(e.cost_estimate for e in self.current_session)
        avg_response_time = sum(e.response_time for e in self.current_session) / len(self.current_session)
        
        # Find most used project and agent
        projects = list(set(e.project for e in self.current_session))
        agent_counts = {}
        for entry in self.current_session:
            agent_counts[entry.agent_type] = agent_counts.get(entry.agent_type, 0) + 1
        
        most_used_agent = max(agent_counts.items(), key=lambda x: x[1])[0] if agent_counts else "none"
        
        return DailySummary(
            date=date.today().isoformat(),
            total_requests=len(self.current_session),
            successful_requests=len(successful),
            failed_requests=len(failed),
            total_tokens=total_tokens,
            total_cost=total_cost,
            avg_response_time=avg_response_time,
            projects_used=projects,
            most_used_agent=most_used_agent,
            real_ai_requests=len(real_ai_entries)
        )
    
    def get_daily_summary(self, target_date: str = None) -> Optional[DailySummary]:
        """Get summary for a specific date"""
        
        if target_date is None:
            return self._generate_daily_summary()
        
        daily_file = self.usage_dir / 'daily' / f'{target_date}.json'
        if not daily_file.exists():
            return None
        
        try:
            with open(daily_file, 'r') as f:
                data = json.load(f)
                return DailySummary(**data['summary'])
        except Exception as e:
            print(f"Error loading daily summary: {e}")
            return None
    
    def get_usage_stats(self, days: int = 7) -> Dict[str, Any]:
        """Get usage statistics for the last N days"""
        
        stats = {
            'period_days': days,
            'daily_summaries': [],
            'totals': {
                'requests': 0,
                'tokens': 0,
                'cost': 0.0,
                'real_ai_requests': 0
            },
            'averages': {
                'requests_per_day': 0.0,
                'tokens_per_day': 0.0,
                'cost_per_day': 0.0,
                'response_time': 0.0
            },
            'trends': {
                'most_active_projects': [],
                'agent_usage': {},
                'peak_hours': []
            }
        }
        
        # Collect data for the last N days
        from datetime import timedelta
        today = date.today()
        
        valid_days = 0
        total_response_times = []
        project_counts = {}
        agent_counts = {}
        hourly_usage = [0] * 24
        
        for i in range(days):
            check_date = today - timedelta(days=i)
            daily_summary = self.get_daily_summary(check_date.isoformat())
            
            if daily_summary and daily_summary.total_requests > 0:
                valid_days += 1
                stats['daily_summaries'].append(asdict(daily_summary))
                
                # Update totals
                stats['totals']['requests'] += daily_summary.total_requests
                stats['totals']['tokens'] += daily_summary.total_tokens
                stats['totals']['cost'] += daily_summary.total_cost
                stats['totals']['real_ai_requests'] += daily_summary.real_ai_requests
                
                # Collect data for trends
                for project in daily_summary.projects_used:
                    project_counts[project] = project_counts.get(project, 0) + 1
                
                agent_counts[daily_summary.most_used_agent] = agent_counts.get(
                    daily_summary.most_used_agent, 0
                ) + 1
                
                total_response_times.append(daily_summary.avg_response_time)
        
        # Calculate averages
        if valid_days > 0:
            stats['averages']['requests_per_day'] = stats['totals']['requests'] / valid_days
            stats['averages']['tokens_per_day'] = stats['totals']['tokens'] / valid_days
            stats['averages']['cost_per_day'] = stats['totals']['cost'] / valid_days
            
            if total_response_times:
                stats['averages']['response_time'] = sum(total_response_times) / len(total_response_times)
        
        # Generate trends
        stats['trends']['most_active_projects'] = sorted(
            project_counts.items(), key=lambda x: x[1], reverse=True
        )[:5]
        
        stats['trends']['agent_usage'] = agent_counts
        
        return stats
    
    def export_usage_data(self, start_date: str, end_date: str, format: str = 'json') -> str:
        """Export usage data for a date range"""
        
        from datetime import datetime as dt
        start = dt.fromisoformat(start_date).date()
        end = dt.fromisoformat(end_date).date()
        
        export_data = {
            'export_info': {
                'start_date': start_date,
                'end_date': end_date,
                'export_timestamp': datetime.now().isoformat(),
                'format': format
            },
            'daily_data': []
        }
        
        current = start
        while current <= end:
            daily_file = self.usage_dir / 'daily' / f'{current.isoformat()}.json'
            if daily_file.exists():
                try:
                    with open(daily_file, 'r') as f:
                        daily_data = json.load(f)
                        export_data['daily_data'].append(daily_data)
                except Exception as e:
                    print(f"Warning: Could not load data for {current}: {e}")
            
            from datetime import timedelta
            current += timedelta(days=1)
        
        # Save export file
        export_filename = f"usage_export_{start_date}_to_{end_date}.{format}"
        export_path = self.usage_dir / export_filename
        
        if format == 'json':
            with open(export_path, 'w') as f:
                json.dump(export_data, f, indent=2)
        elif format == 'csv':
            import csv
            csv_path = self.usage_dir / f"usage_export_{start_date}_to_{end_date}.csv"
            
            with open(csv_path, 'w', newline='') as f:
                if export_data['daily_data']:
                    # Flatten all entries for CSV
                    all_entries = []
                    for daily in export_data['daily_data']:
                        all_entries.extend(daily.get('entries', []))
                    
                    if all_entries:
                        writer = csv.DictWriter(f, fieldnames=all_entries[0].keys())
                        writer.writeheader()
                        writer.writerows(all_entries)
            
            return str(csv_path)
        
        return str(export_path)

# Global usage tracker instance
usage_tracker = UsageTracker()
