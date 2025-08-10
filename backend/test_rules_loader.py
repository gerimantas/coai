# test_rules_loader.py
import os
import tempfile
from app.rules_loader import load_agent_rules

def test_load_agent_rules():
    with tempfile.TemporaryDirectory() as tmpdir:
        rules_path = os.path.join(tmpdir, 'agent_rules.txt')
        with open(rules_path, 'w') as f:
            f.write('[agent:default]\n- Rule1\n- Rule2\n[agent:admin]\n- AdminRule')
        rules = load_agent_rules(rules_path)
        assert 'default' in rules
        assert 'admin' in rules
        assert rules['default'] == ['- Rule1', '- Rule2']
        assert rules['admin'] == ['- AdminRule']
