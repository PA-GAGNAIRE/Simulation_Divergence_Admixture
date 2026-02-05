# Quick Start Guide

Get up and running in minutes!

## Prerequisites

Before you start, you need:
- **Python 3.8+** - Download from [python.org](https://www.python.org/)
- **SLiM 4.0+** - Download from [messerlab.org/slim](https://messerlab.org/slim/)
- **Git** (optional, for cloning) - Download from [git-scm.com](https://git-scm.com/)

## Installation Steps

### 1. Get the Code

**Option A: Clone with Git**
```bash
git clone https://github.com/PA-GAGNAIRE/Simulation_Divergence_Admixture.git
cd Simulation_Divergence_Admixture
```

**Option B: Download ZIP**
- Visit https://github.com/PA-GAGNAIRE/Simulation_Divergence_Admixture
- Click "Code" → "Download ZIP"
- Extract and open terminal in that folder

### 2. Install Python Packages

```bash
pip install -r requirements.txt
```

If you get permission errors, try:
```bash
pip install --user -r requirements.txt
```

### 3. Verify Installation

```bash
python check_environment.py
```

You should see all ✓ marks. If not, see troubleshooting below.

### 4. Run the Notebook

```bash
jupyter notebook divergence_admixture_simulation.ipynb
```

This opens Jupyter in your browser. In the notebook:
- Click **Cell → Run All** to run everything
- Or press **Shift+Enter** to run cells one by one

## Expected Runtime

- Basic simulation: **1-5 minutes**
- With parameter sweeps: **10-30 minutes**
- Full analysis: **15-45 minutes**

## Quick Troubleshooting

### "slim: command not found"
- SLiM is not installed or not in PATH
- **Fix**: Install SLiM from https://messerlab.org/slim/
- **Linux**: Follow build instructions in INSTALLATION.md
- **macOS**: Download dmg and add to PATH
- **Windows**: Use WSL

### "ModuleNotFoundError: No module named 'tskit'"
- Python packages not installed
- **Fix**: `pip install -r requirements.txt`

### "jupyter: command not found"
- Jupyter not installed or not in PATH
- **Fix**: `pip install jupyter notebook`
- **Alternative**: `python -m jupyter notebook`

### Notebook crashes or runs slowly
- System resources exhausted
- **Fix**: In notebook, reduce parameters:
  ```python
  genome_length = 1e5  # Instead of 1e6
  run_sweep = False    # Skip time-intensive analysis
  ```

### Permission errors
- Can't install packages globally
- **Fix**: Use virtual environment or --user flag:
  ```bash
  python -m venv venv
  source venv/bin/activate  # Linux/macOS
  pip install -r requirements.txt
  ```

## What You'll See

The notebook produces:

1. **Population genetics statistics**
   - Genetic diversity (π)
   - Tajima's D
   - FST between populations
   - Site frequency spectra

2. **Dxy decomposition plots**
   - Total divergence over time
   - Ancestral vs. new mutations
   - Theoretical comparisons

3. **Local ancestry visualizations**
   - Chromosome mosaics (F1, F2, backcrosses)
   - Ancestry block distributions
   - Recombination patterns

4. **Tract length decay**
   - Admixture tract lengths over time
   - Observed vs. analytical predictions
   - Hyperbolic decay curves

## Customizing Parameters

In the notebook's first code cells, you can modify:

```python
# Quick test (faster)
genome_length = 1e5
Tsplit = 500
Tadmix = 1000

# Detailed analysis (slower)
genome_length = 1e6
Tsplit = 1000
Tadmix = 2000
run_sweep = True
run_multi_generation = True
```

## Next Steps

Once it's working:

1. **Explore the documentation**
   - [README.md](README.md) - Full feature overview
   - [MODEL_DESCRIPTION.md](MODEL_DESCRIPTION.md) - Mathematical details
   - [LOCAL_ANCESTRY_GUIDE.md](LOCAL_ANCESTRY_GUIDE.md) - Ancestry analysis
   - [TRACT_LENGTH_GUIDE.md](TRACT_LENGTH_GUIDE.md) - Tract length theory

2. **Experiment with parameters**
   - Try different population sizes
   - Vary split and admixture times
   - Change admixture proportions

3. **Adapt for your research**
   - Modify demographic model
   - Add your own analyses
   - Create custom visualizations

## Getting Help

**Still stuck?**

1. Check [INSTALLATION.md](INSTALLATION.md) for detailed instructions
2. Search [GitHub Issues](https://github.com/PA-GAGNAIRE/Simulation_Divergence_Admixture/issues)
3. Open a new issue with:
   - Your OS and versions
   - Full error message
   - What you've tried

**External resources:**
- SLiM Manual: https://messerlab.org/slim/
- tskit Documentation: https://tskit.dev/
- Jupyter Help: https://jupyter-notebook.readthedocs.io/

Happy simulating! 🧬
