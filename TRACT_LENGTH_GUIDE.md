# Tract Length Decay Analysis Guide

## Overview

This guide explains the analysis of admixture tract length decay over time, a fundamental process in population genetics that results from recombination breaking up ancestry blocks in admixed populations.

## What is Tract Length Decay?

After two populations mix (admixture event), their genomes initially form large continuous blocks of ancestry from each source population. Over subsequent generations, recombination progressively breaks these blocks into smaller segments, creating a mosaic pattern that becomes increasingly fine-grained with time.

The rate of this decay provides information about:
- How long ago the admixture occurred
- The recombination rate in the population
- The proportion of ancestry from each source

## Theoretical Background

### The Formula

The mean length of ancestry tracts from one source population decreases according to:

**L = 1 / [(1-h) × r × (t-1)]**

Where:
- **L** = mean tract length (in base pairs)
- **h** = hybrid index (proportion of genome from population 1)
- **r** = recombination rate per base pair per generation
- **t** = number of generations since admixture formation

### Key Insights

1. **Hyperbolic Decay**: Tract length decreases as 1/(t-1), not exponentially
   - Very rapid decay in first few generations
   - Progressively slower decay over time
   - Never reaches zero (always some long tracts by chance)

2. **Role of Recombination**: Higher r means faster decay
   - Each recombination event can break an ancestry block
   - Expected number of breakpoints per chromosome ≈ r × L × (t-1)
   - Physical linkage determines minimum tract size

3. **Hybrid Index Effect**: The (1-h) term accounts for asymmetry
   - When h ≈ 0.5 (balanced admixture), decay is fastest
   - When h is extreme (e.g., 0.1 or 0.9), decay is slower
   - Reflects probability of having both ancestries to recombine between

4. **Time Dependence**: The (t-1) term
   - Subtracting 1 accounts for the generation of admixture itself
   - At t=1 (immediately after admixture), formula undefined
   - At t=2, mean tract length already substantially reduced

## Implementation in the Notebook

### Step 1: Tract Extraction

The analysis uses the local ancestry data already computed:

```python
# Extract all Population 1 ancestry tracts
for ancestry in ancestry_results:
    # Find runs of population 1 ancestry
    current_anc = ancestry[0]
    block_start = 0
    
    for j in range(1, len(ancestry)):
        if ancestry[j] != current_anc:
            if current_anc == 1:  # Pop 1 tract
                block_length = (j - block_start) * window_size
                pop1_tract_lengths.append(block_length)
```

### Step 2: Calculate Statistics

Basic descriptive statistics:
- Mean tract length
- Median tract length (robust to outliers)
- Min/max tract lengths
- Number of tracts

### Step 3: Calculate Hybrid Index

```python
h = total_pop1_ancestry / total_windows
```

This represents the genome-wide proportion from Population 1.

### Step 4: Calculate Time Since Admixture

```python
t = Tend - Tadmix
```

Number of generations that have elapsed since the admixture event.

### Step 5: Analytical Prediction

```python
predicted_mean_length = 1.0 / ((1 - h) * recomb_rate * (t - 1))
```

Applies the theoretical formula using observed parameters.

### Step 6: Comparison

```python
ratio = observed_mean / predicted_mean
```

Ratio close to 1.0 indicates good agreement with theory.

## Visualizations

### Panel 1: Tract Length Distribution

A histogram showing:
- Distribution of all observed tract lengths
- Red dashed line: Observed mean
- Green dashed line: Theoretical prediction
- X-axis in kb for readability

**What to look for:**
- Exponential-like distribution (many short, few long tracts)
- Long right tail (some very long tracts persist)
- Mean position relative to distribution mode
- Agreement between observed and predicted means

### Panel 2: Decay Curve

A plot showing:
- X-axis: Generations since admixture (t)
- Y-axis: Mean tract length (kb)
- Green curve: Analytical prediction L = 1/[(1-h)r(t-1)]
- Red point: Observed value at current time
- Parameter box showing h, r, and t

**What to look for:**
- Hyperbolic decay shape (rapid then slow)
- Observed point near predicted curve
- Steeper decline at early time points
- Asymptotic approach to small values

## Multi-Generation Analysis (Optional)

### Purpose

