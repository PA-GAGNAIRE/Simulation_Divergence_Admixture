#!/usr/bin/env python3
"""
Environment verification script for SLiM5 simulation notebook.
Run this script to verify your environment is properly set up.
"""

import sys
import subprocess

def check_python_version():
    """Check Python version is >= 3.8"""
    version = sys.version_info
    if version.major >= 3 and version.minor >= 8:
        print(f"✓ Python {version.major}.{version.minor}.{version.micro}")
        return True
    else:
        print(f"✗ Python {version.major}.{version.minor}.{version.micro} (requires >= 3.8)")
        return False

def check_package(package_name):
    """Check if a Python package is installed"""
    try:
        __import__(package_name)
        return True
    except ImportError:
        return False

def check_slim():
    """Check if SLiM is installed and accessible"""
    try:
        result = subprocess.run(['slim', '-version'], 
                              capture_output=True, 
                              text=True, 
                              timeout=5)
        if result.returncode == 0:
            version = result.stdout.strip() if result.stdout else result.stderr.strip()
            print(f"✓ SLiM installed: {version}")
            return True
        else:
            print("✗ SLiM not properly configured")
            return False
    except FileNotFoundError:
        print("✗ SLiM not found in PATH")
        return False
    except Exception as e:
        print(f"✗ Error checking SLiM: {e}")
        return False

def main():
    print("=" * 70)
    print("Environment Verification for SLiM5 Simulation Notebook")
    print("=" * 70)
    print()
    
    all_ok = True
    
    # Check Python version
    print("Checking Python version...")
    if not check_python_version():
        all_ok = False
    print()
    
    # Check required packages
    print("Checking required Python packages...")
    required_packages = {
        'numpy': 'numpy',
        'matplotlib': 'matplotlib',
        'pandas': 'pandas',
        'tskit': 'tskit',
        'jupyter': 'jupyter'
    }
    
    missing_packages = []
    for display_name, import_name in required_packages.items():
        if check_package(import_name):
            print(f"✓ {display_name}")
        else:
            print(f"✗ {display_name}")
            missing_packages.append(display_name)
            all_ok = False
    
    if missing_packages:
        print(f"\nTo install missing packages, run:")
        print(f"  pip install {' '.join(missing_packages)}")
        print(f"or:")
        print(f"  pip install -r requirements.txt")
    print()
    
    # Check SLiM
    print("Checking SLiM installation...")
    if not check_slim():
        print("\nTo install SLiM:")
        print("  Visit: https://messerlab.org/slim/")
        print("  Or use conda: conda install -c conda-forge slim")
        all_ok = False
    print()
    
    # Summary
    print("=" * 70)
    if all_ok:
        print("✓ Environment is ready! You can run the notebook.")
    else:
        print("✗ Some requirements are missing. Please install them before running.")
    print("=" * 70)
    
    return 0 if all_ok else 1

if __name__ == "__main__":
    sys.exit(main())
