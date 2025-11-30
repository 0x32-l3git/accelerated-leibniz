# Cubic Acceleration of the Leibniz Series for $\pi$

## Overview

This repository documents the mathematical proof and computational verification of an independently discovered infinite series for $\pi$.

While investigating rational functions and their summations, a specific cubic denominator was identified that, when summed alternatively, converges to $\pi$ with significantly higher efficiency than the classical Leibniz series. Unlike the standard Leibniz formula which exhibits error decay on the order of $O(1/n)$, this formulation has an error that decays on the order of $O(1/n^3)$.

## The Formula

The series defines $\pi$ through the following identity:

$$ \pi = 3 - \sum_{x=1}^{\infty} \frac{(-1)^x}{2x^3 + 3x^2 + x} $$

## Repository Contents

### 1. [Mathematical Proof](proof.md)
A rigorous step-by-step derivation of the formula.
- **Method:** Partial fraction decomposition and summation of infinite series components.
- **Key Insight:** The decomposition effectively separates the slow-converging logarithmic terms, leaving a rapidly converging remainder.

### 2. [Python Evaluation & Comparison](evaluation.py)
A Python script that numerically verifies the identity and benchmarks it against the standard Leibniz series.
- **Comparison:** Calculates the error margin at specific iteration counts (e.g., $N=314$).
- **Result:** Demonstrates that this series gains accuracy approximately **3x faster** per order of magnitude of iterations compared to the standard method.

## Quick Start

To verify the convergence comparison yourself, run the included Python script:

```bash
python evaluation.py
```

### Performance Snapshot
At the **314th iteration**:
*   **Standard Leibniz:** ~3 decimal digits of accuracy.
*   **This Cubic Series:** ~8 decimal digits of accuracy.

By $x=314$, this series achieves about 5 extra digits of accuracy (i.e., the error is ~10^5 times smaller than Leibniz).
