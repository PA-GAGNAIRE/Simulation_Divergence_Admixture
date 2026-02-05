# Simulation_Divergence_Admixture

Population divergence followed by admixture simulation using SLiM5 and tskit analysis.

## Overview

This repository contains a Jupyter notebook that simulates and analyzes a demographic model where:
1. An ancestral population reaches mutation-drift equilibrium (using recapitation)
2. The population splits into two daughter populations
3. The populations diverge independently without gene flow
4. An admixed population is formed by mixing individuals from both daughter populations

### Key Features

- **Recapitation**: Uses tskit's recapitation to simulate coalescent history and ensure mutation-drift equilibrium in the ancestral population
- **Explicit Mutation Simulation**: Mutations are added after the simulation using tskit.mutate(), allowing precise tracking of mutation origins
- **Dxy Decomposition**: Analyzes genetic divergence (Dxy) by decomposing it into:
  - Ancestral polymorphism (mutations present before population split)
  - New mutations (arising independently after split)
- **Parameter Sweeps**: Explores how Dxy components change with split time
- **Comprehensive Visualizations**: Multi-panel figures showing Dxy accumulation, rates, and theoretical comparisons

## Requirements

### Software
- **SLiM** (version 4.0 or later recommended, SLiM 4.1+ for best compatibility): Download from https://messerlab.org/slim/
  - Note: This notebook uses SLiM's tree sequence recording features available in SLiM 4.0+
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
- `Tburn = 10 * Na`: Burn-in time for mutation-drift equilibrium (recapitation)
- `N1 = 800`: Daughter population 1 size
- `N2 = 1200`: Daughter population 2 size
- `NAdmix = 1000`: Admixed population size
- `Tsplit = 1000`: Generation at which split occurs (after burn-in)
- `Tadmix = 2000`: Generation at which admixture occurs (after burn-in)
- `f = 0.6`: Admixture fraction from population 1
- `genome_length = 1e6`: Simulated genome length (1 Mb)
- `recomb_rate = 1e-8`: Recombination rate per bp per generation
- `mutation_rate = 1e-8`: Mutation rate per bp per generation

You can modify these parameters in the notebook to explore different demographic scenarios.

## Output

