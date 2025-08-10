# test_multi_project_manager.py
import os
import shutil
import tempfile
import pytest
from app.multi_project_manager import MultiProjectManager

def setup_projects(tmpdir):
    os.makedirs(os.path.join(tmpdir, 'projA'))
    os.makedirs(os.path.join(tmpdir, 'projB'))

class TestMultiProjectManager:
    def test_list_projects(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            setup_projects(tmpdir)
            mgr = MultiProjectManager(tmpdir)
            projects = mgr.list_projects()
            assert set(projects) == {'projA', 'projB'}

    def test_select_project(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            setup_projects(tmpdir)
            mgr = MultiProjectManager(tmpdir)
            path = mgr.select_project('projA')
            assert os.path.basename(path) == 'projA'
            with pytest.raises(FileNotFoundError):
                mgr.select_project('projX')

    def test_migrate_project(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            setup_projects(tmpdir)
            src = os.path.join(tmpdir, 'projA')
            dest = os.path.join(tmpdir, 'projA_copy')
            mgr = MultiProjectManager(tmpdir)
            assert mgr.migrate_project(src, dest)
            assert os.path.exists(dest)
