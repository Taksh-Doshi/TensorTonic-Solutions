from collections import Counter
import numpy as np

def mean_median_mode(x: list) -> dict:
    """
    Returns a dictionary with mean, median, and mode.
    """
    numbers = x

    mean = sum(numbers) / len(numbers)

    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)

    if n % 2 == 1:
        median = float(sorted_numbers[n // 2])
    else:
        median = (sorted_numbers[n // 2 - 1] + sorted_numbers[n // 2]) / 2

    counts = Counter(numbers)
    mode = float(counts.most_common(1)[0][0])

    return {
        "mean": mean,
        "median": median,
        "mode": mode
    }