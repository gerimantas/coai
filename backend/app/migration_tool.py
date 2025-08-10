# migration_tool.py
"""
Stage II: 10.4 Migration tool (single-project → multi-project)

Migrates a single-project structure to a multi-project structure in C:\ai_projects.
"""
import os
import shutil
from typing import Optional

def migrate_single_to_multi(src_dir: str, project_name: str, dest_root: str = r'C:\ai_projects') -> Optional[str]:
    """
    Migrates a single-project directory to multi-project root.
    Copies all files and folders from src_dir to dest_root/project_name.
    Returns the path to the new project directory.
    """
    dest_dir = os.path.join(dest_root, project_name)
    if not os.path.exists(src_dir):
        raise FileNotFoundError(f"Source directory '{src_dir}' not found.")
    if os.path.exists(dest_dir):
        raise FileExistsError(f"Destination project '{dest_dir}' already exists.")
    shutil.copytree(src_dir, dest_dir)
    return dest_dir
