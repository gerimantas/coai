# rules_loader.py
"""
Stage II: 11.1 Agent instructions & rules loader

Loads agent rules from .coai/rules/agent_rules.txt
"""
import os
from typing import Dict, List

RULES_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../.coai/rules/agent_rules.txt'))


def load_agent_rules(path: str = RULES_PATH) -> Dict[str, List[str]]:
    """
    Loads global rules and per-agent rules from the rules file.
    Returns a dict: { 'global': [...], 'agents': { agent_name: [...] } }
    """
    global_rules = []
    agent_rules = {}
    current_agent = None
    in_global = True
    if not os.path.exists(path):
        return { 'global': [], 'agents': {} }
    with open(path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if line.startswith('[agent:') and line.endswith(']'):
                current_agent = line[7:-1]
                agent_rules[current_agent] = []
                in_global = False
            elif current_agent and line and not line.startswith('#'):
                agent_rules[current_agent].append(line)
            elif not current_agent and line and not line.startswith('#'):
                # Collect global rules before first agent section
                global_rules.append(line)
    return { 'global': global_rules, 'agents': agent_rules }
