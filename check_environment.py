#!/usr/bin/env python3
"""
Environment verification script for SLiM simulation notebook.
Run this script to verify your environment is properly set up.
"""

import sys
import subprocess
import platform

def check_python_version():
    """Check Python version is >= 3.8"""
    version = sys.version_info
    version_str = f"{version.major}.{version.minor}.{version.micro}"
    if version.major >= 3 and version.minor >= 8:
        print(f"✓ Python {version_str} (OK)")
        return True, version_str
    else:
        print(f"✗ Python {version_str} (requires >= 3.8)")
        print("  → Install Python 3.8+ from https://www.python.org/")
        return False, version_str

def check_package(package_name, min_version=None):
    """Check if a Python package is installed and get version"""
    try:
        module = __import__(package_name)
        version = getattr(module, '__version__', 'unknown')
        return True, version
    except ImportError:
        return False, None

def check_slim():
    """Check if SLiM is installed and accessible"""
    try:
        # Try -version first
        result = subprocess.run(['slim', '-version'], 
                              capture_output=True, 
                              text=True, 
                              timeout=5)
        if result.returncode == 0:
            version = result.stdout.strip() if result.stdout else result.stderr.strip()
            # Extract version number if possible
            if 'version' in version.lower():
                print(f"✓ SLiM: {version}")
            else:
                print(f"✓ SLiM found: {version}")
            
            # Check if it's version 4.0+
            if 'version 4' in version or 'version 5' in version:
                print("  → Version 4.0+ detected (tree sequence support available)")
                return True, version
            else:
                print("  ⚠ Warning: SLiM 4.0+ recommended for tree sequence recording")
                return True, version
        else:
            print("✗ SLiM not properly configured")
            return False, None
    except FileNotFoundError:
        print("✗ SLiM not found in PATH")
        print_slim_instructions()
        return False, None
    except subprocess.TimeoutExpired:
        print("✗ SLiM command timed out")
        return False, None
    except Exception as e:
        print(f"✗ Error checking SLiM: {e}")
        return False, None

def print_slim_instructions():
    """Print OS-specific SLiM installation instructions"""
    os_type = platform.system()
    print("\n  Installation instructions:")
    if os_type == "Linux":
        print("    • Ubuntu/Debian:")
        print("        sudo apt-get install cmake g++ ninja-build")
        print("        wget https://github.com/MesserLab/SLiM/releases/download/v4.1/SLiM.zip")
        print("        unzip SLiM.zip && cd SLiM && mkdir build && cd build")
        print("        cmake -G Ninja .. && ninja && sudo ninja install")
    elif os_type == "Darwin":
        print("    • macOS:")
        print("        Download from: https://messerlab.org/slim/")
        print("        Or build with: brew install cmake ninja")
    elif os_type == "Windows":
        print("    • Windows:")
        print("        Use WSL (Windows Subsystem for Linux) - recommended")
        print("        Or download native build from https://messerlab.org/slim/")
    print("    • Conda (all platforms):")
    print("        conda install -c conda-forge slim")
    print("    • See INSTALLATION.md for detailed instructions")

def main():
    print("=" * 80)
    print("   Environment Verification for Simulation_Divergence_Admixture")
    print("=" * 80)
    print()
    
    # System info
    print(f"System: {platform.system()} {platform.release()}")
    print(f"Platform: {platform.platform()}")
    print()
    
    all_ok = True
    warnings = []
    
    # Check Python version
    print("1. Checking Python version...")
    python_ok, python_version = check_python_version()
    if not python_ok:
        all_ok = False
    print()
    
    # Check required packages
    print("2. Checking required Python packages...")
    required_packages = {
        'jupyter': ('jupyter', '1.0.0'),
        'notebook': ('notebook', '6.0.0'),
        'tskit': ('tskit', '0.5.0'),
        'numpy': ('numpy', '1.20.0'),
        'matplotlib': ('matplotlib', '3.3.0'),
        'pandas': ('pandas', '1.2.0'),
    }
    
    missing_packages = []
    outdated_packages = []
    
    for display_name, (import_name, min_version) in required_packages.items():
        installed, version = check_package(import_name)
        if installed:
            print(f"   ✓ {display_name}: {version}")
        else:
            print(f"   ✗ {display_name}: NOT INSTALLED")
            missing_packages.append(import_name)
            all_ok = False
    
    if missing_packages:
        print("\n   → To install missing packages:")
        print(f"       pip install -r requirements.txt")
        print("      or")
        print(f"       pip install {' '.join(missing_packages)}")
    print()
    
    # Check SLiM
    print("3. Checking SLiM installation...")
    slim_ok, slim_version = check_slim()
    if not slim_ok:
        all_ok = False
    print()
    
    # Check Jupyter notebook
    print("4. Checking Jupyter notebook...")
    if check_package('notebook')[0]:
        print("   ✓ Jupyter Notebook is installed")
        print("   → Start with: jupyter notebook divergence_admixture_simulation.ipynb")
    else:
        print("   ✗ Jupyter Notebook not found")
        all_ok = False
    print()
    
    # Additional checks
    print("5. Additional information...")
    
    # Check if requirements.txt exists
    try:
        with open('requirements.txt', 'r') as f:
            print("   ✓ requirements.txt found")
    except FileNotFoundError:
        print("   ⚠ requirements.txt not found (are you in the right directory?)")
        warnings.append("Make sure you're running this from the repository root")
    
    # Check if notebook exists
    try:
        with open('divergence_admixture_simulation.ipynb', 'r') as f:
            print("   ✓ divergence_admixture_simulation.ipynb found")
    except FileNotFoundError:
        print("   ⚠ divergence_admixture_simulation.ipynb not found")
        warnings.append("Notebook file not found in current directory")
    
    print()
    
    # Summary
    print("=" * 80)
    print("SUMMARY")
    print("=" * 80)
    
    if all_ok:
        print("✓✓✓ All requirements satisfied! ✓✓✓")
        print()
        print("You're ready to run the simulation notebook!")
        print()
        print("Next steps:")
        print("  1. Start Jupyter: jupyter notebook")
        print("  2. Open: divergence_admixture_simulation.ipynb")
        print("  3. Run cells with Shift+Enter or Cell → Run All")
        print()
        print("For detailed usage instructions, see README.md")
    else:
        print("✗ Some requirements are missing or outdated")
        print()
        print("Please fix the issues above before running the notebook.")
        print("See INSTALLATION.md for detailed setup instructions.")
    
    if warnings:
        print()
        print("WARNINGS:")
        for warning in warnings:
            print(f"  ⚠ {warning}")
    
    print("=" * 80)
    print()
    
    return 0 if all_ok else 1

if __name__ == "__main__":
    sys.exit(main())
