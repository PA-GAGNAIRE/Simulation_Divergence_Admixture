# 📦 Repository Contents & Getting Started

## 📥 How to Download & Run

### Option 1: Quick Download (for beginners)

1. **Download as ZIP**
   - Go to: https://github.com/PA-GAGNAIRE/Simulation_Divergence_Admixture
   - Click the green **"Code"** button
   - Select **"Download ZIP"**
   - Extract the ZIP file to your desired location
   - Open terminal/command prompt in that folder

2. **Follow Quick Start**
   - Read [QUICKSTART.md](QUICKSTART.md) - 5 minute setup guide

### Option 2: Git Clone (recommended for developers)

```bash
git clone https://github.com/PA-GAGNAIRE/Simulation_Divergence_Admixture.git
cd Simulation_Divergence_Admixture
```

### Option 3: GitHub Desktop

1. Download GitHub Desktop from https://desktop.github.com/
2. File → Clone Repository
3. Enter: `PA-GAGNAIRE/Simulation_Divergence_Admixture`

---

## 📚 Documentation Guide

### Getting Started Documents (Read These First!)

| Document | Purpose | Who Should Read |
|----------|---------|-----------------|
| **[QUICKSTART.md](QUICKSTART.md)** | 5-minute setup guide | Everyone - start here! |
| **[README.md](README.md)** | Feature overview & usage | All users |
| **[INSTALLATION.md](INSTALLATION.md)** | Detailed platform-specific setup | If you have installation issues |

### Setup & Installation

| File | Purpose |
|------|---------|
| **setup.sh** | Automated setup script (Linux/macOS) |
| **requirements.txt** | Python package dependencies |
| **check_environment.py** | Verify your installation |

### Analysis Documentation

| Document | Content | When to Read |
|----------|---------|--------------|
| **[MODEL_DESCRIPTION.md](MODEL_DESCRIPTION.md)** | Mathematical model details | Understanding the theory |
| **[LOCAL_ANCESTRY_GUIDE.md](LOCAL_ANCESTRY_GUIDE.md)** | Ancestry visualization guide | Interpreting ancestry plots |
| **[TRACT_LENGTH_GUIDE.md](TRACT_LENGTH_GUIDE.md)** | Tract length decay theory | Understanding admixture tracts |
| **[EXAMPLE_OUTPUT.md](EXAMPLE_OUTPUT.md)** | Expected results & patterns | Validating your results |
| **[IMPLEMENTATION_SUMMARY.md](IMPLEMENTATION_SUMMARY.md)** | Technical implementation | Developers & advanced users |

### Main Notebook

| File | Description |
|------|-------------|
| **divergence_admixture_simulation.ipynb** | Main Jupyter notebook with all simulations and analyses |

---

## 🚀 Quick Start Workflow

```
┌─────────────────────────────────────────────────────────────┐
│  1. DOWNLOAD                                                │
│  • Clone or download ZIP                                    │
│  • Extract to your working directory                        │
└─────────────────────────────────────────────────────────────┘
                           ↓
┌─────────────────────────────────────────────────────────────┐
│  2. INSTALL REQUIREMENTS                                    │
│  • Linux/macOS: Run ./setup.sh                              │
│  • All platforms: pip install -r requirements.txt          │
│  • Install SLiM (see INSTALLATION.md)                       │
└─────────────────────────────────────────────────────────────┘
                           ↓
┌─────────────────────────────────────────────────────────────┐
│  3. VERIFY                                                  │
│  • Run: python check_environment.py                         │
│  • All checks should show ✓                                 │
└─────────────────────────────────────────────────────────────┘
                           ↓
┌─────────────────────────────────────────────────────────────┐
│  4. RUN NOTEBOOK                                            │
│  • jupyter notebook divergence_admixture_simulation.ipynb   │
│  • Cell → Run All                                           │
└─────────────────────────────────────────────────────────────┘
                           ↓
┌─────────────────────────────────────────────────────────────┐
│  5. EXPLORE & CUSTOMIZE                                     │
│  • Modify parameters                                        │
│  • Read analysis guides                                     │
│  • Adapt for your research                                  │
└─────────────────────────────────────────────────────────────┘
```

---

## 🔧 Prerequisites

### Required Software

| Software | Minimum Version | Purpose |
|----------|----------------|---------|
| **Python** | 3.8+ | Running analyses |
| **SLiM** | 4.0+ | Forward-time simulations |
| **Git** | Any (optional) | Cloning repository |

### Required Python Packages (installed via requirements.txt)

- jupyter (≥1.0.0)
- notebook (≥6.0.0)
- tskit (≥0.5.0)
- numpy (≥1.20.0)
- matplotlib (≥3.3.0)
- pandas (≥1.2.0)

---

## 📖 Reading Path by User Type

### 👨‍🎓 Students / New Users