To see the complete decay pattern, not just a single time point.

### How It Works

1. Runs multiple SLiM simulations with different end times
2. Extracts tract lengths at t = 1, 2, 3, 5, 10, 20, 50 generations
3. Plots all points against analytical curve
4. Shows full trajectory from admixture to late generations

### Interpretation

- Early rapid decay visible as steep curve segment
- Later slower decay visible as flattening
- Individual points may deviate due to stochasticity
- Overall trend should match 1/(t-1) relationship

### When to Use

- Validating simulation accuracy
- Understanding full dynamics
- Educational demonstrations
- Publication-quality figures

**Note**: Time-consuming (multiple simulations), disabled by default.

## Expected Patterns

### Typical Values

For a simulation with:
- r = 1e-8 per bp per generation
- h = 0.5 (balanced admixture)
- Genome length = 1 Mb
- t = 10 generations

Expected mean tract length:
```
L = 1 / [(1-0.5) × 1e-8 × (10-1)]
L = 1 / [0.5 × 1e-8 × 9]
L = 1 / 4.5e-8
L ≈ 22,222,222 bp ≈ 22 Mb
```

But our genome is only 1 Mb, so tracts are capped at that length.

For longer times (t=100):
```
L = 1 / [(1-0.5) × 1e-8 × 99]
L ≈ 202,020 bp ≈ 202 kb
```

Now within genome length, so more realistic.

### Generation-Specific Patterns

**t = 2-5 generations**:
- Mean tract length: Very long (100s of kb to Mb)
- Distribution: Broad, right-skewed
- Variance: High between individuals
- Interpretation: Recent admixture, little recombination

**t = 5-20 generations**:
- Mean tract length: Moderate (10s to 100s of kb)
- Distribution: Exponential-like
- Variance: Moderate
- Interpretation: Active decay phase

**t = 20-100 generations**:
- Mean tract length: Short (few to tens of kb)
- Distribution: Concentrated at small values
- Variance: Low (more uniform)
- Interpretation: Old admixture, well-mixed

**t > 100 generations**:
- Mean tract length: Very short (few kb)
- Distribution: Tight, peaked at small values
- Variance: Minimal
- Interpretation: Ancient admixture, approaching equilibrium

## Factors Affecting Agreement

### 1. Window Resolution

The genome is divided into windows for computational efficiency:
- Smaller windows → Better resolution but slower
- Larger windows → Faster but may miss small tracts
- Default 200 windows balances speed and accuracy
- Very short tracts (< window size) cannot be detected

**Effect**: Slight overestimation of mean tract length

### 2. Sample Size

Number of individuals analyzed:
- More samples → Better population estimate
- Fewer samples → More stochastic variation
- Default 8 samples is reasonable
- Consider more for rigorous validation

**Effect**: Variance in observed mean

### 3. Genome Length

Simulation uses finite genome:
- Very long tracts may be capped by chromosome ends
- Small genome (1 Mb) → More edge effects
- Larger genome → More realistic but slower
- Theory assumes infinite genome

**Effect**: Slight underestimation of mean tract length for recent admixture

### 4. Stochastic Effects

Recombination is random:
- Individual tracts vary substantially
- Some long tracts persist by chance
- Distribution has long right tail
- Average over many tracts/individuals improves estimate

**Effect**: Variance around theoretical prediction

### 5. Model Assumptions

Theory assumes:
- Single pulse admixture (no ongoing gene flow)
- Random mating after admixture
- Constant population size
- No selection
- Uniform recombination rate

Violations of these assumptions cause deviations.

## Applications

### 1. Dating Admixture Events

If you measure tract lengths in real data:
```
t = 1 + 1/[(1-h) × r × L]
```

Where you estimate:
- h from genome-wide ancestry proportions
- r from recombination maps
- L from observed mean tract length

Solve for t to estimate time since admixture.

**Example**: 
- Observed L = 100 kb
- h = 0.6
- r = 1e-8

```
t = 1 + 1/[(1-0.6) × 1e-8 × 100,000]
t = 1 + 1/[0.4 × 0.001]
t = 1 + 1/0.0004
t = 1 + 2,500
t = 2,501 generations
```

At ~25 years per generation, that's ~62,500 years ago.

### 2. Estimating Recombination Rate

