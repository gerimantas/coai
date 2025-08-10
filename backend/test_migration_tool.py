# test_migration_tool.py
import os
import tempfile
import shutil
from app.migration_tool import migrate_single_to_multi

def setup_single_project(tmpdir):
    os.makedirs(os.path.join(tmpdir, 'single'))
    with open(os.path.join(tmpdir, 'single', 'config.json'), 'w') as f:
        f.write('{"name": "single"}')
    with open(os.path.join(tmpdir, 'single', 'data.txt'), 'w') as f:
        f.write('data')

def test_migration():
    with tempfile.TemporaryDirectory() as tmpdir:
        setup_single_project(tmpdir)
        src = os.path.join(tmpdir, 'single')
        dest_root = os.path.join(tmpdir, 'projects')
        os.makedirs(dest_root)
        new_path = migrate_single_to_multi(src, 'migrated_project', dest_root)
        assert os.path.exists(new_path)
        assert os.path.exists(os.path.join(new_path, 'config.json'))
        assert os.path.exists(os.path.join(new_path, 'data.txt'))
