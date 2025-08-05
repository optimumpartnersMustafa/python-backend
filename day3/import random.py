import random

def generate_random_numbers(count, min_val, max_val):
    if count <= 0:
        return []
    if min_val > max_val:
        min_val, max_val = max_val, min_val
    return [random.uniform(min_val, max_val) for _ in range(count)]

import statistics
import math

def calculate_mean(data):
    if not data:
        return None
    return statistics.mean(data)

def calculate_median(data):
    if not data:
        return None
    return statistics.median(data)

def calculate_stdev(data):
    if len(data) < 2:
        return None
    return statistics.stdev(data)

def calculate_variance_and_sqrt(data):
    if len(data) < 2:
        return None, None
    variance = statistics.variance(data)
    stdev_from_sqrt = math.sqrt(variance)
    return variance, stdev_from_sqrt

def main():
    print("--- Statistical Analysis Program ---")

    num_samples = 100
    min_value = 0.0
    max_value = 100.0
    data = generate_random_numbers(num_samples, min_value, max_value)

    if not data:
        print("No data generated.")
        return

    print(f"Generated {num_samples} numbers.")

    mean_val = calculate_mean(data)
    if mean_val is not None:
        print(f"Mean: {mean_val:.4f}")

    median_val = calculate_median(data)
    if median_val is not None:
        print(f"Median: {median_val:.4f}")

    stdev_val = calculate_stdev(data)
    if stdev_val is not None:
        print(f"Standard Deviation: {stdev_val:.4f}")

    variance_val, stdev_from_sqrt_val = calculate_variance_and_sqrt(data)
    if variance_val is not None:
        print(f"Variance: {variance_val:.4f}")

    print("--- Program Finished ---")

if __name__ == "__main__":
    main()
