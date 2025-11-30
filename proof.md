# Proof: The Cubic Acceleration of the Leibniz Series

## 1. Introduction

This document presents a formal proof and analysis of a specific infinite alternating series. While the classical Leibniz series for $\pi$ is mathematically elegant, it is computationally inefficient due to its slow error decay on the order of $1/n$. Through an independent discovery, it was found that a specific rational function, when summed, acts as a cubic accelerator for the calculation of $\pi$.

By manipulating the algebraic structure of the summands, this series effectively cancels out the slow-converging logarithmic “noise” built into the Leibniz series, leaving an expression that converges to $\pi$ with an error term that decays on the order of $1/n^3$.

We define the identity as

```math
3 - \sum_{x=1}^{\infty} \frac{(-1)^x}{2x^3 + 3x^2 + x} = \pi.
````

## 2. Factorization and Decomposition

Let $S$ be the infinite sum

```math
S = \sum_{x=1}^{\infty} a_x, \quad \text{where } a_x = \frac{(-1)^x}{2x^3 + 3x^2 + x}.
```

We first factor the denominator:

```math
D(x) = x(2x^2 + 3x + 1) = x(2x+1)(x+1).
```

Using partial fraction decomposition, we write

```math
\frac{1}{x(x+1)(2x+1)} = \frac{A}{x} + \frac{B}{x+1} + \frac{C}{2x+1}.
```

Multiplying both sides by $x(x+1)(2x+1)$ gives

```math
1 = A(2x+1)(x+1) + Bx(2x+1) + Cx(x+1).
```

Equating coefficients of like powers of $x$ yields $A = 1$, $B = 1$, and $C = -4$, so

```math
\frac{1}{x(x+1)(2x+1)} = \frac{1}{x} + \frac{1}{x+1} - \frac{4}{2x+1}.
```

Thus, our series becomes a linear combination of three simpler alternating series:

```math
S = \sum_{x=1}^{\infty} (-1)^x \left( \frac{1}{x} + \frac{1}{x+1} - \frac{4}{2x+1} \right).
```

## 3. Evaluation of the Component Series

We evaluate the infinite sums of the decomposed parts.

1. **Part A.**

   ```math
   \sum_{x=1}^{\infty} \frac{(-1)^x}{x} = -\ln 2.
   ```

2. **Part B.**

   ```math
   \sum_{x=1}^{\infty} \frac{(-1)^x}{x+1} = \ln 2 - 1.
   ```

3. **Part C.**

   ```math
   -4 \sum_{x=1}^{\infty} \frac{(-1)^x}{2x+1} = 4 - \pi.
   ```

Summing these components,

```math
S = -\ln 2 + (\ln 2 - 1) + (4 - \pi) = 3 - \pi.
```

Rearranging for $\pi$,

```math
\pi = 3 - S.
```

## 4. Convergence Analysis: Accelerated Leibniz Series

This series is effectively a “masked” version of the Leibniz series, but with vastly superior convergence properties.

The standard Leibniz series is

```math
\frac{\pi}{4} = \sum_{k=0}^{\infty} \frac{(-1)^k}{2k+1}.
```

The error term after $n$ iterations in the standard Leibniz series is approximately the magnitude of the first neglected term:

```math
\lvert E_{\text{Leibniz}} \rvert \approx \frac{1}{2n}.
```

This gives an error that decays on the order of $O(n^{-1})$. To get $6$ digits of accuracy, one typically needs on the order of $10^{6}$ iterations.

For our independently discovered cubic series, the general term is

```math
\lvert a_n \rvert = \frac{1}{2n^3 + 3n^2 + n} \approx \frac{1}{2n^3},
```

which yields an error that decays on the order of $O(n^{-3})$.

Because the denominator grows like $n^3$, the terms diminish much faster. Comparing error terms,

```math
\frac{E_{\text{new}}}{E_{\text{Leibniz}}}
  \approx \frac{1/(2n^3)}{1/(2n)}
  = \frac{1}{n^2}.
```

This implies that for every order-of-magnitude increase in iterations, this series gains roughly three decimal digits of accuracy, whereas the Leibniz series gains only one.

### Comparison at the 314th Iteration

At $x = 314$ (chosen for the digits of $\pi$):

* **Leibniz error**

  ```math
  \approx \frac{1}{2 \cdot 314} \approx 1.5 \times 10^{-3}.
  ```

* **Cubic series error**

  ```math
  \approx \frac{1}{2 \cdot 314^3}
  \approx \frac{1}{61{,}917{,}392}
  \approx 1.6 \times 10^{-8}.
  ```

Comparing $10^{-3}$ and $10^{-8}$, the discovered series effectively calculates about **five more digits of accuracy** than the standard Leibniz series by the 314th iteration.

## 5. Conclusion

We have proven that the series converges to $3 - \pi$. Furthermore, the discovery of this form highlights a significant computational advantage: by algebraically restructuring the series, we achieve a convergence rate on the order of $n^{-3}$, transforming the notoriously slow Leibniz series into a rapidly converging algorithm for computing $\pi$.

Q.E.D.
