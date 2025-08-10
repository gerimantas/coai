# rules_loader.py
"""
Stage II: 11.1 Agent instructions & rules loader

Loads agent rules from .coai/rules/agent_rules.txt
"""
import os
from typing import Dict, List

RULES_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../.coai/rules/agent_rules.txt'))

def load_agent_rules(path: str = RULES_PATH) -> Dict[str, List[str]]:
    rules = {}
    current_agent = None
    if not os.path.exists(path):
        return rules
    with open(path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if line.startswith('[') and line.endswith(']'):
                current_agent = line[7:-1] if line.startswith('[agent:') else None
                if current_agent:
                    rules[current_agent] = []
            elif current_agent and line and not line.startswith('#'):
                rules[current_agent].append(line)
    return rules
