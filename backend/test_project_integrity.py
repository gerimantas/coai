# test_project_integrity.py
import os
import tempfile
import shutil
import pytest
from app.multi_project_manager import MultiProjectManager
from app.migration_tool import migrate_single_to_multi

def setup_projects(tmpdir):
    os.makedirs(os.path.join(tmpdir, 'projA'))
    with open(os.path.join(tmpdir, 'projA', 'data.txt'), 'w') as f:
        f.write('A')
    os.makedirs(os.path.join(tmpdir, 'projB'))
    with open(os.path.join(tmpdir, 'projB', 'data.txt'), 'w') as f:
        f.write('B')

def test_switching_integrity():
    with tempfile.TemporaryDirectory() as tmpdir:
        setup_projects(tmpdir)
        mgr = MultiProjectManager(tmpdir)
        assert set(mgr.list_projects()) == {'projA', 'projB'}
        pathA = mgr.select_project('projA')
        pathB = mgr.select_project('projB')
        assert os.path.exists(os.path.join(pathA, 'data.txt'))
        assert os.path.exists(os.path.join(pathB, 'data.txt'))
        with open(os.path.join(pathA, 'data.txt')) as f:
            assert f.read() == 'A'
        with open(os.path.join(pathB, 'data.txt')) as f:
            assert f.read() == 'B'

def test_migration_integrity():
    with tempfile.TemporaryDirectory() as tmpdir:
        src = os.path.join(tmpdir, 'single')
        os.makedirs(src)
        with open(os.path.join(src, 'data.txt'), 'w') as f:
            f.write('X')
        dest_root = os.path.join(tmpdir, 'projects')
        os.makedirs(dest_root)
        new_path = migrate_single_to_multi(src, 'migrated', dest_root)
        assert os.path.exists(new_path)
        with open(os.path.join(new_path, 'data.txt')) as f:
            assert f.read() == 'X'
