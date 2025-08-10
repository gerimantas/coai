# Local Git Hooks (Optional)

To protect read-only planning files (master, versions, and stage plans without checkboxes),
install the following pre-commit hook locally:

## .git/hooks/pre-commit (bash)

```bash
#!/usr/bin/env bash
set -e
protected_files=$(git diff --cached --name-only | egrep "planning/master/|planning/versions/|planning/progress/.*/stage[0-9]+_plan\.md$" || true)
if [ -n "$protected_files" ]; then
  echo "Blocking commit: protected planning files changed (master/versions/stage_plan)."
  echo "$protected_files"
  exit 1
fi
exit 0
```

Note: Git does not version-control hooks by default. Copy this file to `.git/hooks/pre-commit` and make it executable.
