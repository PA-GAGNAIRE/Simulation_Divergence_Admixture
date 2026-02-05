# Simulation_Divergence_Admixture

Population divergence followed by admixture simulation using SLiM5 and tskit analysis.

## Overview

This repository contains a Jupyter notebook that simulates and analyzes a demographic model where:
1. An ancestral population splits into two daughter populations
2. The populations diverge independently without gene flow
3. An admixed population is formed by mixing individuals from both daughter populations

## Requirements

### Software
- **SLiM** (version 4.0 or later): Download from https://messerlab.org/slim/
- **Python** (version 3.8 or later)

### Python Packages
Install the required Python packages using:
```bash
pip install -r requirements.txt
```

Required packages:
- jupyter
- tskit
- numpy
- matplotlib
- pandas

### Verify Environment Setup
Run the environment check script to verify your setup:
```bash
python check_environment.py
```

This will verify that Python, SLiM, and all required packages are properly installed.

## Usage

### Running the Notebook

1. **Clone the repository**:
   ```bash
   git clone https://github.com/PA-GAGNAIRE/Simulation_Divergence_Admixture.git
   cd Simulation_Divergence_Admixture
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Start Jupyter Notebook**:
   ```bash
   jupyter notebook divergence_admixture_simulation.ipynb
   ```

4. **Run the notebook**:
   - Execute all cells in order (Cell → Run All)
   - Or run cells individually to explore step-by-step

### Simulation Parameters

The notebook uses the following default parameters (adjustable in the notebook):

- `Na = 1000`: Ancestral population size
- `N1 = 800`: Daughter population 1 size
- `N2 = 1200`: Daughter population 2 size
- `NAdmix = 1000`: Admixed population size
- `Tsplit = 1000`: Generation at which split occurs
- `Tadmix = 2000`: Generation at which admixture occurs
- `f = 0.6`: Admixture fraction from population 1

You can modify these parameters in the notebook to explore different demographic scenarios.

## Output

The notebook produces:
- **SLiM script**: `divergence_admixture.slim` (generated dynamically)
- **Tree sequence**: `simulation_output.trees` (SLiM output)
- **Visualizations**: 
  - Genetic diversity statistics
  - Pairwise divergence (Dxy) matrix
  - FST matrix
  - Site frequency spectra
  - Tree visualization
  - Admixture proportion analysis

## Analysis Components

1. **Tree Sequence Generation**: Uses SLiM5 to simulate a recombining genome with the specified demographic history
2. **Population Genetics Statistics**: Calculates diversity (π), Tajima's D, FST, and divergence
3. **Admixture Analysis**: Examines genetic ancestry proportions in the admixed population
4. **Visualization**: Generates plots for all major statistics and patterns

## Model Details

### Timeline
```
Generation 1      → Ancestral population (p0) of size Na exists
Generation Tsplit → Split into p1 (size N1) and p2 (size N2)
Generation Tadmix → Create admixed population p3 (size NAdmix)
                     p3 receives fraction f from p1 and (1-f) from p2
```

### Genetic Model
- Recombining genome (default: 1 Mb)
- Neutral mutations only
- Wright-Fisher model
- Tree sequence recording enabled

## Troubleshooting

### SLiM not found
If you get "SLiM executable not found", make sure:
- SLiM is installed on your system
- The `slim` command is in your PATH

### Memory issues
For large simulations, reduce:
- Population sizes (Na, N1, N2, NAdmix)
- Genome length
- Simulation duration (Tend)

## Citation

If you use this code, please cite:
- SLiM: Haller and Messer (2023) DOI: 10.1093/molbev/msy228
- tskit: Kelleher et al. (2018) DOI: 10.1371/journal.pcbi.1006581

## License

This project is open source and available under the MIT License.
