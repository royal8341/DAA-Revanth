def factors(n):
    return [i for i in range(1, n + 1) if n % i == 0]

# Example usage:
n = 28
print(f"Factors of {n} are: {factors(n)}")