1. [QUICKSTART.md](QUICKSTART.md) - Get it running fast
2. [README.md](README.md) - Understand what it does
3. Run the notebook with default parameters
4. [EXAMPLE_OUTPUT.md](EXAMPLE_OUTPUT.md) - Compare your results
5. [MODEL_DESCRIPTION.md](MODEL_DESCRIPTION.md) - Learn the theory

### 👨‍🔬 Researchers

1. [README.md](README.md) - Feature overview
2. [MODEL_DESCRIPTION.md](MODEL_DESCRIPTION.md) - Mathematical foundation
3. Run notebook and analyze results
4. [LOCAL_ANCESTRY_GUIDE.md](LOCAL_ANCESTRY_GUIDE.md) - Detailed ancestry methods
5. [TRACT_LENGTH_GUIDE.md](TRACT_LENGTH_GUIDE.md) - Tract length applications
6. Modify parameters for your study

### 👨‍💻 Developers

1. [README.md](README.md) - Overview
2. [IMPLEMENTATION_SUMMARY.md](IMPLEMENTATION_SUMMARY.md) - Technical details
3. Review notebook code structure
4. [MODEL_DESCRIPTION.md](MODEL_DESCRIPTION.md) - Theoretical basis
5. Extend and modify as needed

---

## 🆘 Troubleshooting Path

Having problems? Follow this path:

```
Problem occurs
     ↓
1. Check QUICKSTART.md troubleshooting section
     ↓
2. Run: python check_environment.py
     ↓
3. Check INSTALLATION.md for your OS
     ↓
4. Search GitHub Issues
     ↓
5. Open new GitHub Issue with details
```

---

## 📊 What This Repository Does

### The Simulation Model

```
Time →

Recapitation     Ancestral Pop     Split      Divergence      Admixture      Analysis
(Equilibrium)    (size Na)         (Tsplit)   (no gene flow)  (Tadmix)       (tskit)
     ↓               ↓                 ↓            ↓              ↓              ↓
   ~10*Na        Generation 1     Pop1 (N1)    Independent   Pop3 formed    Statistics
generations      (burn-in)        Pop2 (N2)    evolution     (NAdmix)       & Plots
```

### Key Analyses Performed

1. **Dxy Decomposition**
   - Separates divergence into ancestral vs. new mutations
   - Shows temporal dynamics
   - Compares with theory

2. **Local Ancestry Visualization**
   - Maps genome ancestry blocks
   - Shows F1, F2, backcrosses, late-generation hybrids
   - Demonstrates recombination effects

3. **Tract Length Decay**
   - Measures admixture tract shortening
   - Compares observed vs. predicted: L = 1/[(1-h)rt]
   - Shows hyperbolic decay pattern

---

## 💡 Tips for Success

### For Fast Results
- Set `genome_length = 1e5` (instead of 1e6)
- Set `run_sweep = False`
- Set `run_multi_generation = False`
- Use smaller population sizes

### For Comprehensive Analysis
- Use default parameters
- Set `run_sweep = True` for Dxy time series
- Set `run_multi_generation = True` for tract decay curves
- Be patient - may take 30-45 minutes

### For Custom Research
1. Start with defaults to understand the system
2. Modify one parameter at a time
3. Document your changes
4. Compare results with EXAMPLE_OUTPUT.md
5. Read relevant guide (ancestry or tract length)

---

## 🔗 External Resources

### SLiM Resources
- **Official Site**: https://messerlab.org/slim/
- **Manual**: Comprehensive documentation
- **Cookbook**: Example recipes
- **Forum**: https://groups.google.com/g/slim-discuss

### tskit Resources
- **Documentation**: https://tskit.dev/
- **Tutorials**: https://tskit.dev/tutorials/
- **GitHub**: https://github.com/tskit-dev/tskit

### Population Genetics Background
- Wakeley, J. (2008). "Coalescent Theory: An Introduction"
- Hahn, M. W. (2018). "Molecular Population Genetics"

---

## ✅ Verification Checklist

Before running the simulation, verify:

- [ ] Repository downloaded and extracted
- [ ] Python 3.8+ installed
- [ ] SLiM 4.0+ installed
- [ ] Python packages installed (`pip install -r requirements.txt`)
- [ ] Environment check passes (`python check_environment.py`)
- [ ] Jupyter notebook opens (`jupyter notebook`)
- [ ] Read QUICKSTART.md or README.md

All checked? You're ready to simulate! 🎉

---

## 📬 Getting Help

1. **Documentation**: Check the guides above
2. **Environment Issues**: INSTALLATION.md
3. **GitHub Issues**: https://github.com/PA-GAGNAIRE/Simulation_Divergence_Admixture/issues
4. **SLiM Questions**: SLiM forum
5. **tskit Questions**: tskit documentation

---

## 📄 License

See repository for license information.

## 🙏 Citation

If you use this in your research, please cite appropriately (see repository).

---

**Ready to start?** → Open [QUICKSTART.md](QUICKSTART.md) and follow the 5-minute guide! 🚀
