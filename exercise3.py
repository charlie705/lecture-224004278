import random
import statistics


random_numbers = [random.randint(1, 50) for _ in range(100)]

# Step 2: Compute statistics
mean = statistics.mean(random_numbers)
median = statistics.median(random_numbers)
mode = statistics.mode(random_numbers)
std_dev = statistics.stdev(random_numbers)


print("Generated random numbers:")
print(random_numbers)
print(f"\nMean: {mean}")
print(f"Median: {median}")
print(f"Mode: {mode}")
print(f"Standard Deviation: {std_dev}")