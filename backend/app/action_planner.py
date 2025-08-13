"""
Action Plan Generation System
Breaks down user requests into step-by-step actionable plans
"""
import json
import os
from datetime import datetime
from typing import Dict, List, Optional, Any
from dataclasses import dataclass, asdict
from enum import Enum

class TaskStatus(Enum):
    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    BLOCKED = "blocked"
    CANCELLED = "cancelled"

class TaskPriority(Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"

@dataclass
class Task:
    """Individual task within an action plan"""
    id: str
    title: str
    description: str
    status: TaskStatus = TaskStatus.PENDING
    priority: TaskPriority = TaskPriority.MEDIUM
    estimated_time: int = 30  # minutes
    dependencies: List[str] = None  # task IDs
    tags: List[str] = None
    created_at: str = None
    completed_at: Optional[str] = None
    
    def __post_init__(self):
        if self.dependencies is None:
            self.dependencies = []
        if self.tags is None:
            self.tags = []
        if self.created_at is None:
            self.created_at = datetime.now().isoformat()

@dataclass
class ActionPlan:
    """Complete action plan with multiple tasks"""
    id: str
    title: str
    description: str
    tasks: List[Task]
    project_path: Optional[str] = None
    created_at: str = None
    updated_at: str = None
    total_estimated_time: int = 0
    completion_percentage: float = 0.0
    
    def __post_init__(self):
        if self.created_at is None:
            self.created_at = datetime.now().isoformat()
        if self.updated_at is None:
            self.updated_at = self.created_at
        self.calculate_metrics()
    
    def calculate_metrics(self):
        """Calculate plan metrics"""
        self.total_estimated_time = sum(task.estimated_time for task in self.tasks)
        completed_tasks = [task for task in self.tasks if task.status == TaskStatus.COMPLETED]
        self.completion_percentage = (len(completed_tasks) / len(self.tasks) * 100) if self.tasks else 0.0

class ActionPlanner:
    """AI-powered action plan generation and management"""
    
    def __init__(self, storage_path: str = None):
        self.storage_path = storage_path or os.path.join('.coai', 'plans')
        os.makedirs(self.storage_path, exist_ok=True)
    
    def generate_plan(self, user_request: str, project_context: Dict[str, Any] = None) -> ActionPlan:
        """
        Generate an action plan from user request using AI analysis
        """
        # Analyze the request to determine complexity and scope
        plan_analysis = self._analyze_request(user_request, project_context)
        
        # Generate tasks based on analysis
        tasks = self._generate_tasks(plan_analysis)
        
        # Create action plan
        plan_id = f"plan_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        plan = ActionPlan(
            id=plan_id,
            title=plan_analysis.get('title', 'Generated Action Plan'),
            description=plan_analysis.get('description', user_request),
            tasks=tasks,
            project_path=project_context.get('path') if project_context else None
        )
        
        # Save plan
        self.save_plan(plan)
        
        return plan
    
    def _analyze_request(self, request: str, context: Dict[str, Any] = None) -> Dict[str, Any]:
        """Analyze user request to determine plan structure"""
        
        # Simple keyword-based analysis (in production, would use AI)
        analysis = {
            'title': 'Custom Development Plan',
            'description': request,
            'complexity': 'medium',
            'estimated_duration': 120,  # minutes
            'categories': []
        }
        
        # Detect common patterns
        request_lower = request.lower()
        
        if any(word in request_lower for word in ['api', 'endpoint', 'backend', 'server', 'authentication', 'auth', 'login']):
            analysis['categories'].append('backend')
        
        if any(word in request_lower for word in ['ui', 'frontend', 'component', 'page', 'web', 'application', 'app', 'interface']):
            analysis['categories'].append('frontend')
        
        if any(word in request_lower for word in ['test', 'testing', 'unit test']):
            analysis['categories'].append('testing')
        
        if any(word in request_lower for word in ['deploy', 'production', 'build']):
            analysis['categories'].append('deployment')
        
        if any(word in request_lower for word in ['database', 'data', 'model', 'user', 'auth']):
            analysis['categories'].append('database')
        
        # Determine complexity
        if len(request.split()) > 50 or 'complex' in request_lower:
            analysis['complexity'] = 'high'
            analysis['estimated_duration'] = 240
        elif len(request.split()) < 10:
            analysis['complexity'] = 'low'
            analysis['estimated_duration'] = 60
        
        return analysis
    
    def _generate_tasks(self, analysis: Dict[str, Any]) -> List[Task]:
        """Generate specific tasks based on analysis"""
        tasks = []
        task_counter = 1
        
        categories = analysis.get('categories', [])
        complexity = analysis.get('complexity', 'medium')
        
        # Common initial tasks
        tasks.append(Task(
            id=f"task_{task_counter}",
            title="Requirements Analysis",
            description="Analyze and document detailed requirements",
            priority=TaskPriority.HIGH,
            estimated_time=30,
            tags=['planning', 'analysis']
        ))
        task_counter += 1
        
        # Category-specific tasks
        if 'backend' in categories:
            tasks.extend([
                Task(
                    id=f"task_{task_counter}",
                    title="Backend API Design",
                    description="Design API endpoints and data structures",
                    priority=TaskPriority.HIGH,
                    estimated_time=45,
                    dependencies=['task_1'],
                    tags=['backend', 'api']
                ),
                Task(
                    id=f"task_{task_counter + 1}",
                    title="Implement Backend Logic",
                    description="Code the backend implementation",
                    priority=TaskPriority.MEDIUM,
                    estimated_time=90,
                    dependencies=[f'task_{task_counter}'],
                    tags=['backend', 'implementation']
                )
            ])
            task_counter += 2
        
        if 'frontend' in categories:
            tasks.extend([
                Task(
                    id=f"task_{task_counter}",
                    title="UI/UX Design",
                    description="Design user interface and experience",
                    priority=TaskPriority.MEDIUM,
                    estimated_time=60,
                    dependencies=['task_1'],
                    tags=['frontend', 'design']
                ),
                Task(
                    id=f"task_{task_counter + 1}",
                    title="Frontend Implementation",
                    description="Implement frontend components and logic",
                    priority=TaskPriority.MEDIUM,
                    estimated_time=90,
                    dependencies=[f'task_{task_counter}'],
                    tags=['frontend', 'implementation']
                )
            ])
            task_counter += 2
        
        if 'testing' in categories:
            tasks.append(Task(
                id=f"task_{task_counter}",
                title="Testing Implementation",
                description="Write and execute comprehensive tests",
                priority=TaskPriority.MEDIUM,
                estimated_time=60,
                dependencies=[t.id for t in tasks if 'implementation' in t.tags],
                tags=['testing', 'quality']
            ))
            task_counter += 1
        
        # Always add integration and deployment tasks for complex projects
        if complexity in ['medium', 'high']:
            tasks.extend([
                Task(
                    id=f"task_{task_counter}",
                    title="Integration Testing",
                    description="Test integration between components",
                    priority=TaskPriority.MEDIUM,
                    estimated_time=45,
                    dependencies=[t.id for t in tasks if 'implementation' in t.tags],
                    tags=['testing', 'integration']
                ),
                Task(
                    id=f"task_{task_counter + 1}",
                    title="Documentation",
                    description="Create comprehensive documentation",
                    priority=TaskPriority.LOW,
                    estimated_time=30,
                    tags=['documentation']
                )
            ])
        
        return tasks
    
    def save_plan(self, plan: ActionPlan) -> str:
        """Save action plan to storage"""
        file_path = os.path.join(self.storage_path, f"{plan.id}.json")
        
        # Convert to JSON-serializable format
        plan_data = asdict(plan)
        # Convert enums to strings
        for task in plan_data['tasks']:
            if isinstance(task['status'], TaskStatus):
                task['status'] = task['status'].value
            if isinstance(task['priority'], TaskPriority):
                task['priority'] = task['priority'].value
        
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(plan_data, f, indent=2, ensure_ascii=False)
        
        return file_path
    
    def load_plan(self, plan_id: str) -> Optional[ActionPlan]:
        """Load action plan from storage"""
        file_path = os.path.join(self.storage_path, f"{plan_id}.json")
        
        if not os.path.exists(file_path):
            return None
        
        with open(file_path, 'r', encoding='utf-8') as f:
            plan_data = json.load(f)
        
        # Convert string enums back to enum objects
        tasks = []
        for task_data in plan_data['tasks']:
            task_data['status'] = TaskStatus(task_data['status'])
            task_data['priority'] = TaskPriority(task_data['priority'])
            tasks.append(Task(**task_data))
        
        plan_data['tasks'] = tasks
        return ActionPlan(**plan_data)
    
    def update_task_status(self, plan_id: str, task_id: str, new_status: TaskStatus) -> bool:
        """Update status of a specific task"""
        plan = self.load_plan(plan_id)
        if not plan:
            return False
        
        for task in plan.tasks:
            if task.id == task_id:
                task.status = new_status
                if new_status == TaskStatus.COMPLETED:
                    task.completed_at = datetime.now().isoformat()
                break
        else:
            return False
        
        plan.updated_at = datetime.now().isoformat()
        plan.calculate_metrics()
        self.save_plan(plan)
        return True
    
    def get_plan_progress(self, plan_id: str) -> Dict[str, Any]:
        """Get detailed progress information for a plan"""
        plan = self.load_plan(plan_id)
        if not plan:
            return {}
        
        status_counts = {}
        for status in TaskStatus:
            status_counts[status.value] = len([t for t in plan.tasks if t.status == status])
        
        return {
            'plan_id': plan.id,
            'title': plan.title,
            'completion_percentage': plan.completion_percentage,
            'total_tasks': len(plan.tasks),
            'total_estimated_time': plan.total_estimated_time,
            'status_breakdown': status_counts,
            'next_tasks': [
                {'id': t.id, 'title': t.title, 'priority': t.priority.value}
                for t in plan.tasks
                if t.status == TaskStatus.PENDING
            ][:3]  # Next 3 pending tasks
        }
    
    def list_plans(self, project_path: str = None) -> List[Dict[str, Any]]:
        """List all available plans, optionally filtered by project"""
        plans = []
        
        if not os.path.exists(self.storage_path):
            return plans
        
        for file in os.listdir(self.storage_path):
            if file.endswith('.json'):
                plan_id = file[:-5]  # Remove .json extension
                plan = self.load_plan(plan_id)
                if plan:
                    if project_path is None or plan.project_path == project_path:
                        plans.append({
                            'id': plan.id,
                            'title': plan.title,
                            'description': plan.description,
                            'completion_percentage': plan.completion_percentage,
                            'total_tasks': len(plan.tasks),
                            'created_at': plan.created_at,
                            'updated_at': plan.updated_at
                        })
        
        return sorted(plans, key=lambda x: x['updated_at'], reverse=True)
