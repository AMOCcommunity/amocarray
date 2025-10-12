# Project Maintenance Checklist

Quick reference for maintaining AMOCatlas development environment and processes.

---

## Dependencies

**Adding packages:**
- ✅ Runtime needs → add to `requirements.txt`
- ✅ Development only → add to `requirements-dev.txt` 
- ✅ Update GitHub Actions if CI needs it

**Updating packages:**
- ✅ Test locally first
- ✅ Recreate virtual environment if major changes
- ✅ Verify CI still passes

---

## Environment Refresh

When things get messy:
```bash
rm -rf venv/
python3 -m venv venv
source venv/bin/activate
pip install -r requirements-dev.txt
pip install -e .
pytest  # Verify everything works
```

---

## Pre-merge Checklist

Before merging any PR:
- ✅ `pytest` passes locally
- ✅ `pre-commit run --all-files` passes  
- ✅ Run demo notebooks: `demo.ipynb` and `demo-convert.ipynb` (check for errors)
- ✅ Clear all notebook outputs before committing
- ✅ GitHub Actions CI is green
- ✅ Consider "Squash and merge" for cleaner history

---

## Documentation

**When adding docs dependencies:**
- ✅ Add to `requirements-dev.txt`
- ✅ Test build: `cd docs && make clean html`
- ✅ Verify GitHub Actions docs build passes

---

*For detailed workflows, see the {doc}`developer_guide`.*

