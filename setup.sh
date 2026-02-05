#!/bin/bash

# Automated setup script for Simulation_Divergence_Admixture
# For Linux and macOS systems

set -e  # Exit on error

echo "========================================================================"
echo "  Simulation_Divergence_Admixture Setup Script"
echo "========================================================================"
echo ""

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

print_status() {
    echo -e "${BLUE}[INFO]${NC} $1"
}

print_success() {
    echo -e "${GREEN}[SUCCESS]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

print_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

# Check if running on supported OS
print_status "Checking operating system..."
OS="$(uname -s)"
case "$OS" in
    Linux*)     OS_TYPE=Linux;;
    Darwin*)    OS_TYPE=macOS;;
    *)          OS_TYPE="UNKNOWN:${OS}";;
esac

if [[ "$OS_TYPE" == "UNKNOWN"* ]]; then
    print_error "Unsupported operating system: $OS"
    print_error "This script supports Linux and macOS only."
    print_error "For Windows, please use WSL or see INSTALLATION.md"
    exit 1
fi

print_success "Operating system: $OS_TYPE"
echo ""

# Check Python installation
print_status "Checking Python installation..."
if command -v python3 &> /dev/null; then
    PYTHON_CMD="python3"
    PYTHON_VERSION=$(python3 --version 2>&1 | awk '{print $2}')
    print_success "Python found: $PYTHON_VERSION"
    
    # Check Python version (needs 3.8+)
    PYTHON_MAJOR=$(echo $PYTHON_VERSION | cut -d. -f1)
    PYTHON_MINOR=$(echo $PYTHON_VERSION | cut -d. -f2)
    
    if [[ $PYTHON_MAJOR -lt 3 ]] || [[ $PYTHON_MAJOR -eq 3 && $PYTHON_MINOR -lt 8 ]]; then
        print_error "Python 3.8 or later is required (found $PYTHON_VERSION)"
        print_error "Please install Python 3.8+ and run this script again"
        exit 1
    fi
elif command -v python &> /dev/null; then
    PYTHON_VERSION=$(python --version 2>&1 | awk '{print $2}')
    if [[ $PYTHON_VERSION == 3.* ]]; then
        PYTHON_CMD="python"
        print_success "Python found: $PYTHON_VERSION"
    else
        print_error "Python 3.8+ is required"
        exit 1
    fi
else
    print_error "Python not found!"
    print_error "Please install Python 3.8+ from https://www.python.org/"
    exit 1
fi
echo ""

# Check pip installation
print_status "Checking pip installation..."
if command -v pip3 &> /dev/null; then
    PIP_CMD="pip3"
    print_success "pip3 found"
elif command -v pip &> /dev/null; then
    PIP_CMD="pip"
    print_success "pip found"
else
    print_warning "pip not found, installing..."
    $PYTHON_CMD -m ensurepip --default-pip || {
        print_error "Failed to install pip"
        exit 1
    }
    PIP_CMD="$PYTHON_CMD -m pip"
fi
echo ""

# Check SLiM installation
print_status "Checking SLiM installation..."
if command -v slim &> /dev/null; then
    SLIM_VERSION=$(slim -v 2>&1 | head -n1)
    print_success "SLiM found: $SLIM_VERSION"
    
    # Check if version is 4.0+
    if [[ $SLIM_VERSION == *"SLiM version 4"* ]] || [[ $SLIM_VERSION == *"SLiM version 5"* ]]; then
        print_success "SLiM version is compatible (4.0+)"
    else
        print_warning "SLiM version may be too old (4.0+ required)"
        print_warning "Tree sequence recording was added in SLiM 4.0"
    fi