If you know when admixture occurred:
```
r = 1/[(1-h) × L × (t-1)]
```

Useful for species where recombination maps are uncertain.

### 3. Identifying Multiple Admixture Events

Different tracts may show different decay patterns:
- Bimodal distribution suggests two admixture pulses
- Different source populations may have different h values
- Can decompose by source ancestry

### 4. Detecting Selection

Tracts that are:
- Unusually long → Possible positive selection maintaining ancestry
- Unusually short → Possible negative selection breaking up ancestry
- Comparing observed to null (neutral) model identifies outliers

### 5. Understanding Population History

Tract length distributions contain information about:
- Number of admixture events
- Relative timing of events
- Effective population size changes
- Gene flow patterns

## Troubleshooting

### Problem: No tracts found

**Possible causes:**
- Admixture fraction is 0 or 1 (no mixing)
- Sample from wrong population
- All ancestry classified as "ancestral"

**Solutions:**
- Check admixture parameters (f should be between 0 and 1)
- Verify analyzing population p3 (admixed)
- Check ancestry classification threshold

### Problem: Predicted mean = infinity or very large

**Possible causes:**
- t = 1 (immediately after admixture)
- h very close to 0 or 1
- Recombination rate = 0

**Solutions:**
- Ensure t > 1 (run longer simulation)
- Check hybrid index calculation
- Verify recombination rate is positive

### Problem: Poor agreement (ratio far from 1)

**Possible causes:**
- Too few samples
- Window resolution too coarse
- Genome too short
- Stochastic variation

**Solutions:**
- Increase number of samples analyzed
- Increase number of windows (num_windows parameter)
- Use larger genome
- Run multiple simulations and average

### Problem: All tracts same length

**Possible causes:**
- Window size larger than tract length variation
- Not enough generations for recombination
- Numerical precision issues

**Solutions:**
- Increase window number for finer resolution
- Run simulation longer
- Check that recombination is occurring

## Best Practices

1. **Multiple Simulations**: Run several replicate simulations to estimate variance

2. **Appropriate Time Scale**: Choose simulation duration to see meaningful decay
   - Too short → No decay observable
   - Too long → Tracts very small, harder to measure

3. **Sufficient Genome Length**: Use genomes long enough to contain multiple tracts
   - 1 Mb minimum
   - 10+ Mb better for late-generation analysis

4. **Balanced Sampling**: Sample equally from all individuals
   - Avoid bias toward particular lineages
   - Use random sampling

5. **Parameter Validation**: Compare multiple approaches
   - Direct measurement
   - Theoretical prediction
   - Alternative methods (e.g., local ancestry inference tools)

6. **Documentation**: Record all parameters
   - Recombination rate
   - Admixture timing
   - Population sizes
   - Enables reproducibility

## Further Reading

### Key Papers

1. **Pool & Nielsen (2009)**: "Inference of historical changes in migration rate from the lengths of migrant tracts"
   - Original derivation of tract length formula
   - Genetics 181: 711-719

2. **Gravel (2012)**: "Population Genetics Models of Local Ancestry"
   - Comprehensive theoretical framework
   - Genetics 191: 607-619

3. **Liang & Nielsen (2014)**: "The Lengths of Admixture Tracts"
   - Extensions for multiple admixture events
   - Genetics 197: 953-967

4. **Browning et al. (2018)**: "Analysis of Human Sequence Data Reveals Two Pulses of Archaic Denisovan Admixture"
   - Application to ancient admixture
   - Cell 173: 53-61

### Tools

- **RFMix**: Local ancestry inference from genetic data
- **HAPMIX**: HMM-based ancestry inference
- **ELAI**: Efficient local ancestry inference
- **Loter**: Local ancestry reconstruction

## Summary

Tract length decay analysis provides:
- Quantitative measure of admixture timing
- Validation of simulation accuracy
- Understanding of recombination dynamics
- Connection between theory and observation

The analytical formula L = 1/[(1-h)r(t-1)] captures the essential physics:
- Recombination breaks up tracts
- Rate depends on r and time
- Asymmetry captured by hybrid index
- Hyperbolic decay pattern

This analysis bridges population genetics theory and genomic data, offering both scientific insight and practical applications for understanding admixed populations.
