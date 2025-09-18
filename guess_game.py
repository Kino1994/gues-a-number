#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Guess a Number — Thirds vs Pure Binary Strategy (Large N)

Simulates two strategies:
1) Thirds → Binary
2) Pure Binary

Runs 1,000,000 simulations per range/strategy
for ranges:
- 1..100
- 1..1,000
- 1..10,000
- 1..100,000
- 1..1,000,000
- 1..10,000,000
- 1..100,000,000
- 1..1,000,000,000
"""

import numpy as np
import pandas as pd


# -------------------------------
# Strategies (on-the-fly)
# -------------------------------

def thirds_then_binary_questions(N: int, x: int) -> int:
    """Number of questions with Thirds→Binary strategy (on-the-fly)."""
    t1 = N // 3
    t2 = (2 * N) // 3
    q = 0

    q += 1
    if x <= t1:
        low, high = 1, t1
    else:
        q += 1
        if x <= t2:
            low, high = t1 + 1, t2
        else:
            low, high = t2 + 1, N

    while low < high:
        mid = (low + high) // 2
        q += 1
        if x <= mid:
            high = mid
        else:
            low = mid + 1
    return q


def pure_binary_questions(N: int, x: int) -> int:
    """Number of questions with Pure Binary strategy (on-the-fly)."""
    low, high = 1, N
    q = 0
    while low < high:
        mid = (low + high) // 2
        q += 1
        if x <= mid:
            high = mid
        else:
            low = mid + 1
    return q


# -------------------------------
# Simulation
# -------------------------------

def simulate_on_the_fly(N: int, fn, num_trials: int, rng: np.random.Generator):
    """Run num_trials simulations on the fly (no precomputation)."""
    choices = rng.integers(1, N + 1, size=num_trials)
    return np.fromiter((fn(N, int(x)) for x in choices), dtype=np.int16, count=num_trials)


def summarize_with_deciles(sims: np.ndarray):
    stats = {
        "Mean": float(np.mean(sims)),
        "Std": float(np.std(sims, ddof=0)),
        "Min": int(np.min(sims)),
        "P50": float(np.quantile(sims, 0.50, method="midpoint")),
        "P90": float(np.quantile(sims, 0.90, method="midpoint")),
        "P99": float(np.quantile(sims, 0.99, method="midpoint")),
        "Max": int(np.max(sims)),
    }
    for p in range(10, 101, 10):
        stats[f"P{p}"] = float(np.quantile(sims, p / 100, method="midpoint"))
    return stats


# -------------------------------
# Main
# -------------------------------

def run_experiments(num_trials=1_000_000, seed=2025):
    rng = np.random.default_rng(seed)

    ranges = [100, 1000, 10_000, 100_000, 1_000_000,
              10_000_000, 100_000_000, 1_000_000_000]
    strategies = {
        "Thirds→Binary": thirds_then_binary_questions,
        "Pure Binary": pure_binary_questions,
    }

    results = []
    for N in ranges:
        for name, fn in strategies.items():
            print(f"\n=== Running {name}, N={N} ===")
            sims = simulate_on_the_fly(N, fn, num_trials, rng)
            stats = summarize_with_deciles(sims)
            stats["Range"] = f"1..{N}"
            stats["Strategy"] = name
            results.append(stats)

    df = pd.DataFrame(results)
    print("\n=== Final Results (1M simulations each) ===")
    print(df.to_string(index=False))
    df.to_csv("summary_results_large.csv", index=False)


if __name__ == "__main__":
    run_experiments()

