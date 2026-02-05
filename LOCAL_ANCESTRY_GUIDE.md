# Local Ancestry Visualization Guide

## Overview

The local ancestry visualization feature allows you to see how hybridization generates a mosaic of recombined ancestries along the genome. This is a powerful way to understand the genomic consequences of admixture and recombination over multiple generations.

## What is Local Ancestry?

Local ancestry refers to determining, for each segment of an individual's genome, which ancestral population that segment originated from. In our simulation with two source populations (p1 and p2), each genomic segment can be traced back to one of these populations through the tree sequence genealogy.

## How It Works

### 1. Ancestry Tracking

The `get_local_ancestry()` function traces each genomic position back through the tree sequence:

```python
def get_local_ancestry(ts, sample_node, pop1_id=1, pop2_id=2, num_windows=100):
    # Divides genome into windows
    # For each window, traces genealogy back to source populations
    # Returns ancestry classification for each window
```

**Key Steps:**
1. Divide the genome into windows (default: 200 windows)
2. For each window, find the tree at that genomic position
3. Trace the sample node's ancestry up the tree
4. Identify which source population the lineage passes through
5. Classify the window as coming from Population 1, 2, or ancestral

### 2. Visualization

The `plot_local_ancestry()` function creates visual representations:
- Each individual is shown as a horizontal bar
- Genomic position along the x-axis
- Colors indicate ancestry origin:
  - **Blue** = Population 1
  - **Red** = Population 2
  - **Gray** = Ancestral/uncertain

## Hybrid Generation Types

### F1 Hybrids (First Generation)

**Characteristics:**
- Direct offspring of crosses between p1 and p2
- ~50% ancestry from each parent
- Large, continuous blocks of ancestry
- Few recombination breakpoints (typically 1-3 per chromosome)

**Expected Pattern:**
```
Chromosome: |████████████|■■■■■■■■■■■■|
            Pop1 (50%)    Pop2 (50%)
```

**Interpretation:**
- One chromosome copy from each parent
- Minimal recombination in first generation
- Block boundaries correspond to chromosome ends or rare crossovers

### F2 Hybrids (Second Generation)

**Characteristics:**
- Offspring of F1 × F1 crosses
- Still ~50% from each source on average
- More recombination breakpoints (typically 3-8 per chromosome)
- Smaller ancestry blocks than F1

**Expected Pattern:**
```
Chromosome: |████|■■■|████|■■■■■|████|■■|
            Pop1  Pop2 Pop1  Pop2  Pop1 P2
```

**Interpretation:**
- Recombination in F1 parents creates mosaic patterns
- Chromosome copies are mixtures of both ancestries
- Block sizes reflect one generation of recombination

### Backcross Hybrids

**Characteristics:**
- F1 crossed back to one parental population
- Skewed ancestry (typically 75% from one parent, 25% from other)
- Intermediate block sizes
- Asymmetric pattern

**Expected Pattern:**
```
Chromosome: |████████████|■■|████████|■|████|
            Pop1 (75%)     P2  Pop1    P2 Pop1
```

**Interpretation:**
- Useful for introgression studies
- Shows how minority ancestry is distributed
- Pattern depends on which parent was used for backcross

### Late-Generation Hybrids

**Characteristics:**
- Multiple generations of admixture
- Fine-scale mosaic pattern
- Many small ancestry blocks
- Numerous recombination breakpoints (10+ per chromosome)
- Ancestry proportions may vary from 50:50

**Expected Pattern:**
```
Chromosome: |██|■|█|■■|█|■|██|■|█|■■■|█|■|█|■|
            Fine-scale mosaic with many switches
```

**Interpretation:**
- Cumulative effect of recombination over generations
- Approaches random mixing at the fine scale
- Useful for detecting recent vs. ancient admixture

## Ancestry Block Analysis

### Block Size Statistics

For each individual, the analysis reports:
- **Total blocks**: Number of continuous ancestry segments
- **Mean block size**: Average length of blocks from each population
- **Median block size**: Middle value (less affected by outliers)
- **Max block size**: Largest continuous segment
- **Recombination breakpoints**: Number of switches between ancestries

### Block Size Distributions

The histograms show:
- **Exponential-like distribution**: Many small blocks, few large blocks
- **Long tail**: Some very large blocks persist for many generations
- **Generation effect**: Older admixture has smaller mean block size

### Theoretical Expectations

Block size is related to:
- Number of generations since admixture (g)
- Recombination rate (r)
- Chromosome length (L)

