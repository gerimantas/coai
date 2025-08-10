# test_rules_loader.py
import os
import tempfile
from app.rules_loader import load_agent_rules

def test_load_agent_rules():
    with tempfile.TemporaryDirectory() as tmpdir:
        rules_path = os.path.join(tmpdir, 'agent_rules.txt')
        with open(rules_path, 'w') as f:
            f.write('# Global rules\n- Global1\n- Global2\n[agent:default]\n- Rule1\n- Rule2\n[agent:admin]\n- AdminRule')
        rules = load_agent_rules(rules_path)
        assert 'global' in rules
        assert 'agents' in rules
        assert rules['global'] == ['- Global1', '- Global2']
        assert 'default' in rules['agents']
        assert 'admin' in rules['agents']
        assert rules['agents']['default'] == ['- Rule1', '- Rule2']
        assert rules['agents']['admin'] == ['- AdminRule']
