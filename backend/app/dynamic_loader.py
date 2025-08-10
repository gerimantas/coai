# dynamic_loader.py
"""
Stage II: 10.3 Dynamic project configs/rules/plans loading in backend

Provides dynamic loading of config, rules, and plans for a selected project.
"""
import os
import json
from typing import Optional

class DynamicProjectLoader:
    def __init__(self, projects_root: str = r'C:\ai_projects'):
        self.projects_root = os.path.abspath(projects_root)

    def get_config(self, project_name: str) -> Optional[dict]:
        config_path = os.path.join(self.projects_root, project_name, 'config.json')
        if os.path.exists(config_path):
            with open(config_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        return None

    def get_rules(self, project_name: str) -> Optional[str]:
        rules_path = os.path.join(self.projects_root, project_name, 'rules.txt')
        if os.path.exists(rules_path):
            with open(rules_path, 'r', encoding='utf-8') as f:
                return f.read()
        return None

    def get_plan(self, project_name: str) -> Optional[str]:
        plan_path = os.path.join(self.projects_root, project_name, 'plan.md')
        if os.path.exists(plan_path):
            with open(plan_path, 'r', encoding='utf-8') as f:
                return f.read()
        return None
