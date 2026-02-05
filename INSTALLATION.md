# Installation Guide

Complete step-by-step guide to set up and run the Simulation_Divergence_Admixture notebook on your local computer.

## Table of Contents

1. [Quick Start](#quick-start)
2. [Detailed Installation](#detailed-installation)
3. [Platform-Specific Instructions](#platform-specific-instructions)
4. [Verification](#verification)
5. [Troubleshooting](#troubleshooting)
6. [Running the Notebook](#running-the-notebook)

---

## Quick Start

For experienced users, here's the quick version:

```bash
# 1. Clone the repository
git clone https://github.com/PA-GAGNAIRE/Simulation_Divergence_Admixture.git
cd Simulation_Divergence_Admixture

# 2. Install SLiM (see platform-specific instructions below)

# 3. Install Python dependencies
pip install -r requirements.txt

# 4. Verify installation
python check_environment.py

# 5. Run the notebook
jupyter notebook divergence_admixture_simulation.ipynb
```

---

## Detailed Installation

### Step 1: Download the Repository

You have three options to get the code:

#### Option A: Git Clone (Recommended)
```bash
git clone https://github.com/PA-GAGNAIRE/Simulation_Divergence_Admixture.git
cd Simulation_Divergence_Admixture
```

#### Option B: Download ZIP
1. Go to https://github.com/PA-GAGNAIRE/Simulation_Divergence_Admixture
2. Click the green "Code" button
3. Select "Download ZIP"
4. Extract the ZIP file
5. Open terminal/command prompt in the extracted folder

#### Option C: GitHub Desktop
1. Install GitHub Desktop from https://desktop.github.com/
2. File → Clone Repository
3. Enter: `PA-GAGNAIRE/Simulation_Divergence_Admixture`
4. Choose a local path and clone

### Step 2: Install SLiM

SLiM is required to run the forward-time population genetic simulations.

**Minimum version**: SLiM 4.0 (SLiM 4.1+ recommended for best compatibility)

See [Platform-Specific Instructions](#platform-specific-instructions) below for installation on your operating system.

### Step 3: Install Python and Dependencies

#### Python Version
- **Required**: Python 3.8 or later
- **Recommended**: Python 3.9 or 3.10

Check your Python version:
```bash
python --version
# or
python3 --version
```

#### Install Python Packages

The easiest method is using pip:

```bash
pip install -r requirements.txt
```

Or install individually:
```bash
pip install jupyter notebook tskit numpy matplotlib pandas
```

#### Using Conda (Alternative)

If you use Anaconda or Miniconda:

```bash
# Create a new environment
conda create -n slim_sim python=3.9
conda activate slim_sim

# Install packages
pip install -r requirements.txt
```

### Step 4: Verify Installation

Run the environment check script:

```bash
python check_environment.py
```

This will verify:
- ✓ Python version
- ✓ SLiM installation and version
- ✓ All required Python packages
- ✓ Package versions

If everything is green with ✓ marks, you're ready to go!

---

## Platform-Specific Instructions

### Linux

#### Installing SLiM on Linux

**Ubuntu/Debian:**
```bash
# Install dependencies
sudo apt-get update
sudo apt-get install cmake g++ ninja-build

# Download and build SLiM
wget https://github.com/MesserLab/SLiM/releases/download/v4.1/SLiM.zip
unzip SLiM.zip
cd SLiM
mkdir build && cd build
cmake -G Ninja ..
ninja
sudo ninja install

# Verify installation
slim -v
```

**Fedora/RHEL/CentOS:**
```bash
# Install dependencies
sudo dnf install cmake gcc-c++ ninja-build

# Then follow the build steps above
```

**Alternative: Build from source**
```bash
git clone https://github.com/MesserLab/SLiM.git
cd SLiM
mkdir build && cd build
cmake -G Ninja ..
ninja
sudo ninja install
```

#### Installing Python packages on Linux
```bash
# Using system Python
pip install --user -r requirements.txt

# Or using apt (Ubuntu/Debian)
sudo apt-get install python3-jupyter python3-numpy python3-matplotlib python3-pandas
pip install --user tskit
```

### macOS

#### Installing SLiM on macOS

**Option 1: Download pre-built binary (Easiest)**
1. Go to https://messerlab.org/slim/
2. Download the latest macOS version (dmg file)
3. Open the dmg and drag SLiM to Applications
4. Add to PATH (add to ~/.zshrc or ~/.bash_profile):
   ```bash
   export PATH="/Applications/SLiM.app/Contents/MacOS:$PATH"
   ```
5. Restart terminal and verify:
   ```bash
   slim -v
   ```

**Option 2: Build from source**
```bash
# Install Xcode Command Line Tools
xcode-select --install

# Install CMake (using Homebrew)
brew install cmake ninja

# Download and build
wget https://github.com/MesserLab/SLiM/releases/download/v4.1/SLiM.zip
unzip SLiM.zip
cd SLiM
mkdir build && cd build
cmake -G Ninja ..
ninja
sudo ninja install
```

#### Installing Python packages on macOS
```bash
# Using pip
pip3 install -r requirements.txt

# Or using Homebrew
brew install python3
pip3 install -r requirements.txt
```

### Windows

#### Installing SLiM on Windows

**Option 1: Windows Subsystem for Linux (WSL) - Recommended**

WSL allows you to run Linux on Windows and is the easiest way to use SLiM:

1. **Install WSL**:
   - Open PowerShell as Administrator
   - Run: `wsl --install`
   - Restart computer
   - Open "Ubuntu" from Start menu

2. **Inside WSL, follow Linux instructions**:
   ```bash
   # Update system
   sudo apt-get update
   sudo apt-get upgrade
   
   # Install dependencies
   sudo apt-get install cmake g++ ninja-build python3 python3-pip
   
   # Install SLiM (see Linux instructions above)
   
   # Clone repository
   git clone https://github.com/PA-GAGNAIRE/Simulation_Divergence_Admixture.git
   cd Simulation_Divergence_Admixture
   
   # Install Python packages
   pip3 install -r requirements.txt
   ```

3. **Run Jupyter in WSL**:
   ```bash
   jupyter notebook --no-browser
   # Copy the URL with token that appears
   # Paste it into your Windows browser
   ```

**Option 2: Native Windows Build**

SLiM can be built natively on Windows using Visual Studio:

1. Install Visual Studio 2019 or later with C++ tools
2. Install CMake from https://cmake.org/download/
3. Download SLiM source from https://github.com/MesserLab/SLiM
4. Build using CMake and Visual Studio
5. Add to PATH

See detailed instructions at: https://messerlab.org/slim/

**Option 3: Docker**

Run everything in a containerized environment:

```bash
# Pull and run a Python/Jupyter container
docker run -p 8888:8888 -v "%cd%":/home/jovyan/work jupyter/scipy-notebook

# Install SLiM inside container
# (Requires additional setup - see Linux instructions)
```

---

## Verification

After installation, verify everything works:

### 1. Check SLiM

```bash
slim -v
```

Expected output: `SLiM version 4.x, built ...`

### 2. Check Python

```bash
python --version
```

Expected: `Python 3.8.x` or later

### 3. Check Python Packages

```bash
python check_environment.py
```

Expected output with all ✓ marks:
```
Checking environment for SLiM simulation notebook...

✓ Python version: 3.9.x (OK)
✓ SLiM found: version 4.1
✓ jupyter: 1.0.0 (OK)
✓ notebook: 6.4.0 (OK)
✓ tskit: 0.5.3 (OK)
✓ numpy: 1.21.0 (OK)
✓ matplotlib: 3.4.2 (OK)
✓ pandas: 1.3.0 (OK)

✓✓✓ All requirements satisfied! ✓✓✓
```

### 4. Test SLiM Script

Create a simple test:

```bash
echo 'initialize() { initializeMutationRate(0); initializeTreeSeq(); initializeRecombinationRate(0); }
1 early() { sim.addSubpop("p0", 100); }
10 late() { sim.treeSeqOutput("test.trees"); }' > test.slim

slim test.slim
```

Should complete without errors and create `test.trees`.

---

## Troubleshooting

### SLiM Not Found

**Problem**: `slim: command not found` or `'slim' is not recognized`

**Solution**:
- Verify SLiM is installed: Look for it in Applications (macOS) or Program Files
- Add SLiM to PATH:
  - **Linux/macOS**: Add to `~/.bashrc` or `~/.zshrc`:
    ```bash
    export PATH="/path/to/slim:$PATH"
    ```
  - **Windows**: Add SLiM directory to System PATH in Environment Variables

### Python Version Too Old

**Problem**: `Python 3.7` or earlier

**Solution**:
- Install Python 3.8+ from https://www.python.org/downloads/
- Or use conda: `conda install python=3.9`

### tskit Installation Fails

**Problem**: Error installing tskit

**Solution**:
- Update pip: `pip install --upgrade pip`
- Install build tools:
  - **Linux**: `sudo apt-get install python3-dev build-essential`
  - **macOS**: `xcode-select --install`
  - **Windows**: Install Visual C++ Build Tools
- Try: `pip install --upgrade tskit`

### Jupyter Not Starting

**Problem**: `jupyter: command not found`

**Solution**:
```bash
# Ensure jupyter is installed
pip install jupyter notebook

# If installed but not found, check PATH
python -m jupyter notebook
```

### Permission Errors (Linux/macOS)

**Problem**: Permission denied when installing packages

**Solution**:
```bash
# Install in user directory (no sudo needed)
pip install --user -r requirements.txt

# Or use virtual environment
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Memory Issues

**Problem**: Notebook crashes or runs very slowly

**Solution**:
- Reduce simulation parameters in the notebook:
  - Decrease `genome_length` (e.g., to 1e5)
  - Reduce population sizes
  - Shorten simulation time
- Close other applications
- Use parameter `run_sweep=False` to skip time-intensive analyses

### SLiM Version Incompatibility

**Problem**: SLiM script fails with syntax errors

**Solution**:
- Update to SLiM 4.0 or later
- Check version: `slim -v`
- If using SLiM 3.x, many features won't work (tree sequence recording was added in 4.0)

### Windows-Specific Issues

**Problem**: Line ending issues, path problems

**Solution**:
- Use WSL (strongly recommended)
- Or use Git Bash for better Unix-like environment
- Ensure text editor doesn't convert line endings (use LF, not CRLF)

### Package Conflicts

**Problem**: Version conflicts between packages

**Solution**:
```bash
# Create fresh virtual environment
python -m venv slim_env
source slim_env/bin/activate  # Linux/macOS
# or
slim_env\Scripts\activate  # Windows

# Install from requirements
pip install -r requirements.txt
```

---

## Running the Notebook

Once everything is installed and verified:

### Start Jupyter

```bash
# Navigate to repository directory
cd Simulation_Divergence_Admixture

# Launch Jupyter
jupyter notebook
```

This will:
1. Start the Jupyter server
2. Open your web browser automatically
3. Show the file browser

### Open the Notebook

In the Jupyter browser interface:
1. Click on `divergence_admixture_simulation.ipynb`
2. The notebook will open in a new tab

### Run the Analysis

**Option 1: Run all cells**
- Menu: Cell → Run All
- Or: Click the ⏩ button in toolbar

**Option 2: Run cells individually**
- Click on a cell
- Press Shift+Enter to run and move to next cell
- Or click the ▶ Run button in toolbar

### Expected Runtime

- Basic simulation (~10 generations): 1-5 minutes
- With parameter sweeps: 10-30 minutes
- Multi-generation tract length analysis: 15-45 minutes

Runtime depends on:
- Genome length
- Population sizes  
- Number of samples
- Computer speed

### Modify Parameters

In the first code cells, you can adjust:

```python
# Demographic parameters
Na = 1000        # Ancestral population size
N1 = 800         # Population 1 size
N2 = 1200        # Population 2 size
NAdmix = 1000    # Admixed population size

# Timing
Tsplit = 1000    # When populations split
Tadmix = 2000    # When admixture occurs

# Genetic
genome_length = 1e6      # Genome size (bp)
recomb_rate = 1e-8       # Recombination rate
mutation_rate = 1e-8     # Mutation rate

# Analysis options
run_sweep = False        # Set True for split time analysis
run_multi_generation = False  # Set True for tract length time series
```

Start with default values, then experiment!

---

## Getting Help

If you encounter issues not covered here:

1. **Check the Documentation**:
   - README.md - Overview and usage
   - EXAMPLE_OUTPUT.md - Expected results
   - MODEL_DESCRIPTION.md - Theoretical background

2. **Check SLiM Documentation**:
   - Manual: https://messerlab.org/slim/
   - Cookbook: Real-world examples
   - Forum: https://groups.google.com/g/slim-discuss

3. **Check tskit Documentation**:
   - https://tskit.dev/tskit/docs/stable/

4. **GitHub Issues**:
   - Search existing issues: https://github.com/PA-GAGNAIRE/Simulation_Divergence_Admixture/issues
   - Open a new issue with:
     - Your operating system
     - Python version
     - SLiM version
     - Error messages
     - What you've tried

5. **Python/Jupyter Help**:
   - Jupyter documentation: https://jupyter-notebook.readthedocs.io/
   - Stack Overflow: Tag questions with `jupyter-notebook`, `slim`, or `tskit`

---

## Next Steps

After successful installation:

1. **Read the README**: Understand the simulation model
2. **Run the default simulation**: Get familiar with outputs
3. **Explore parameters**: Try different demographic scenarios
4. **Read the guides**:
   - LOCAL_ANCESTRY_GUIDE.md - Understanding ancestry patterns
   - TRACT_LENGTH_GUIDE.md - Tract length decay theory
   - MODEL_DESCRIPTION.md - Mathematical details
5. **Adapt for your research**: Modify for your specific questions

Happy simulating! 🧬