The notebook produces:
- **SLiM script**: `divergence_admixture.slim` (generated dynamically)
- **Tree sequence**: `simulation_output.trees` (SLiM output, without mutations)
- **Recapitated & Mutated tree sequence**: Contains full coalescent history with explicit mutations
- **Visualizations**: 
  - Genetic diversity statistics (π, Tajima's D)
  - Pairwise divergence (Dxy) matrix
  - FST matrix
  - Site frequency spectra
  - Tree visualization
  - **Dxy decomposition by mutation origin** (ancestral vs. new)
  - **Dxy vs split time analysis** (parameter sweep)
  - Admixture proportion analysis
  - **Local ancestry mosaics** showing recombined ancestries along genomes
    - F1 hybrids (balanced 50:50 ancestry)
    - F2 hybrids (increased recombination)
    - Backcross patterns (skewed ancestry)
    - Late-generation hybrids (fine-scale mosaic)
  - Ancestry block size distributions

## Analysis Components

1. **Tree Sequence Generation**: Uses SLiM to simulate a recombining genome with the specified demographic history (without mutations)
2. **Recapitation**: Adds coalescent history before the forward simulation to ensure mutation-drift equilibrium
3. **Explicit Mutation Simulation**: Adds mutations using tskit.mutate() after recapitation, enabling precise tracking of mutation origins
4. **Mutation Origin Tracking**: Classifies each mutation as either:
   - **Ancestral**: Present in the ancestral population before split
   - **New**: Arose independently in descendant populations after split
5. **Dxy Decomposition**: Partitions genetic divergence into contributions from ancestral polymorphism vs. new mutations
6. **Parameter Sweeps**: Explores how Dxy components change with varying split times
7. **Population Genetics Statistics**: Calculates diversity (π), Tajima's D, FST, and divergence
8. **Admixture Analysis**: Examines genetic ancestry proportions in the admixed population
9. **Local Ancestry Tracking**: Traces genomic segments back through the genealogy to determine source population
   - Tracks ancestry along the genome at fine spatial resolution
   - Identifies recombination breakpoints between ancestries
   - Classifies individuals as F1-like, F2-like, backcross-like, or late-generation based on patterns
10. **Comprehensive Visualization**: Multi-panel figures showing temporal dynamics and theoretical comparisons

## Model Details

### Timeline
```
Recapitation      → Coalescent history simulated backward (Tburn generations)
Generation 1      → Ancestral population (p0) of size Na exists
Generation Tsplit → Split into p1 (size N1) and p2 (size N2)
Generation Tadmix → Create admixed population p3 (size NAdmix)
                     p3 receives fraction f from p1 and (1-f) from p2
Mutation addition → Mutations added to entire tree sequence using tskit.mutate()
```

### Genetic Model
- Recombining genome (default: 1 Mb)
- Neutral mutations added post-hoc (not during forward simulation)
- Mutation-drift equilibrium ensured via recapitation
- Wright-Fisher model
- Tree sequence recording enabled

## Dxy Decomposition Analysis

One of the key features of this notebook is the ability to decompose genetic divergence (Dxy) into its components:

### Mutation Classification

Each mutation is classified based on when it arose relative to the population split:
- **Ancestral polymorphism**: Mutations that arose before the split (time > Tend - Tsplit)
- **New mutations**: Mutations that arose after the split in either population

### Dxy Components

The total divergence between two populations can be decomposed as:

```
Total Dxy = Ancestral Dxy + New Dxy
```

Where:
- **Ancestral Dxy**: Divergence due to alleles segregating in the ancestral population
- **New Dxy**: Divergence due to mutations arising independently after the split

### Theoretical Expectations

- Ancestral contribution should remain relatively constant regardless of split time
- New mutation contribution should increase linearly with split time: `New Dxy ≈ 2μT`
  - where μ is the mutation rate and T is the split time
- The rate of Dxy accumulation should equal `2μ` (twice the mutation rate)

### Visualizations

The notebook produces several visualizations:
1. **Bar plot**: Absolute contributions of each component
2. **Stacked area plot**: Dxy components over time
3. **Proportions**: Relative contributions as a function of split time
4. **Accumulation rates**: Rate of Dxy increase, compared to theoretical expectation

## Local Ancestry Visualization

The notebook includes comprehensive visualization of how hybridization creates genomic mosaics through recombination. This analysis shows local ancestry patterns across different hybrid generations:

### What is Visualized

For each individual in the admixed population, the analysis traces genomic segments back through the tree sequence to determine which source population (Population 1 or Population 2) each segment originated from.

### Hybrid Generation Types

The visualization categorizes individuals into four types based on their ancestry patterns:

1. **F1-like Hybrids**
   - Balanced ancestry (~50% from each parent population)
   - Large, continuous blocks of ancestry
   - Few recombination breakpoints
   - Represents first-generation crosses

2. **F2-like Hybrids**
   - Balanced ancestry but more recombination
   - Intermediate number of ancestry blocks
   - Represents second-generation offspring

3. **Backcross-like Hybrids**
   - Skewed ancestry (e.g., 75% from one parent, 25% from other)
   - Results from crossing F1 back to one parental population
   - Asymmetric patterns

4. **Late-generation Hybrids**
   - Fine-scale mosaic with many small ancestry blocks
   - Numerous recombination breakpoints
   - Results from multiple generations of admixture

### Color Coding

- **Blue**: Ancestry from Population 1
- **Red**: Ancestry from Population 2  
- **Gray**: Ancestral (pre-split) or uncertain ancestry

### Block Size Analysis

The analysis also provides:
- Distribution of ancestry block sizes for each population
- Statistics on block lengths (mean, median, max)
- Number of recombination breakpoints per individual
- Histograms showing block size distributions

### Interpretation

These visualizations demonstrate:
- How recombination breaks up parental genomes over generations
- The stochastic nature of inheritance and recombination
- Differences between early and late-generation hybrids
- The genomic signature of different admixture scenarios

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
