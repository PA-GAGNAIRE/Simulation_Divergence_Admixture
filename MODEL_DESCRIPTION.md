# Demographic Model Documentation

## Visual Representation

```
Generation Timeline:

Gen 1       Ancestral Population (p0)
|           Size = Na
|           ┌─────────┐
|           │   p0    │
|           │  (Na)   │
|           └─────────┘
|                │
|                │
v                │
Gen Tsplit       ├──────────────┐
|                │              │
|                v              v
|           ┌─────────┐    ┌─────────┐
|           │   p1    │    │   p2    │
|           │  (N1)   │    │  (N2)   │
|           └─────────┘    └─────────┘
|                │              │
|                │              │
|           (No gene flow)      │
|                │              │
v                │              │
Gen Tadmix       │              │
|                │              │
|                ├──────┬───────┤
|                │  f   │ (1-f) │
|                │      │       │
|                v      v       v
|           ┌─────────┐    ┌─────────┐
|           │   p1    │    │   p2    │
|           │  (N1)   │    │  (N2)   │
|           └─────────┘    └─────────┘
|                              
|                └──────┬───────┘
|                       │
|                       v
|                  ┌─────────┐
|                  │   p3    │
|                  │(NAdmix) │
|                  └─────────┘
|                       │
|                       │
v                       │
Gen Tend                v
                   End of simulation
```

## Mathematical Description

### Population History

1. **Initial State (Generation 1)**
   - Single ancestral population p0
   - Size: Na individuals
   - All lineages coalesce in p0

2. **Population Split (Generation Tsplit)**
   - p0 splits into two daughter populations
   - Population p1: N1 individuals (derived from p0)
   - Population p2: N2 individuals (derived from p0)
   - p0 is removed (size set to 0)
   - Migration rate between p1 and p2: m = 0 (no gene flow)

3. **Divergence Period (Generations Tsplit to Tadmix)**
   - Duration: Δt₁ = Tadmix - Tsplit generations
   - p1 and p2 evolve independently
   - Genetic drift operates in each population
   - Expected divergence accumulates: Dxy ∝ Δt₁

4. **Admixture Event (Generation Tadmix)**
   - New population p3 created with NAdmix individuals
   - Admixture proportions:
     * Fraction f from p1
     * Fraction (1-f) from p2
   - Expected number from p1: f × NAdmix
   - Expected number from p2: (1-f) × NAdmix
   - Migration rates set for one generation:
     * m₁→₃ = f (migration from p1 to p3)
     * m₂→₃ = 1-f (migration from p2 to p3)

5. **Post-Admixture (Generations Tadmix+1 to Tend)**
   - Duration: Δt₂ = Tend - Tadmix generations
   - Migration rates set to 0
   - p3 evolves independently
   - All populations continue until Tend

### Genetic Expectations

#### Within-Population Diversity (π)

For a neutral, constant-size population:
```
π = 4Neμ
```
where:
- Ne = effective population size
- μ = mutation rate per site per generation

Expected relative diversity:
- π₁ ∝ 4N₁μ
- π₂ ∝ 4N₂μ
- π₃ ≈ f²π₁ + (1-f)²π₂ + 2f(1-f)Dxy₁₂ (immediately post-admixture)

#### Between-Population Divergence (Dxy)

For populations diverged at time T:
```
Dxy = 2μT (for T >> Ne)
```

Expected divergence:
- Dxy₁₂ = divergence between p1 and p2 ≈ 2μ(Tadmix - Tsplit)
- Dxy₁₃ = divergence between p1 and p3 ≈ (1-f)Dxy₁₂
- Dxy₂₃ = divergence between p2 and p3 ≈ f × Dxy₁₂

#### FST (Population Differentiation)

```
FST = (Dxy - (π₁+π₂)/2) / Dxy
```

Expected FST:
- FST₁₂: High (long divergence, no gene flow)
- FST₁₃, FST₂₃: Moderate (recent admixture reduces differentiation)

#### Site Frequency Spectrum

Expected shape under neutrality:
```
E[ξᵢ] = θ/i
```
where:
- ξᵢ = number of sites with i derived alleles
- θ = 4Neμ
- i = allele count

Departures from expectation indicate:
- Positive Tajima's D: balancing selection or population structure
- Negative Tajima's D: population expansion or purifying selection

### Admixture Proportion Estimation

From divergence data:
```
f_estimated = 1 - (Dxy₁₃ / Dxy₁₂)
```

This assumes:
- Dxy₁₂ represents full divergence between source populations
- Dxy₁₃ is proportional to ancestry from p2
- No continued gene flow after admixture

### Parameter Constraints

For a valid simulation:
1. All population sizes must be positive integers:
   - Na, N1, N2, NAdmix > 0

2. Temporal ordering must be logical:
   - 1 < Tsplit < Tadmix < Tend

3. Admixture fraction must be valid:
   - 0 ≤ f ≤ 1

4. Genetic parameters must be positive:
   - genome_length > 0
   - recomb_rate ≥ 0
   - mutation_rate ≥ 0

### Computational Considerations

#### Memory Usage
Tree sequence memory scales with:
- O(N × L × R) where:
  - N = total sample size
  - L = sequence length
  - R = recombination rate × generations

#### Runtime
Simulation time scales approximately:
- O(T × N²) for Wright-Fisher model
- Can be reduced with:
  - Smaller population sizes
  - Shorter sequence length
  - Fewer generations

#### Accuracy
Genetic estimates improve with:
- Larger sample sizes (more statistical power)
- Longer sequences (more segregating sites)
- Higher mutation rates (more polymorphism)

## References

### Key Papers

1. **SLiM 4**:
   Haller, B. C., & Messer, P. W. (2023). SLiM 4: Multispecies Eco-Evolutionary Modeling. 
   *American Naturalist*, 201(5), E127-E139.

2. **Tree Sequences**:
   Kelleher, J., et al. (2018). Efficient Coalescent Simulation and Genealogical Analysis 
   for Large Sample Sizes. *PLOS Computational Biology*, 14(11), e1006581.

3. **Admixture Theory**:
   Patterson, N., et al. (2012). Ancient Admixture in Human History. 
   *Genetics*, 192(3), 1065-1093.

4. **FST Estimation**:
   Hudson, R. R., et al. (1992). Estimation of Levels of Gene Flow from DNA Sequence Data. 
   *Genetics*, 132(2), 583-589.

### Software Documentation

- SLiM Manual: https://messerlab.org/slim/
- tskit Documentation: https://tskit.dev/
- Python libraries: numpy, matplotlib, pandas
