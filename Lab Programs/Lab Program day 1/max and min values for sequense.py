def min_max_sequence(lst):
    min_value = min(lst)
    max_value = max(lst)
    return min_value, max_value

# Example usage:
lst = [3, 1, 4, 1, 5, 9, 2, 6, 5]
min_value, max_value = min_max_sequence(lst)
print(f"Minimum value: {min_value}, Maximum value: {max_value}")
