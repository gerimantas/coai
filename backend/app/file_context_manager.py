"""
COAI File Context Manager
Handles project file reading and context injection for AI agents
"""

import os
import logging
from typing import Dict, List, Any
from pathlib import Path

logger = logging.getLogger(__name__)

class FileContextManager:
    """
    Manages file context for AI agents - reads project files when needed
    """
    
    def __init__(self):
        # Workspace root (two levels up from backend/app/)
        self.workspace_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../'))
        self.max_file_size = 50000  # 50KB max per file
        self.allowed_extensions = {'.py', '.js', '.ts', '.jsx', '.tsx', '.md', '.txt', '.json', '.yaml', '.yml'}
        
    def should_include_file_context(self, message: str) -> bool:
        """
        Determine if message requires file context
        """
        file_keywords = [
            'files in this project', 'project files', 'what files',
            'project structure', 'file structure', 'list files',
            'show files', 'project contents', 'code files'
        ]
        
        message_lower = message.lower()
        return any(keyword in message_lower for keyword in file_keywords)
    
    def get_project_file_listing(self, project: str = None) -> Dict[str, Any]:
        """
        Get comprehensive project file listing
        """
        try:
            project_path = self.workspace_root
            
            # If specific project requested, look in that subfolder
            if project and project != "demo-project":
                potential_project_path = os.path.join(self.workspace_root, project)
                if os.path.exists(potential_project_path):
                    project_path = potential_project_path
            
            file_tree = self._build_file_tree(project_path)
            file_summary = self._get_file_summary(project_path)
            
            return {
                "status": "success",
                "project_path": project_path,
                "file_tree": file_tree,
                "file_summary": file_summary,
                "total_files": file_summary["total_files"]
            }
            
        except Exception as e:
            logger.error(f"Error getting project file listing: {str(e)}")
            return {
                "status": "error",
                "error": str(e),
                "file_tree": {},
                "file_summary": {"total_files": 0}
            }
    
    def _build_file_tree(self, root_path: str, max_depth: int = 3) -> Dict[str, Any]:
        """
        Build a tree structure of project files
        """
        def build_tree(path: str, current_depth: int = 0) -> Dict[str, Any]:
            if current_depth > max_depth:
                return {"name": "...", "type": "truncated"}
                
            name = os.path.basename(path)
            
            if os.path.isdir(path):
                # Skip hidden directories and common build/cache dirs
                if name.startswith('.') or name in ['node_modules', '__pycache__', 'dist', 'build']:
                    return None
                    
                children = []
                try:
                    for entry in sorted(os.listdir(path)):
                        child_path = os.path.join(path, entry)
                        child_tree = build_tree(child_path, current_depth + 1)
                        if child_tree:
                            children.append(child_tree)
                except PermissionError:
                    logger.warning(f"Permission denied accessing {path}")
                    return {"name": name, "type": "dir", "error": "permission_denied"}
                
                return {
                    "name": name,
                    "type": "dir",
                    "children": children[:20],  # Limit children to prevent overwhelming
                    "path": os.path.relpath(path, root_path)
                }
            else:
                # Only include allowed file types
                if Path(path).suffix.lower() not in self.allowed_extensions:
                    return None
                    
                file_size = os.path.getsize(path)
                return {
                    "name": name,
                    "type": "file",
                    "path": os.path.relpath(path, root_path),
                    "size": file_size,
                    "extension": Path(path).suffix
                }
        
        return build_tree(root_path)
    
    def _get_file_summary(self, root_path: str) -> Dict[str, Any]:
        """
        Get summary statistics about project files
        """
        summary = {
            "total_files": 0,
            "by_type": {},
            "key_files": [],
            "directories": []
        }
        
        try:
            for root, dirs, files in os.walk(root_path):
                # Skip hidden and build directories
                dirs[:] = [d for d in dirs if not d.startswith('.') and d not in ['node_modules', '__pycache__', 'dist', 'build']]
                
                rel_root = os.path.relpath(root, root_path)
                if rel_root != '.':
                    summary["directories"].append(rel_root)
                
                for file in files:
                    if file.startswith('.'):
                        continue
                        
                    file_path = os.path.join(root, file)
                    extension = Path(file).suffix.lower()
                    
                    if extension in self.allowed_extensions:
                        summary["total_files"] += 1
                        
                        # Count by file type
                        if extension in summary["by_type"]:
                            summary["by_type"][extension] += 1
                        else:
                            summary["by_type"][extension] = 1
                        
                        # Identify key files
                        if file in ['main.py', 'app.py', 'index.js', 'package.json', 'README.md', 'requirements.txt']:
                            summary["key_files"].append(os.path.relpath(file_path, root_path))
                            
        except Exception as e:
            logger.error(f"Error building file summary: {str(e)}")
        
        return summary
    
    def format_file_context_for_ai(self, file_data: Dict[str, Any]) -> str:
        """
        Format file listing for AI consumption
        """
        if file_data["status"] == "error":
            return f"Error reading project files: {file_data.get('error', 'Unknown error')}"
        
        summary = file_data["file_summary"]
        tree = file_data["file_tree"]
        
        formatted = [
            "=== PROJECT FILE STRUCTURE ===",
            f"Total files: {summary['total_files']}",
            "",
            "📁 DIRECTORY STRUCTURE:",
            self._format_tree_for_display(tree),
            "",
            "📄 FILE TYPES:",
        ]
        
        # Add file type breakdown
        for ext, count in summary["by_type"].items():
            formatted.append(f"  {ext or 'no extension'}: {count} files")
        
        # Add key files
        if summary["key_files"]:
            formatted.extend([
                "",
                "🔑 KEY FILES:",
            ])
            for key_file in summary["key_files"]:
                formatted.append(f"  - {key_file}")
        
        # Add main directories
        if summary["directories"]:
            formatted.extend([
                "",
                "📂 MAIN DIRECTORIES:",
            ])
            for directory in summary["directories"][:10]:  # Show first 10
                formatted.append(f"  - {directory}")
        
        return "\n".join(formatted)
    
    def _format_tree_for_display(self, tree: Dict[str, Any], indent: str = "") -> str:
        """
        Format file tree for readable display
        """
        if not tree:
            return "  (empty)"
            
        lines = []
        
        if tree.get("type") == "dir":
            lines.append(f"{indent}📁 {tree['name']}/")
            children = tree.get("children", [])
            for i, child in enumerate(children[:5]):  # Show first 5 children
                child_indent = indent + "  "
                lines.append(self._format_tree_for_display(child, child_indent))
            if len(children) > 5:
                lines.append(f"{indent}  ... and {len(children) - 5} more items")
        else:
            icon = "📄" if tree.get("type") == "file" else "📁"
            lines.append(f"{indent}{icon} {tree['name']}")
        
        return "\n".join(lines)

# Global instance
file_context_manager = FileContextManager()
