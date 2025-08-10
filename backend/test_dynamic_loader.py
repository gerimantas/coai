# test_dynamic_loader.py
import os
import tempfile
import json
from app.dynamic_loader import DynamicProjectLoader

def setup_project(tmpdir):
    os.makedirs(os.path.join(tmpdir, 'demo'))
    with open(os.path.join(tmpdir, 'demo', 'config.json'), 'w', encoding='utf-8') as f:
        json.dump({'name': 'demo', 'version': 1}, f)
    with open(os.path.join(tmpdir, 'demo', 'rules.txt'), 'w', encoding='utf-8') as f:
        f.write('rule1\nrule2')
    with open(os.path.join(tmpdir, 'demo', 'plan.md'), 'w', encoding='utf-8') as f:
        f.write('# Demo Plan')

def test_dynamic_loader():
    with tempfile.TemporaryDirectory() as tmpdir:
        setup_project(tmpdir)
        loader = DynamicProjectLoader(tmpdir)
        config = loader.get_config('demo')
        assert config['name'] == 'demo'
        assert config['version'] == 1
        rules = loader.get_rules('demo')
        assert 'rule1' in rules
        plan = loader.get_plan('demo')
        assert plan.startswith('# Demo Plan')