Expected mean block size: `E[block size] ≈ 1 / (g × r × L)`

## Practical Applications

### 1. Identifying Hybrid Generation

Compare observed patterns to expectations:
- Large blocks + balanced ancestry → F1-like
- Medium blocks + balanced ancestry → F2-like
- Large blocks + skewed ancestry → Backcross-like
- Small blocks regardless of proportions → Late-generation

### 2. Detecting Admixture Timing

- Block size distribution indicates time since admixture
- Larger blocks suggest more recent admixture
- Uniform small blocks suggest ancient admixture

### 3. Understanding Recombination

- Breakpoint counts reveal recombination activity
- Block boundaries mark historical recombination events
- Patterns show how recombination breaks up parental genomes

### 4. Introgression Studies

- Identify which genomic regions come from which source
- Track minority ancestry through backcrossing
- Understand adaptive introgression patterns

## Limitations and Considerations

### 1. Resolution

- Window size affects resolution (default: 200 windows)
- Very small blocks may not be detected
- Increase windows for finer resolution (trade-off with computation)

### 2. Uncertainty

- Gray color indicates uncertain or ancestral ancestry
- Can occur when lineages coalesce before the split
- More common in older parts of the tree

### 3. Simulation Parameters

- Results depend on:
  - Split time (Tsplit)
  - Admixture time (Tadmix)  
  - Recombination rate
  - Population sizes
  - Time since admixture (Tend - Tadmix)

### 4. Sample Size

- More samples provide better population-level patterns
- Individual variation is expected due to stochastic recombination
- Default shows up to 8 samples for clarity

## Customization

### Adjusting Window Number

```python
# Finer resolution (more computational)
windows, ancestry = get_local_ancestry(ts, sample_node, num_windows=500)

# Coarser resolution (faster)
windows, ancestry = get_local_ancestry(ts, sample_node, num_windows=50)
```

### Selecting Specific Samples

```python
# Analyze specific samples
my_samples = [pop_samples[3][0], pop_samples[3][5]]
ancestry_results = []
for sample in my_samples:
    windows, ancestry = get_local_ancestry(ts, sample)
    ancestry_results.append(ancestry)
```

### Custom Visualization

```python
# Create custom plot with specific samples
fig, ax = plt.subplots(figsize=(14, 3))
plot_local_ancestry(windows, ancestry_results, ax, 
                   'My Custom Title',
                   sample_labels=['Sample A', 'Sample B'])
```

## Interpreting Results

### Key Questions to Ask

1. **Are ancestry proportions balanced?**
   - Yes → F1 or F2 pattern
   - No → Backcross or unbalanced admixture

2. **How many breakpoints?**
   - Few (1-3) → F1-like
   - Medium (4-10) → F2-like or recent admixture
   - Many (>10) → Late-generation or ancient admixture

3. **What's the block size distribution?**
   - Uniform large blocks → F1
   - Mixed sizes → F2 or backcross
   - Many small blocks → Late-generation

4. **Are patterns consistent across individuals?**
   - Yes → Same generation/history
   - No → Mixed hybrid classes or variable history

### Common Patterns

**Pattern 1: Single Large Block**
- Interpretation: Recent introgression event
- One parent contributed most of this chromosome

**Pattern 2: Alternating Blocks**
- Interpretation: F1 pattern with few recombinations
- Typical of first-generation hybrids

**Pattern 3: Checkerboard Pattern**
- Interpretation: Multiple generations of recombination
- Fine-scale mixing of ancestries

**Pattern 4: Skewed with Few Minority Blocks**
- Interpretation: Backcross pattern
- Minority ancestry in discrete segments

## Future Extensions

Possible enhancements to try:
1. Three-way admixture (add a third source population)
2. Temporal series (track how patterns change over generations)
3. Haplotype phasing (separate maternal/paternal chromosomes)
4. Linkage disequilibrium around breakpoints
5. Selection signatures (detect regions with skewed ancestry)

## References

- **Tree sequence methods**: Kelleher et al. (2018) PLOS Comp Biol
- **Local ancestry inference**: Gravel (2012) Genetics
- **Admixture models**: Liang & Nielsen (2014) Genetics
- **Recombination and ancestry**: Pool & Nielsen (2009) Genetics

## Summary

Local ancestry visualization provides insights into:
- How recombination creates genomic mosaics
- Differences between hybrid generations
- Distribution of ancestry along chromosomes
- Timing and mode of admixture events

This powerful tool helps understand the genomic architecture of admixed populations and the evolutionary consequences of hybridization.