else
    print_error "SLiM not found!"
    echo ""
    print_status "SLiM installation instructions:"
    if [[ "$OS_TYPE" == "Linux" ]]; then
        echo "  1. Install dependencies:"
        echo "     sudo apt-get install cmake g++ ninja-build"
        echo ""
        echo "  2. Download and build SLiM:"
        echo "     wget https://github.com/MesserLab/SLiM/releases/download/v4.1/SLiM.zip"
        echo "     unzip SLiM.zip && cd SLiM"
        echo "     mkdir build && cd build"
        echo "     cmake -G Ninja .."
        echo "     ninja"
        echo "     sudo ninja install"
    elif [[ "$OS_TYPE" == "macOS" ]]; then
        echo "  Download from: https://messerlab.org/slim/"
        echo "  Or build from source with Homebrew:"
        echo "     brew install cmake ninja"
        echo "     # Then follow build instructions in INSTALLATION.md"
    fi
    echo ""
    print_status "After installing SLiM, run this script again."
    exit 1
fi
echo ""

# Offer to create virtual environment
echo "========================================================================"
print_status "Python environment setup"
echo "========================================================================"
echo ""
echo "Would you like to:"
echo "  1) Install packages in user directory (pip install --user)"
echo "  2) Create and use a virtual environment (recommended)"
echo "  3) Install globally (requires sudo/admin)"
echo ""
read -p "Enter choice [1-3] (default: 2): " ENV_CHOICE
ENV_CHOICE=${ENV_CHOICE:-2}

case $ENV_CHOICE in
    1)
        print_status "Installing packages in user directory..."
        INSTALL_CMD="$PIP_CMD install --user"
        ;;
    2)
        print_status "Creating virtual environment..."
        if [ ! -d "venv" ]; then
            $PYTHON_CMD -m venv venv || {
                print_error "Failed to create virtual environment"
                print_error "Try installing with --user instead (option 1)"
                exit 1
            }
            print_success "Virtual environment created"
        else
            print_success "Virtual environment already exists"
        fi
        
        # Activate virtual environment
        print_status "Activating virtual environment..."
        source venv/bin/activate
        print_success "Virtual environment activated"
        
        INSTALL_CMD="pip install"
        ;;
    3)
        print_status "Installing packages globally..."
        print_warning "This may require administrator privileges"
        INSTALL_CMD="pip install"
        ;;
    *)
        print_error "Invalid choice"
        exit 1
        ;;
esac
echo ""

# Install Python packages
print_status "Installing Python packages from requirements.txt..."
echo ""

if [ -f "requirements.txt" ]; then
    $INSTALL_CMD -r requirements.txt || {
        print_error "Failed to install packages"
        print_error "Try updating pip: $PIP_CMD install --upgrade pip"
        exit 1
    }
    print_success "All Python packages installed successfully"
else
    print_error "requirements.txt not found"
    print_error "Make sure you're running this script from the repository root"
    exit 1
fi
echo ""

# Verify installation
echo "========================================================================"
print_status "Verifying installation..."
echo "========================================================================"
echo ""

if [ -f "check_environment.py" ]; then
    $PYTHON_CMD check_environment.py || {
        print_warning "Environment check reported issues"
        print_warning "Please review the output above and fix any problems"
    }
else
    print_warning "check_environment.py not found, skipping verification"
fi
echo ""

# Success message and next steps
echo "========================================================================"
print_success "Setup Complete!"
echo "========================================================================"
echo ""
echo "Next steps:"
echo ""

if [[ $ENV_CHOICE -eq 2 ]]; then
    echo "  1. Activate the virtual environment (if not already active):"
    echo "     source venv/bin/activate"
    echo ""
fi

echo "  2. Start Jupyter Notebook:"
echo "     jupyter notebook divergence_admixture_simulation.ipynb"
echo ""
echo "  3. In the notebook:"
echo "     - Run all cells: Cell → Run All"
echo "     - Or run cells individually with Shift+Enter"
echo ""
echo "  4. Read the documentation:"
echo "     - README.md - Overview and usage"
echo "     - INSTALLATION.md - Detailed installation guide"
echo "     - EXAMPLE_OUTPUT.md - Expected results"
echo ""

if [[ $ENV_CHOICE -eq 2 ]]; then
    echo "  To deactivate virtual environment later:"
    echo "     deactivate"
    echo ""
fi

echo "Happy simulating! 🧬"
echo ""
