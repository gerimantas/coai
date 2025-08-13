# rules_loader.py
"""
Stage IV: Enhanced Rules System
Advanced rules loader with validation, versioning, and per-project overrides
"""
import os
import json
import shutil
from datetime import datetime
from typing import Dict, List, Optional, Union
from dataclasses import dataclass, asdict
from pathlib import Path

# Configuration
GLOBAL_RULES_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../.coai/rules'))
BACKUP_DIR = os.path.join(GLOBAL_RULES_PATH, 'backups')
VERSIONS_DIR = os.path.join(GLOBAL_RULES_PATH, 'versions')

# Legacy compatibility
RULES_PATH = os.path.join(GLOBAL_RULES_PATH, 'agent_rules.txt')

@dataclass
class RuleSet:
    """Represents a complete rule set with metadata"""
    global_rules: List[str]
    agent_rules: Dict[str, List[str]]
    version: str
    created_at: str
    project_path: Optional[str] = None
    description: Optional[str] = None

@dataclass
class RuleValidationResult:
    """Result of rule validation"""
    is_valid: bool
    errors: List[str]
    warnings: List[str]

class EnhancedRulesLoader:
    """Enhanced rules loader with validation, versioning, and project overrides"""
    
    def __init__(self):
        self.ensure_directories()
    
    def ensure_directories(self):
        """Ensure all required directories exist"""
        for dir_path in [GLOBAL_RULES_PATH, BACKUP_DIR, VERSIONS_DIR]:
            os.makedirs(dir_path, exist_ok=True)
    
    def load_rules(self, project_path: Optional[str] = None) -> RuleSet:
        """
        Load rules with project-specific overrides
        
        Args:
            project_path: Optional path to project for project-specific rules
            
        Returns:
            RuleSet with merged global and project-specific rules
        """
        # Load global rules first
        global_rules = self._load_global_rules()
        
        # Load project-specific rules if project path provided
        if project_path:
            project_rules = self._load_project_rules(project_path)
            if project_rules:
                # Merge project rules with global rules
                return self._merge_rules(global_rules, project_rules)
        
        return global_rules
    
    def _load_global_rules(self) -> RuleSet:
        """Load global rules from default location"""
        rules_file = os.path.join(GLOBAL_RULES_PATH, 'agent_rules.txt')
        return self._parse_rules_file(rules_file)
    
    def _load_project_rules(self, project_path: str) -> Optional[RuleSet]:
        """Load project-specific rules"""
        project_rules_file = os.path.join(project_path, '.coai', 'rules', 'agent_rules.txt')
        if os.path.exists(project_rules_file):
            return self._parse_rules_file(project_rules_file, project_path)
        return None
    
    def _parse_rules_file(self, file_path: str, project_path: Optional[str] = None) -> RuleSet:
        """Parse rules file into RuleSet object"""
        global_rules = []
        agent_rules = {}
        current_agent = None
        
        if not os.path.exists(file_path):
            return RuleSet(
                global_rules=[],
                agent_rules={},
                version="1.0.0",
                created_at=datetime.now().isoformat(),
                project_path=project_path
            )
        
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if line.startswith('[agent:') and line.endswith(']'):
                    current_agent = line[7:-1]
                    agent_rules[current_agent] = []
                elif current_agent and line and not line.startswith('#'):
                    agent_rules[current_agent].append(line)
                elif not current_agent and line and not line.startswith('#'):
                    global_rules.append(line)
        
        return RuleSet(
            global_rules=global_rules,
            agent_rules=agent_rules,
            version="1.0.0",
            created_at=datetime.now().isoformat(),
            project_path=project_path
        )
    
    def _merge_rules(self, global_rules: RuleSet, project_rules: RuleSet) -> RuleSet:
        """Merge project rules with global rules (project takes precedence)"""
        merged_global = global_rules.global_rules + project_rules.global_rules
        merged_agents = global_rules.agent_rules.copy()
        
        # Merge agent-specific rules
        for agent, rules in project_rules.agent_rules.items():
            if agent in merged_agents:
                merged_agents[agent].extend(rules)
            else:
                merged_agents[agent] = rules
        
        return RuleSet(
            global_rules=merged_global,
            agent_rules=merged_agents,
            version=f"{global_rules.version}+{project_rules.version}",
            created_at=datetime.now().isoformat(),
            project_path=project_rules.project_path,
            description="Merged global and project rules"
        )
    
    def validate_rules(self, rules: RuleSet) -> RuleValidationResult:
        """Validate rules for syntax and content"""
        errors = []
        warnings = []
        
        # Check for empty rules
        if not rules.global_rules and not rules.agent_rules:
            warnings.append("No rules defined")
        
        # Validate agent names
        valid_agents = ['openai', 'copilot', 'claude', 'gemini']
        for agent in rules.agent_rules.keys():
            if agent not in valid_agents:
                warnings.append(f"Unknown agent: {agent}")
        
        # Check rule length
        all_rules = rules.global_rules + [rule for agent_rules in rules.agent_rules.values() for rule in agent_rules]
        for rule in all_rules:
            if len(rule) > 500:
                warnings.append(f"Rule may be too long: {rule[:50]}...")
            if len(rule.strip()) < 10:
                warnings.append(f"Rule may be too short: {rule}")
        
        return RuleValidationResult(
            is_valid=len(errors) == 0,
            errors=errors,
            warnings=warnings
        )
    
    def save_rules_version(self, rules: RuleSet, version: str, description: str = "") -> str:
        """Save rules as a versioned backup"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        version_file = os.path.join(VERSIONS_DIR, f"rules_v{version}_{timestamp}.json")
        
        rules_data = asdict(rules)
        rules_data['version'] = version
        rules_data['description'] = description
        rules_data['saved_at'] = datetime.now().isoformat()
        
        with open(version_file, 'w', encoding='utf-8') as f:
            json.dump(rules_data, f, indent=2, ensure_ascii=False)
        
        return version_file
    
    def create_backup(self, source_path: Optional[str] = None) -> str:
        """Create backup of current rules"""
        if source_path is None:
            source_path = os.path.join(GLOBAL_RULES_PATH, 'agent_rules.txt')
        
        if not os.path.exists(source_path):
            raise FileNotFoundError(f"Rules file not found: {source_path}")
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_file = os.path.join(BACKUP_DIR, f"agent_rules_backup_{timestamp}.txt")
        
        shutil.copy2(source_path, backup_file)
        return backup_file
    
    def restore_from_backup(self, backup_file: str, target_path: Optional[str] = None) -> bool:
        """Restore rules from backup"""
        if not os.path.exists(backup_file):
            return False
        
        if target_path is None:
            target_path = os.path.join(GLOBAL_RULES_PATH, 'agent_rules.txt')
        
        # Create backup of current rules before restoring
        if os.path.exists(target_path):
            self.create_backup(target_path)
        
        shutil.copy2(backup_file, target_path)
        return True
    
    def list_versions(self) -> List[Dict]:
        """List all available rule versions"""
        versions = []
        
        if os.path.exists(VERSIONS_DIR):
            for file in os.listdir(VERSIONS_DIR):
                if file.endswith('.json'):
                    file_path = os.path.join(VERSIONS_DIR, file)
                    try:
                        with open(file_path, 'r', encoding='utf-8') as f:
                            data = json.load(f)
                            versions.append({
                                'file': file,
                                'version': data.get('version', 'unknown'),
                                'created_at': data.get('saved_at', 'unknown'),
                                'description': data.get('description', ''),
                                'path': file_path
                            })
                    except Exception:
                        continue
        
        return sorted(versions, key=lambda x: x['created_at'], reverse=True)


# Legacy compatibility function
def load_agent_rules(path: str = None) -> Dict[str, Union[List[str], Dict]]:
    """
    Legacy compatibility function
    Returns rules in the old format for backward compatibility
    """
    loader = EnhancedRulesLoader()
    rules = loader.load_rules()
    
    return {
        'global': rules.global_rules,
        'agents': rules.agent_rules
    }
