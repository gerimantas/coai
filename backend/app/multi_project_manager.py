# multi_project_manager.py
"""
Stage II: 10.1 Multi-project management & migration

Provides management for multiple projects, including listing, selecting, and migrating projects.
"""
import os
from typing import List

PROJECTS_DIR = os.path.join(os.path.dirname(__file__), '../../projects')

class MultiProjectManager:
    def __init__(self, projects_dir: str = PROJECTS_DIR):
        self.projects_dir = os.path.abspath(projects_dir)

    def list_projects(self) -> List[str]:
        """Return a list of available project names."""
        if not os.path.exists(self.projects_dir):
            return []
        return [d for d in os.listdir(self.projects_dir) if os.path.isdir(os.path.join(self.projects_dir, d))]

    def select_project(self, name: str) -> str:
        """Select a project by name and return its path."""
        path = os.path.join(self.projects_dir, name)
        if os.path.exists(path):
            return path
        raise FileNotFoundError(f"Project '{name}' not found.")

    def migrate_project(self, src: str, dest: str) -> bool:
        """Migrate a project from src to dest directory."""
        import shutil
        if not os.path.exists(src):
            raise FileNotFoundError(f"Source project '{src}' not found.")
        shutil.copytree(src, dest)
        return True
