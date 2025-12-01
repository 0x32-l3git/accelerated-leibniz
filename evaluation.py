from __future__ import annotations

import math


def leibniz_partial(n: int) -> float:
    if n < 0:
        raise ValueError("n must be non negative")
    total = 0.0
    sign = 1.0
    for k in range(n + 1):
        total += sign / (2 * k + 1)
        sign = -sign
    return 4.0 * total


def cubic_partial(n: int) -> float:
    if n < 0:
        raise ValueError("n must be non negative")
    total = 0.0
    sign = -1.0
    for x in range(1, n + 1):
        denom = 2 * x**3 + 3 * x**2 + x
        total += sign / denom
        sign = -sign
    return 3.0 - total


def digits_of_accuracy(approx: float, true_value: float = math.pi, max_digits: int = 15) -> int:
    error = abs(approx - true_value)
    if error == 0.0:
        return max_digits
    try:
        estimate = int(-math.log10(error))
    except:
        return max_digits
    return max(0, min(max_digits, estimate))


def run_pi_prefixes() -> None:
    n_values = [3, 31, 314, 3141, 31415]

    for n in n_values:
        le = leibniz_partial(n)
        cu = cubic_partial(n)

        le_err = abs(le - math.pi)
        cu_err = abs(cu - math.pi)

        le_dig = digits_of_accuracy(le)
        cu_dig = digits_of_accuracy(cu)

        print("For n =", n)
        print("  Leibniz approximation error:", le_err)
        print("  Estimated correct digits:", le_dig)
        print("  Accelerated approximation error:", cu_err)
        print("  Estimated correct digits:", cu_dig)
        print()


def main() -> None:
    run_pi_prefixes()


if __name__ == "__main__":
    main()
